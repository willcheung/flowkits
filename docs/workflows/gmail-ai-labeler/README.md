# Gmail AI Email Labeler
# AI-enhanced email categorization — reads your inbox, uses GPT to categorize, labels automatically.

## What It Does
Monitors your Gmail inbox for new unread emails every 5 minutes, uses OpenAI to analyze each email's subject and content, then applies the appropriate label. If no existing label fits, it creates a new one.

## Why This Beats the n8n Version
- **Retry logic** — if Gmail API rate-limits you, it backs off and retries (up to 3x with exponential delay)
- **Label caching** — doesn't refetch labels on every email, caches for 10 minutes
- **Better AI prompt** — configurable categorization rules, not just "pick a label"
- **Proper error handling** — if OpenAI fails, emails get "Uncategorized" instead of breaking the whole workflow
- **Runs anywhere** — no n8n server required. Cron job, systemd, or any scheduler

## Setup

### 1. Gmail API Credentials
1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a project (or use existing)
3. Enable Gmail API
4. Create OAuth 2.0 credentials (Desktop app)
5. Download JSON → save to `~/.flowkits/gmail-ai-labeler/credentials.json`

### 2. OpenAI API Key
```bash
export OPENAI_API_KEY="sk-..."
```

### 3. Install Dependencies
```bash
pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib openai
```

### 4. Run
```bash
python workflow.py
```

First run will open a browser for Gmail OAuth. After that, it runs silently.

### 5. Schedule (optional)
```bash
# Run every 5 minutes
crontab -e
*/5 * * * * /usr/bin/python3 /path/to/workflow.py >> ~/.flowkits/gmail-ai-labeler/log.txt 2>&1
```

## Customization

Edit `SYSTEM_PROMPT` in `workflow.py` to change how emails are categorized:
- Add your own label hierarchy rules
- Filter out senders/domains you don't want labeled
- Set sensitivity thresholds

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `CHECK_INTERVAL` | 300 (5 min) | Seconds between email checks |
| `POLL_LOOKBACK_MINUTES` | 10 | How far back to look for new emails |
| `OPENAI_API_KEY` | env var | Your OpenAI API key |
| `TOKEN_PATH` | `~/.flowkits/gmail-ai-labeler/token.json` | OAuth token storage |
| `CREDS_PATH` | `~/.flowkits/gmail-ai-labeler/credentials.json` | Google OAuth credentials |

## Requirements
- Python 3.10+
- Google Cloud project with Gmail API enabled
- OpenAI API key (GPT-4o-mini recommended — cheap and fast)
