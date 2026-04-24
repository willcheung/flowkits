# Pre-Meeting AI News Briefing — AI Agent Context

## What This Is
Python automation that scans Google Calendar for upcoming meetings, fetches recent news about each company, generates AI briefings with talking points and things to avoid, and delivers via email.

## Architecture
- `workflow.py` — Single-file automation. Entry point: `run()`
- Google Calendar API or JSON file for meeting input
- NewsAPI for company news
- OpenAI GPT-4o-mini for briefing generation
- SMTP for email delivery

## Key Functions
- `PreMeetingBriefing.get_upcoming_meetings_from_google()` — Google Calendar integration
- `PreMeetingBriefing.get_upcoming_meetings_from_json()` — JSON file input (testing)
- `PreMeetingBriefing._extract_company_from_title()` — Parses meeting titles for company names
- `PreMeetingBriefing.fetch_company_news()` — NewsAPI integration
- `PreMeetingBriefing.generate_briefing()` — AI briefing generation
- `PreMeetingBriefing.send_briefing_email()` — HTML + plain text email delivery
- `PreMeetingBriefing.run()` — Full pipeline

## AI Enhancement Over n8n Original
1. Smarter company extraction from meeting titles
2. Structured briefing format (talking points, things to avoid, quick stats)
3. Skips internal meetings automatically (standups, 1:1s)
4. HTML + plain text email rendering
5. Flexible input (Google Calendar or JSON)
6. Graceful handling of missing API keys

## Setup Requirements
- `OPENAI_API_KEY`, `NEWS_API_KEY` environment variables
- Google Calendar OAuth (optional)
- SMTP credentials (optional)

## How to Extend
- Add CRM integration (Salesforce, HubSpot) for contact enrichment
- Add LinkedIn company data
- Add Slack/Teams delivery instead of email
- Add meeting notes generation post-call
