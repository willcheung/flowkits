# FlowKits Workflow: Pre-Meeting AI News Briefing
# Category: Sales
# Original inspiration: n8n workflow #2110
# Price: $15

import os
import json
import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime, timedelta
from dataclasses import dataclass
from typing import Optional

import requests
from openai import OpenAI

# --- Configuration ---
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")  # https://newsapi.org

# Email config (SMTP)
SMTP_SERVER = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "")
SMTP_PASS = os.environ.get("SMTP_PASS", "")
EMAIL_FROM = os.environ.get("EMAIL_FROM", SMTP_USER)
EMAIL_TO = os.environ.get("EMAIL_TO", SMTP_USER)

# Briefing window
BRIEFING_HOURS_AHEAD = 24  # Look for meetings in next 24 hours
NEWS_DAYS_BACK = 7  # How far back to search for news

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("pre-meeting-briefing")

SYSTEM_PROMPT = """You are an executive briefing assistant. Given a company name and a list of recent 
news articles about them, create a concise pre-meeting briefing.

Format:
## Company: {company}
## Meeting: {meeting_title} at {meeting_time}

### Key Headlines (last 7 days)
- Bullet points of the most important news

### Talking Points
- 3-5 conversation starters based on recent news

### Things to Avoid
- Any sensitive topics or recent negative press to steer around

### Quick Stats (if available)
- Revenue, funding, headcount changes, product launches

Be specific. Reference actual headlines. A salesperson should read this 5 minutes before a call and sound informed."""

USER_PROMPT_TEMPLATE = """Create a pre-meeting briefing:

Company: {company}
Meeting: {meeting_title}
Time: {meeting_time}

Recent news about {company}:
{news_articles}

Create a concise, actionable briefing."""


@dataclass
class CalendarEvent:
    title: str
    company: str
    start_time: datetime
    attendees: list[str]
    description: str


@dataclass
class NewsArticle:
    title: str
    description: str
    url: str
    source: str
    published_at: str


@dataclass
class Briefing:
    company: str
    meeting_title: str
    meeting_time: str
    briefing_text: str
    articles_used: int


class PreMeetingBriefing:
    """Scans calendar for upcoming meetings, fetches company news, creates AI briefings."""

    def __init__(self):
        self.openai = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
        self.session = requests.Session()

    # --- Calendar Integration ---
    # Supports Google Calendar API or Microsoft Graph
    # For simplicity, also supports a JSON file input for demo/testing

    def get_upcoming_meetings_from_google(self, credentials_path: str = "~/.flowkits/pre-meeting-briefing/credentials.json") -> list[CalendarEvent]:
        """Fetch upcoming meetings from Google Calendar API."""
        try:
            from google.oauth2.credentials import Credentials
            from google_auth_oauthlib.flow import InstalledAppFlow
            from google.auth.transport.requests import Request
            import googleapiclient.discovery

            SCOPES = ["https://www.googleapis.com/auth/calendar.readonly"]
            creds_path = os.path.expanduser(credentials_path)
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

            service = googleapiclient.discovery.build("calendar", "v1", credentials=creds)
            now = datetime.utcnow().isoformat() + "Z"
            end = (datetime.utcnow() + timedelta(hours=BRIEFING_HOURS_AHEAD)).isoformat() + "Z"

            events_result = (
                service.events()
                .list(calendarId="primary", timeMin=now, timeMax=end, singleEvents=True, orderBy="startTime")
                .execute()
            )

            events = []
            for event in events_result.get("items", []):
                start = event.get("start", {}).get("dateTime", event.get("start", {}).get("date", ""))
                if not start:
                    continue
                # Extract company name from event title (common patterns)
                title = event.get("summary", "Meeting")
                company = self._extract_company_from_title(title)
                events.append(
                    CalendarEvent(
                        title=title,
                        company=company,
                        start_time=datetime.fromisoformat(start.replace("Z", "+00:00")),
                        attendees=[a.get("email", "") for a in event.get("attendees", [])],
                        description=event.get("description", ""),
                    )
                )
            return events

        except ImportError:
            logger.warning("Google Calendar libraries not installed. Use get_upcoming_meetings_from_json() instead.")
            return []

    def get_upcoming_meetings_from_json(self, json_path: str) -> list[CalendarEvent]:
        """Load meetings from a JSON file (for testing or custom calendar integrations)."""
        with open(json_path) as f:
            data = json.load(f)

        events = []
        for meeting in data:
            events.append(
                CalendarEvent(
                    title=meeting["title"],
                    company=self._extract_company_from_title(meeting["title"]),
                    start_time=datetime.fromisoformat(meeting["start_time"]),
                    attendees=meeting.get("attendees", []),
                    description=meeting.get("description", ""),
                )
            )
        return events

    def _extract_company_from_title(self, title: str) -> str:
        """Extract company name from meeting title. Handles common patterns."""
        # Remove common prefixes
        cleaned = title
        for prefix in ["Meeting with ", "Call with ", "1:1 with ", "Sync with ", "Interview - ", "Catch up: "]:
            cleaned = cleaned.replace(prefix, "")

        # Remove common suffixes
        for suffix in [" - follow up", " (reschedule)", " - recurring", " meeting", " call"]:
            cleaned = cleaned.replace(suffix, "")

        return cleaned.strip()

    # --- News Fetching ---

    def fetch_company_news(self, company: str, max_articles: int = 10) -> list[NewsArticle]:
        """Fetch recent news about a company from NewsAPI."""
        if not NEWS_API_KEY:
            logger.warning("NEWS_API_KEY not set. Skipping news fetch.")
            return []

        from_date = (datetime.now() - timedelta(days=NEWS_DAYS_BACK)).strftime("%Y-%m-%d")

        try:
            response = self.session.get(
                "https://newsapi.org/v2/everything",
                params={
                    "q": company,
                    "from": from_date,
                    "sortBy": "publishedAt",
                    "pageSize": max_articles,
                    "apiKey": NEWS_API_KEY,
                },
                timeout=10,
            )
            response.raise_for_status()
            data = response.json()

            articles = []
            for article in data.get("articles", []):
                articles.append(
                    NewsArticle(
                        title=article["title"],
                        description=article.get("description", "") or "",
                        url=article["url"],
                        source=article["source"]["name"],
                        published_at=article["publishedAt"],
                    )
                )
            return articles

        except Exception as e:
            logger.error(f"News fetch failed for {company}: {e}")
            return []

    # --- AI Briefing Generation ---

    def generate_briefing(self, event: CalendarEvent, articles: list[NewsArticle]) -> Optional[Briefing]:
        """Generate an AI briefing for a meeting."""
        if not self.openai:
            logger.error("OpenAI API key not set")
            return None

        if not articles:
            logger.info(f"No news found for {event.company}. Skipping briefing.")
            return None

        news_text = "\n".join(
            f"- [{a.source}] {a.title}: {a.description}" for a in articles[:10]
        )

        prompt = USER_PROMPT_TEMPLATE.format(
            company=event.company,
            meeting_title=event.title,
            meeting_time=event.start_time.strftime("%A, %B %d at %I:%M %p"),
            news_articles=news_text,
        )

        try:
            response = self.openai.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
                max_tokens=1500,
            )

            briefing_text = response.choices[0].message.content

            return Briefing(
                company=event.company,
                meeting_title=event.title,
                meeting_time=event.start_time.strftime("%I:%M %p"),
                briefing_text=briefing_text,
                articles_used=len(articles),
            )

        except Exception as e:
            logger.error(f"Briefing generation failed: {e}")
            return None

    # --- Email Delivery ---

    def send_briefing_email(self, briefing: Briefing) -> bool:
        """Send a briefing via email."""
        if not SMTP_USER or not SMTP_PASS:
            logger.warning("SMTP credentials not set. Cannot send email.")
            return False

        try:
            msg = MIMEMultipart("alternative")
            msg["Subject"] = f"📋 Pre-Meeting Briefing: {briefing.company} ({briefing.meeting_time})"
            msg["From"] = EMAIL_FROM
            msg["To"] = EMAIL_TO

            # Plain text version
            text_content = briefing.briefing_text
            msg.attach(MIMEText(text_content, "plain"))

            # HTML version
            html_lines = briefing.briefing_text.split("\n")
            html_content = "<html><body style='font-family: -apple-system, sans-serif; max-width: 600px; margin: 0 auto;'>"
            for line in html_lines:
                if line.startswith("## "):
                    html_content += f"<h2 style='color: #1a1a1a; border-bottom: 2px solid #4A90D9; padding-bottom: 4px;'>{line[3:]}</h2>"
                elif line.startswith("### "):
                    html_content += f"<h3 style='color: #333;'>{line[4:]}</h3>"
                elif line.startswith("- "):
                    html_content += f"<li>{line[2:]}</li>"
                elif line.strip():
                    html_content += f"<p>{line}</p>"
            html_content += "</body></html>"
            msg.attach(MIMEText(html_content, "html"))

            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_USER, SMTP_PASS)
                server.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())

            logger.info(f"Briefing email sent for {briefing.company}")
            return True

        except Exception as e:
            logger.error(f"Email send failed: {e}")
            return False

    # --- Main Pipeline ---

    def run(self, meetings_source: str = "google") -> list[Briefing]:
        """Full pipeline: fetch meetings → get news → generate briefings → email."""
        logger.info("Pre-Meeting Briefing pipeline starting...")

        # 1. Get upcoming meetings
        if meetings_source == "google":
            events = self.get_upcoming_meetings_from_google()
        elif meetings_source == "json":
            events = self.get_upcoming_meetings_from_json(
                os.path.expanduser("~/.flowkits/pre-meeting-briefing/meetings.json")
            )
        else:
            logger.error(f"Unknown meetings source: {meetings_source}")
            return []

        if not events:
            logger.info("No upcoming meetings found.")
            return []

        logger.info(f"Found {len(events)} upcoming meeting(s).")

        # 2. Process each meeting
        briefings = []
        for event in events:
            if not event.company or event.company.lower() in ("meeting", "standup", "sync", "1:1"):
                logger.info(f"Skipping internal meeting: {event.title}")
                continue

            logger.info(f"Processing: {event.title} ({event.company})")

            # Fetch news
            articles = self.fetch_company_news(event.company)
            logger.info(f"  Found {len(articles)} news article(s)")

            # Generate briefing
            briefing = self.generate_briefing(event, articles)
            if briefing:
                briefings.append(briefing)
                logger.info(f"  Briefing generated ({briefing.articles_used} articles used)")

                # Send email
                self.send_briefing_email(briefing)

        logger.info(f"Generated {len(briefings)} briefing(s).")
        return briefings


def run():
    """Entry point."""
    briefing = PreMeetingBriefing()
    return briefing.run()


if __name__ == "__main__":
    results = run()
    for b in results:
        print(f"\n{'='*60}")
        print(f"BRIEFING: {b.company}")
        print(f"{'='*60}")
        print(b.briefing_text)
