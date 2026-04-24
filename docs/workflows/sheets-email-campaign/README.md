# Google Sheets Email Campaign Sender
# Personalized email campaigns from a spreadsheet, powered by AI.

## What It Does
Reads recipients from Google Sheets, personalizes each email using AI, sends via SMTP, and tracks status back to the sheet. Supports multi-step sequences with auto follow-up for non-responders.

## Why This Beats the n8n Version
- **AI personalization** — each email is tailored to the recipient, not just mail-merged
- **Auto follow-up** — detects non-responders and sends a contextual follow-up
- **Retry logic** — 3 attempts with exponential backoff on send failures
- **Weekend skip** — won't send on Saturdays/Sundays
- **Rate limiting** — configurable delay between emails + max per run
- **Status tracking** — updates Google Sheet in real-time (sent, bounced, replied)

## Setup

### 1. Google Sheets API
1. Create a Google Sheet with columns: `Email | Name | Company | Status | SentAt`
2. Follow the [Google Sheets API quickstart](https://developers.google.com/sheets/api/quickstart/python)
3. Save credentials to `~/.flowkits/sheets-email-campaign/credentials.json`

### 2. Environment Variables
```bash
export SMTP_USER="you@gmail.com"
export SMTP_PASS="app-password"
export GOOGLE_SHEET_ID="your-sheet-id-from-url"
export SHEET_NAME="Sheet1"
export OPENAI_API_KEY="sk-..."  # Optional — enables AI personalization
```

### 3. Install
```bash
pip install requests openai google-api-python-client google-auth-oauthlib
```

### 4. Run
```bash
# First email in sequence
python workflow.py "Hi {{name}}, I noticed {{company}} is growing fast..." "Quick question about {{company}}"

# Follow-up for non-responders
python workflow.py --follow-up "Quick question about your growth"
```

### 5. Schedule
```bash
# Send follow-ups every 3 days at 9am
0 9 */3 * * /usr/bin/python3 /path/to/workflow.py --follow-up "Following up" >> log.txt 2>&1
```

## Google Sheet Format

| Email | Name | Company | Status | SentAt |
|-------|------|---------|--------|--------|
| alice@acme.com | Alice | Acme Corp | pending | |
| bob@startup.io | Bob | Startup | sent | 2026-04-17T09:00:00 |

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `SEND_DELAY_SECONDS` | 5 | Delay between emails (avoid spam filters) |
| `MAX_EMAILS_PER_RUN` | 50 | Safety limit per execution |
| `SKIP_WEEKENDS` | True | Don't send on Saturday/Sunday |
| `SMTP_SERVER` | smtp.gmail.com | SMTP server |

## Requirements
- Python 3.10+
- Google Sheets API credentials
- SMTP credentials (Gmail app password works)
- OpenAI API key (optional — enables personalization)
