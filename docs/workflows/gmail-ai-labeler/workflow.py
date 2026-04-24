# FlowKits Workflow: Gmail AI Email Labeler
# Category: AI / Personal Productivity
# Original inspiration: n8n workflow #2740
# Price: FREE (lead magnet)

import os
import json
import time
import logging
from datetime import datetime, timedelta
from dataclasses import dataclass, field
from typing import Optional

import googleapiclient.discovery
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from openai import OpenAI

# --- Configuration ---
SCOPES = [
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.labels",
]
TOKEN_PATH = os.path.expanduser("~/.flowkits/gmail-ai-labeler/token.json")
CREDS_PATH = os.path.expanduser("~/.flowkits/gmail-ai-labeler/credentials.json")
CHECK_INTERVAL = 300  # 5 minutes (same as n8n workflow)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("gmail-ai-labeler")

# AI Enhancement: configurable categorization rules
SYSTEM_PROMPT = """You are an email categorization assistant. Given an email's subject, 
sender, and body preview, choose the most appropriate label from the existing labels list.
If none fit well, suggest a new label.

Rules:
- Be specific but not too granular (max 2 levels like "Work/ProjectX")
- Never label promotional/marketing emails as important
- If email looks like spam/phishing, suggest "Spam" or "Phishing"
- Respond with ONLY the label name, nothing else"""

USER_PROMPT_TEMPLATE = """Categorize this email:

Subject: {subject}
From: {from}
Snippet: {snippet}

Existing labels: {labels}

Choose the best existing label, or suggest a new one if none fit."""

POLL_LOOKBACK_MINUTES = 10  # Check emails from last 10 minutes


@dataclass
class LabelResult:
    message_id: str
    subject: str
    assigned_label: str
    is_new_label: bool = False
    confidence: str = "high"


class GmailAIClient:
    """Enhanced Gmail + AI email labeler with retry logic and error handling."""

    def __init__(self):
        self.gmail = self._get_gmail_service()
        self.openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
        self._label_cache: Optional[list[str]] = None
        self._label_cache_time: Optional[datetime] = None

    def _get_gmail_service(self):
        """Authenticate with Gmail API. Handles token refresh."""
        creds = None
        if os.path.exists(TOKEN_PATH):
            creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDS_PATH, SCOPES)
                creds = flow.run_local_server(port=0)
            os.makedirs(os.path.dirname(TOKEN_PATH), exist_ok=True)
            with open(TOKEN_PATH, "w") as f:
                f.write(creds.to_json())

        return googleapiclient.discovery.build("gmail", "v1", credentials=creds)

    def get_labels(self, force_refresh: bool = False) -> list[str]:
        """Fetch all Gmail labels with caching (refreshes every 10 minutes)."""
        if (
            self._label_cache
            and not force_refresh
            and self._label_cache_time
            and (datetime.now() - self._label_cache_time).seconds < 600
        ):
            return self._label_cache

        results = self.gmail.users().labels().list(userId="me").execute()
        labels = results.get("labels", [])
        # Filter out system labels
        self._label_cache = [
            l["name"] for l in labels if not l["name"].startswith("CATEGORY_")
        ]
        self._label_cache_time = datetime.now()
        return self._label_cache

    def get_unread_emails(self, max_results: int = 20) -> list[dict]:
        """Fetch unread emails from the last POLL_LOOKBACK_MINUTES."""
        after = (datetime.now() - timedelta(minutes=POLL_LOOKBACK_MINUTES)).strftime("%Y/%m/%d")
        query = f"is:unread newer_than:{POLL_LOOKBACK_MINUTES}m"

        results = (
            self.gmail.users()
            .messages()
            .list(userId="me", q=query, maxResults=max_results)
            .execute()
        )

        messages = results.get("messages", [])
        emails = []
        for msg in messages:
            detail = (
                self.gmail.users()
                .messages()
                .get(userId="me", id=msg["id"], format="metadata", metadataHeaders=["From", "Subject"])
                .execute()
            )
            headers = {h["name"]: h["value"] for h in detail.get("payload", {}).get("headers", [])}
            snippet = detail.get("snippet", "")[:500]
            emails.append(
                {
                    "id": msg["id"],
                    "subject": headers.get("Subject", "(no subject)"),
                    "from": headers.get("From", "unknown"),
                    "snippet": snippet,
                }
            )
        return emails

    def categorize_email(self, email: dict) -> str:
        """Use OpenAI to categorize an email. Returns the label name."""
        labels = self.get_labels()
        prompt = USER_PROMPT_TEMPLATE.format(
            subject=email["subject"],
            from=email["from"],
            snippet=email["snippet"],
            labels=", ".join(labels),
        )

        try:
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.1,
                max_tokens=30,
            )
            return response.choices[0].message.content.strip().strip('"')
        except Exception as e:
            logger.warning(f"OpenAI categorization failed: {e}")
            return "Uncategorized"

    def apply_label(self, message_id: str, label_name: str) -> bool:
        """Apply a label to an email. Creates the label if it doesn't exist."""
        try:
            # Check if label exists
            labels = self.gmail.users().labels().list(userId="me").execute().get("labels", [])
            label_id = None
            is_new = False

            for label in labels:
                if label["name"].lower() == label_name.lower():
                    label_id = label["id"]
                    break

            if not label_id:
                # Create new label
                label_result = (
                    self.gmail.users()
                    .labels()
                    .create(userId="me", body={"name": label_name, "labelListVisibility": "labelShow"})
                    .execute()
                )
                label_id = label_result["id"]
                is_new = True
                logger.info(f"Created new label: {label_name}")

            # Apply label
            self.gmail.users().messages().modify(
                userId="me", id=message_id, body={"addLabelIds": [label_id]}
            ).execute()
            return is_new

        except Exception as e:
            logger.error(f"Failed to apply label '{label_name}' to {message_id}: {e}")
            return False

    def process_emails(self) -> list[LabelResult]:
        """Main loop: fetch unread emails, categorize, and label them."""
        emails = self.get_unread_emails()
        if not emails:
            logger.debug("No new emails to process.")
            return []

        results = []
        for email in emails:
            logger.info(f"Processing: {email['subject'][:60]}...")

            # AI categorization
            label = self.categorize_email(email)

            # Apply label with retry
            is_new = False
            for attempt in range(3):
                try:
                    is_new = self.apply_label(email["id"], label)
                    break
                except Exception as e:
                    logger.warning(f"Retry {attempt + 1}/3 for label application: {e}")
                    time.sleep(2 ** attempt)

            results.append(
                LabelResult(
                    message_id=email["id"],
                    subject=email["subject"],
                    assigned_label=label,
                    is_new_label=is_new,
                )
            )
            logger.info(f"  → Labeled: {label}" + (" (new)" if is_new else ""))

        return results


def run():
    """Entry point. Runs once, then returns. Schedule externally (cron, systemd, etc.)."""
    logger.info("Gmail AI Labeler starting...")
    client = GmailAIClient()
    results = client.process_emails()
    logger.info(f"Processed {len(results)} emails.")
    for r in results:
        status = "NEW" if r.is_new_label else "existing"
        logger.info(f"  [{status}] {r.subject[:50]} → {r.assigned_label}")
    return results


if __name__ == "__main__":
    run()
