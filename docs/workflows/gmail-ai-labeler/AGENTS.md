# Gmail AI Email Labeler — AI Agent Context

## What This Is
A Python automation that monitors Gmail, uses OpenAI to categorize incoming emails, and applies Gmail labels automatically. Replaces the n8n Gmail + OpenAI workflow with better error handling and retry logic.

## Architecture
- `workflow.py` — Single-file automation. Entry point: `run()`
- Gmail API via `google-api-python-client` with OAuth2
- OpenAI GPT-4o-mini for categorization (cheap, fast)
- Designed to run as a cron job or scheduled task

## Key Functions
- `GmailAIClient.__init__()` — Sets up Gmail + OpenAI clients
- `GmailAIClient.get_unread_emails()` — Fetches unread emails from last 10 minutes
- `GmailAIClient.categorize_email()` — Sends email to OpenAI, returns label name
- `GmailAIClient.apply_label()` — Applies label to Gmail message (creates if new)
- `GmailAIClient.process_emails()` — Main pipeline: fetch → categorize → label
- `run()` — Entry point, runs once then returns

## AI Enhancement Over n8n Original
1. Retry logic with exponential backoff (3 attempts)
2. Label caching to reduce API calls
3. Graceful degradation (if OpenAI fails → "Uncategorized" label)
4. Configurable system prompt for custom categorization rules
5. No dependency on n8n server infrastructure

## Setup Requirements
- Google Cloud Console → Gmail API → OAuth2 credentials
- `OPENAI_API_KEY` environment variable
- `pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib openai`

## How to Extend
- Change `SYSTEM_PROMPT` for different categorization behavior
- Add webhook notifications in `apply_label()` for real-time alerts
- Add batch processing for high-volume inboxes
- Integrate with Slack/Discord for label change notifications
