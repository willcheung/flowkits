# FlowKits Workflow: Human-in-the-Loop AI Email Responder
# Category: Support
# Original inspiration: n8n workflow #2907
# Price: $19

import os
import json
import logging
import imaplib
import email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

import smtplib
from openai import OpenAI

# --- Configuration ---
IMAP_SERVER = os.environ.get("IMAP_SERVER", "imap.gmail.com")
IMAP_USER = os.environ.get("IMAP_USER", "")
IMAP_PASS = os.environ.get("IMAP_PASS", "")

SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", IMAP_USER)
SMTP_PASS = os.environ.get("SMTP_PASS", IMAP_PASS)
APPROVER_EMAIL = os.environ.get("APPROVER_EMAIL", IMAP_USER)  # Who reviews drafts

POLL_INTERVAL = 60  # Check for new emails every 60 seconds
DRAFT_SUBJECT_PREFIX = "[DRAFT] "  # Prefix for draft emails to approver

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("human-in-loop-email")

SYSTEM_PROMPT = """You are an AI email assistant that drafts professional responses to incoming emails.
Given the incoming email, draft a response that is:
- Professional but warm
- Concise (under 200 words)
- Accurate and helpful
- Appropriate in tone for the context

Rules:
- Never invent facts or make promises you can't keep
- If you don't know the answer, say so honestly
- Include a clear next step or question when appropriate
- Match the formality level of the incoming email
- Sign off professionally"""

USER_PROMPT_TEMPLATE = """Draft a response to this email:

From: {from_addr}
To: {to_addr}
Subject: {subject}
Date: {date}

Body:
{body}

Draft a professional response:"""


@dataclass
class IncomingEmail:
    uid: str
    from_addr: str
    to_addr: str
    subject: str
    date: str
    body: str
    raw_message: bytes


@dataclass
class DraftResponse:
    original_subject: str
    original_from: str
    draft_body: str
    draft_subject: str
    needs_approval: bool = True


class HumanInTheLoopResponder:
    """Monitors inbox, drafts AI responses, sends to human approver before sending."""

    def __init__(self):
        self.openai = OpenAI(api_key=os.environ.get("OPENAI_API_KEY")) if os.environ.get("OPENAI_API_KEY") else None

    def _connect_imap(self) -> Optional[imaplib.IMAP4_SSL]:
        """Connect to IMAP server with retry."""
        for attempt in range(3):
            try:
                mail = imaplib.IMAP4_SSL(IMAP_SERVER)
                mail.login(IMAP_USER, IMAP_PASS)
                mail.select("INBOX")
                return mail
            except Exception as e:
                logger.warning(f"IMAP connect attempt {attempt + 1}/3 failed: {e}")
                if attempt < 2:
                    import time
                    time.sleep(5)
        return None

    def get_unread_emails(self, max_emails: int = 10) -> list[IncomingEmail]:
        """Fetch unread emails from inbox."""
        mail = self._connect_imap()
        if not mail:
            return []

        emails = []
        try:
            # Search for unread emails
            status, messages = mail.search(None, "UNSEEN")
            if status != "OK":
                return []

            uid_list = messages[0].split()[:max_emails]

            for uid in uid_list:
                status, msg_data = mail.fetch(uid, "(RFC822)")
                if status != "OK":
                    continue

                raw = msg_data[0][1]
                msg = email.message_from_bytes(raw)

                # Extract fields
                from_addr = msg.get("From", "")
                to_addr = msg.get("To", "")
                subject = msg.get("Subject", "(no subject)")
                date = msg.get("Date", "")

                # Extract body
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type == "text/plain":
                            try:
                                body = part.get_payload(decode=True).decode("utf-8", errors="replace")
                            except:
                                body = "(could not decode)"
                            break
                else:
                    try:
                        body = msg.get_payload(decode=True).decode("utf-8", errors="replace")
                    except:
                        body = "(could not decode)"

                emails.append(
                    IncomingEmail(
                        uid=uid.decode(),
                        from_addr=from_addr,
                        to_addr=to_addr,
                        subject=subject,
                        date=date,
                        body=body[:5000],  # Truncate long emails
                        raw_message=raw,
                    )
                )

        except Exception as e:
            logger.error(f"Failed to fetch emails: {e}")
        finally:
            try:
                mail.close()
                mail.logout()
            except:
                pass

        return emails

    def draft_response(self, incoming: IncomingEmail) -> Optional[DraftResponse]:
        """Use AI to draft a response to an incoming email."""
        if not self.openai:
            logger.error("OpenAI API key not set")
            return None

        prompt = USER_PROMPT_TEMPLATE.format(
            from_addr=incoming.from_addr,
            to_addr=incoming.to_addr,
            subject=incoming.subject,
            date=incoming.date,
            body=incoming.body,
        )

        try:
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.4,
                max_tokens=500,
            )

            draft_body = response.choices[0].message.content.strip()
            draft_subject = f"Re: {incoming.subject}"

            return DraftResponse(
                original_subject=incoming.subject,
                original_from=incoming.from_addr,
                draft_body=draft_body,
                draft_subject=draft_subject,
                needs_approval=True,
            )

        except Exception as e:
            logger.error(f"Draft generation failed: {e}")
            return None

    def send_for_approval(self, draft: DraftResponse) -> bool:
        """Send draft to human approver for review."""
        msg = MIMEMultipart("alternative")
        msg["Subject"] = f"{DRAFT_SUBJECT_PREFIX}{draft.original_subject}"
        msg["From"] = SMTP_USER
        msg["To"] = APPROVER_EMAIL

        # Build approval email
        approval_text = f"""AI has drafted a response to this email:

Original From: {draft.original_from}
Original Subject: {draft.original_subject}

--- DRAFT RESPONSE ---
Subject: {draft.draft_subject}

{draft.draft_body}
--- END DRAFT ---

INSTRUCTIONS:
- Reply with "SEND" to send this response as-is
- Reply with edits to modify before sending
- Reply with "SKIP" to handle manually
- Do nothing and it will be skipped after 24 hours
"""
        msg.attach(MIMEText(approval_text, "plain"))

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASS)
                server.sendmail(SMTP_USER, APPROVER_EMAIL, msg.as_string())
            logger.info(f"Draft sent to {APPROVER_EMAIL} for approval")
            return True
        except Exception as e:
            logger.error(f"Failed to send approval email: {e}")
            return False

    def send_approved_response(self, draft: DraftResponse, to_addr: str) -> bool:
        """Send the approved response to the original sender."""
        msg = MIMEMultipart("alternative")
        msg["Subject"] = draft.draft_subject
        msg["From"] = SMTP_USER
        msg["To"] = to_addr

        msg.attach(MIMEText(draft.draft_body, "plain"))

        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASS)
                server.sendmail(SMTP_USER, to_addr, msg.as_string())
            logger.info(f"Response sent to {to_addr}")
            return True
        except Exception as e:
            logger.error(f"Failed to send response: {e}")
            return False

    def process_pending_approvals(self):
        """Check for approval replies in inbox and send approved responses."""
        # This is a simplified version — in production, you'd track pending drafts
        # in a database or JSON file and match approval replies to drafts
        logger.info("Checking for approval replies...")
        # Implementation would parse replies for "SEND", "SKIP", or edited text
        pass

    def run_once(self) -> list[DraftResponse]:
        """Process unread emails once: fetch → draft → send for approval."""
        logger.info("Human-in-the-Loop Email Responder checking inbox...")

        emails = self.get_unread_emails()
        if not emails:
            logger.info("No unread emails.")
            return []

        drafts = []
        for incoming in emails:
            logger.info(f"Processing: {incoming.subject[:60]}...")

            # Draft AI response
            draft = self.draft_response(incoming)
            if not draft:
                continue

            # Send to human approver
            self.send_for_approval(draft)
            drafts.append(draft)

            # Mark as read (so we don't re-process)
            mail = self._connect_imap()
            if mail:
                try:
                    mail.store(incoming.uid, "+FLAGS", "\\Seen")
                except:
                    pass
                finally:
                    try:
                        mail.close()
                        mail.logout()
                    except:
                        pass

        logger.info(f"Processed {len(drafts)} email(s). Drafts sent for approval.")
        return drafts

    def run(self, continuous: bool = False):
        """Entry point. Run once or continuously."""
        if continuous:
            logger.info("Running in continuous mode. Press Ctrl+C to stop.")
            try:
                while True:
                    self.run_once()
                    self.process_pending_approvals()
                    import time
                    time.sleep(POLL_INTERVAL)
            except KeyboardInterrupt:
                logger.info("Stopped.")
        else:
            return self.run_once()


if __name__ == "__main__":
    import sys
    continuous = "--continuous" in sys.argv or "-c" in sys.argv
    responder = HumanInTheLoopResponder()
    responder.run(continuous=continuous)
