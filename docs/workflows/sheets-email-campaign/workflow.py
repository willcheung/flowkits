# FlowKits Workflow: Google Sheets Email Campaign Sender
# Category: Marketing
# Original inspiration: n8n workflow #2088 + #2137
# Price: $19

import os
import json
import time
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, date
from dataclasses import dataclass, field
from typing import Optional

from openai import OpenAI

# --- Configuration ---
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")
EMAIL_FROM = os.environ.get("EMAIL_FROM", SMTP_USER)

# Google Sheets API
GOOGLE_CREDENTIALS_PATH = os.environ.get("GOOGLE_CREDENTIALS_PATH", "~/.flowkits/sheets-email-campaign/credentials.json")
GOOGLE_SHEET_ID = os.environ.get("GOOGLE_SHEET_ID", "")  # From sheet URL
SHEET_NAME = os.environ.get("SHEET_NAME", "Sheet1")

# Campaign settings
SEND_DELAY_SECONDS = 5  # Delay between emails to avoid spam filters
MAX_EMAILS_PER_RUN = 50  # Safety limit per execution
SKIP_WEEKENDS = True

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("sheets-email-campaign")

# AI Enhancement: personalized email generation
PERSONALIZATION_PROMPT = """You are an expert cold email writer. Given a template and recipient data,
personalize the email. Keep it natural, short, and specific. Don't overdo personalization — 
one or two specific details are enough. The email should feel human, not AI-generated.

Rules:
- Keep the same overall structure and CTA as the template
- Add 1-2 specific details about the recipient/company
- Keep it under 150 words
- Sound like a real person, not marketing copy
- Never use exclamation marks in the first line"""

FOLLOW_UP_PROMPT = """You are writing a follow-up email. The recipient hasn't replied to the first email.
Write a short, polite follow-up (2-3 sentences max). Reference the original topic.
Don't be pushy. Add value (a resource, insight, or question)."""


@dataclass
class Recipient:
    row_index: int
    email: str
    name: str
    company: str = ""
    custom_fields: dict = field(default_factory=dict)
    status: str = "pending"  # pending, sent, replied, bounced, skipped
    sent_at: Optional[str] = None
    thread_id: Optional[str] = None  # For follow-up threading


@dataclass
class CampaignResult:
    sent: int
    skipped: int
    failed: int
    total_processed: int
    details: list[dict]


class SheetsEmailCampaign:
    """Google Sheets → personalized email campaigns with AI and auto follow-up."""

    def __init__(self):
        self.openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY")) if os.environ.get("OPENAI_API_KEY") else None
        self.sheet_service = None

    # --- Google Sheets Integration ---

    def _get_sheets_service(self):
        """Initialize Google Sheets API service."""
        if self.sheet_service:
            return self.sheet_service

        try:
            from google.oauth2.credentials import Credentials
            from google_auth_oauthlib.flow import InstalledAppFlow
            from google.auth.transport.requests import Request
            import googleapiclient.discovery

            SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
            creds_path = os.path.expanduser(GOOGLE_CREDENTIALS_PATH)
            token_path = creds_path.replace("credentials.json", "token.json")

            creds = None
            if os.path.exists(token_path):
                creds = Credentials.from_authorized_user_file(token_path, SCOPES)

            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(creds_path, SCOPES)
                    creds = flow.run_local_server(port=0)
                with open(token_path, "w") as f:
                    f.write(creds.to_json())

            self.sheet_service = googleapiclient.discovery.build("sheets", "v4", credentials=creds)
            return self.sheet_service

        except ImportError:
            logger.error("Google Sheets libraries not installed")
            return None

    def get_recipients(self) -> list[Recipient]:
        """Read recipients from Google Sheet. Expects columns: Email, Name, Company, Status, SentAt"""
        service = self._get_sheets_service()
        if not service or not GOOGLE_SHEET_ID:
            return []

        try:
            result = (
                service.spreadsheets()
                .values()
                .get(spreadsheetId=GOOGLE_SHEET_ID, range=f"{SHEET_NAME}!A2:Z")
                .execute()
            )

            rows = result.get("values", [])
            recipients = []
            for i, row in enumerate(rows):
                if not row or not row[0]:  # Skip empty rows
                    continue

                status = row[3] if len(row) > 3 else "pending"
                if status in ("sent", "replied"):  # Skip already processed
                    continue

                recipients.append(
                    Recipient(
                        row_index=i + 2,  # +2 for 1-indexed + header row
                        email=row[0],
                        name=row[1] if len(row) > 1 else "",
                        company=row[2] if len(row) > 2 else "",
                        status=status,
                        sent_at=row[4] if len(row) > 4 else None,
                    )
                )
            return recipients

        except Exception as e:
            logger.error(f"Failed to read sheet: {e}")
            return []

    def update_row(self, row_index: int, status: str, sent_at: Optional[str] = None):
        """Update a row in Google Sheet with status."""
        service = self._get_sheets_service()
        if not service or not GOOGLE_SHEET_ID:
            return

        values = [[status, sent_at or datetime.now().isoformat()]]
        try:
            service.spreadsheets().values().update(
                spreadsheetId=GOOGLE_SHEET_ID,
                range=f"{SHEET_NAME}!D{row_index}:E{row_index}",
                valueInputOption="RAW",
                body={"values": values},
            ).execute()
        except Exception as e:
            logger.error(f"Failed to update row {row_index}: {e}")

    # --- AI Personalization ---

    def personalize_email(self, template: str, recipient: Recipient) -> str:
        """Use AI to personalize an email template for a specific recipient."""
        if not self.openai:
            return template  # Fall back to raw template

        try:
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": PERSONALIZATION_PROMPT},
                    {
                        "role": "user",
                        "content": f"Template:\n{template}\n\nRecipient: {recipient.name} at {recipient.company}\nEmail: {recipient.email}",
                    },
                ],
                temperature=0.7,
                max_tokens=500,
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            logger.warning(f"AI personalization failed: {e}. Using template as-is.")
            return template

    def generate_follow_up(self, original_subject: str, original_body: str, recipient: Recipient) -> str:
        """Generate a follow-up email for non-responders."""
        if not self.openai:
            return f"Hi {recipient.name},\n\nJust following up on my previous email. Any thoughts?\n\nBest"

        try:
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": FOLLOW_UP_PROMPT},
                    {
                        "role": "user",
                        "content": f"Original subject: {original_subject}\nOriginal body:\n{original_body[:500]}\n\nRecipient: {recipient.name} at {recipient.company}",
                    },
                ],
                temperature=0.7,
                max_tokens=200,
            )
            return response.choices[0].message.content.strip()

        except Exception as e:
            logger.warning(f"AI follow-up generation failed: {e}")
            return f"Hi {recipient.name},\n\nWanted to follow up on my previous email. Let me know if you have any questions.\n\nBest"

    # --- Email Sending ---

    def send_email(
        self,
        to: str,
        subject: str,
        body: str,
        html_body: Optional[str] = None,
        reply_to_id: Optional[str] = None,
    ) -> bool:
        """Send an email via SMTP with retry logic."""
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = EMAIL_FROM
        msg["To"] = to

        msg.attach(MIMEText(body, "plain"))
        if html_body:
            msg.attach(MIMEText(html_body, "html"))

        for attempt in range(3):
            try:
                with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                    server.starttls()
                    server.login(SMTP_USER, SMTP_PASS)
                    server.sendmail(EMAIL_FROM, to, msg.as_string())
                return True
            except Exception as e:
                logger.warning(f"Email send attempt {attempt + 1}/3 failed: {e}")
                if attempt < 2:
                    time.sleep(2 ** attempt)

        return False

    # --- Main Pipeline ---

    def run_campaign(self, template: str, subject: str, follow_up: bool = False) -> CampaignResult:
        """Execute an email campaign from Google Sheets data."""
        if SKIP_WEEKENDS and date.today().weekday() >= 5:
            logger.info("Weekend detected. Skipping campaign.")
            return CampaignResult(0, 0, 0, 0, [])

        recipients = self.get_recipients()
        if not recipients:
            logger.info("No recipients to process.")
            return CampaignResult(0, 0, 0, 0, [])

        # Limit per run
        recipients = recipients[:MAX_EMAILS_PER_RUN]
        logger.info(f"Processing {len(recipients)} recipient(s)...")

        result = CampaignResult(sent=0, skipped=0, failed=0, total_processed=len(recipients), details=[])

        for recipient in recipients:
            logger.info(f"  Sending to: {recipient.name} ({recipient.email})")

            if follow_up and recipient.sent_at:
                # Generate follow-up for non-responders
                body = self.generate_follow_up(subject, template, recipient)
                full_subject = f"Re: {subject}"
            else:
                # Personalize template
                body = self.personalize_email(template, recipient)
                full_subject = subject

            success = self.send_email(recipient.email, full_subject, body)
            if success:
                result.sent += 1
                self.update_row(recipient.row_index, "sent")
                logger.info(f"    ✓ Sent")
            else:
                result.failed += 1
                self.update_row(recipient.row_index, "bounced")
                logger.info(f"    ✗ Failed")

            result.details.append(
                {"email": recipient.email, "name": recipient.name, "success": success}
            )

            # Delay between emails
            if result.sent + result.failed < len(recipients):
                time.sleep(SEND_DELAY_SECONDS)

        logger.info(f"Campaign complete: {result.sent} sent, {result.failed} failed, {result.skipped} skipped")
        return result


def run(template: str, subject: str):
    """Entry point for running a campaign."""
    campaign = SheetsEmailCampaign()
    return campaign.run_campaign(template, subject)


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python workflow.py '<email template>' '<subject>'")
        print("       python workflow.py --follow-up '<subject>'")
        sys.exit(1)

    if sys.argv[1] == "--follow-up":
        campaign = SheetsEmailCampaign()
        result = campaign.run_campaign("", sys.argv[2], follow_up=True)
    else:
        result = run(sys.argv[1], sys.argv[2])

    print(f"\nResults: {result.sent} sent, {result.failed} failed")
