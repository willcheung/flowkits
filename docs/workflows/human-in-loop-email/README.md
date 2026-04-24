# Human-in-the-Loop AI Email Responder
# AI drafts responses. You approve. Safe automation for important emails.

## What It Does
Monitors your inbox for new emails, uses AI to draft professional responses, then sends each draft to YOU for approval before anything goes out. Reply "SEND" to approve, edit to modify, or "SKIP" to handle manually.

## Why This Beats the n8n Version
- **True human-in-the-loop** — drafts go to YOUR inbox for review, not a separate dashboard
- **IMAP + SMTP** — works with Gmail, Outlook, any email provider
- **Multipart email handling** — extracts text from multipart messages correctly
- **Retry logic** — 3 attempts for IMAP connection failures
- **Continuous or one-shot mode** — run once or as a daemon
- **Graceful degradation** — if AI fails, email stays unread for manual handling

## Setup

### 1. Environment Variables
```bash
# IMAP (incoming email)
export IMAP_SERVER="imap.gmail.com"
export IMAP_USER="you@gmail.com"
export IMAP_PASS="app-password"

# SMTP (sending email)
export SMTP_SERVER="smtp.gmail.com"
export SMTP_PORT="587"
export SMTP_USER="you@gmail.com"
export SMTP_PASS="app-password"

# Who approves drafts (usually same as your email)
export APPROVER_EMAIL="you@gmail.com"

# AI
export OPENAI_API_KEY="sk-..."
```

### 2. Install
```bash
pip install openai
```

### 3. Run
```bash
# Check once
python workflow.py

# Run continuously (daemon mode)
python workflow.py --continuous
```

## How It Works

```
1. New email arrives in your inbox
2. AI reads it and drafts a response
3. Draft is forwarded to YOU with [DRAFT] prefix
4. You reply:
   - "SEND" → response goes out to original sender
   - Edited text → your edits are sent instead
   - "SKIP" → nothing happens, handle manually
5. Original email is marked as read
```

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `POLL_INTERVAL` | 60 seconds | How often to check for new emails (continuous mode) |
| `DRAFT_SUBJECT_PREFIX` | "[DRAFT] " | Prefix for approval emails |
| `IMAP_SERVER` | imap.gmail.com | Works with any IMAP server |

## Requirements
- Python 3.10+
- IMAP access to your email (Gmail: use App Password)
- SMTP access (Gmail: use App Password)
- OpenAI API key

## Security Notes
- Your email credentials are stored in environment variables, not in code
- AI drafts are NEVER sent without your approval
- The approver email can be different from the monitored inbox
