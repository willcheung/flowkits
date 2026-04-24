# Pre-Meeting AI News Briefing
# Never walk into a meeting cold again.

## What It Does
Scans your Google Calendar for upcoming meetings, fetches recent news about each company you're meeting with, and generates an AI briefing with talking points, things to avoid, and key stats. Delivers via email before the call.

## Why This Beats the n8n Version
- **Smarter company extraction** — parses meeting titles to find company names (handles "Meeting with Acme Corp", "Sync - Stripe", etc.)
- **Better briefings** — structured format with talking points, things to avoid, and quick stats
- **HTML + plain text email** — looks good in any email client
- **Graceful fallbacks** — skips internal meetings (standups, 1:1s), handles missing API keys
- **Flexible input** — Google Calendar API or JSON file for testing

## Setup

### 1. API Keys
```bash
export OPENAI_API_KEY="sk-..."
export NEWS_API_KEY="..."  # Free tier: https://newsapi.org
```

### 2. Google Calendar (optional — can use JSON input instead)
See Gmail AI Labeler setup for Google OAuth credentials.

### 3. Email (optional — can print to terminal instead)
```bash
export SMTP_USER="you@gmail.com"
export SMTP_PASS="app-password"
export EMAIL_TO="you@gmail.com"
```

### 4. Install
```bash
pip install requests openai google-api-python-client google-auth-oauthlib
```

### 5. Run
```bash
# With Google Calendar
python workflow.py

# With JSON input (for testing)
echo '[{"title": "Call with Stripe", "start_time": "2026-04-18T14:00:00"}]' > ~/.flowkits/pre-meeting-briefing/meetings.json
python workflow.py  # will use JSON since no Google creds
```

### 6. Schedule
```bash
# Run every morning at 7am
0 7 * * * /usr/bin/python3 /path/to/workflow.py >> ~/.flowkits/pre-meeting-briefing/log.txt 2>&1
```

## What You Get Per Meeting
- **Key Headlines** — most important news from last 7 days
- **Talking Points** — 3-5 conversation starters based on recent news
- **Things to Avoid** — sensitive topics or recent negative press
- **Quick Stats** — revenue, funding, headcount changes, product launches

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `BRIEFING_HOURS_AHEAD` | 24 | How far ahead to look for meetings |
| `NEWS_DAYS_BACK` | 7 | How far back to search for news |
| `SMTP_SERVER` | smtp.gmail.com | SMTP server for email delivery |

## Requirements
- Python 3.10+
- OpenAI API key
- NewsAPI key (free tier: 100 requests/day)
- Google Calendar OAuth (optional)
- SMTP credentials (optional — can print to terminal)
