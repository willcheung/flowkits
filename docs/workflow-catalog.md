# FlowKits.ai — Workflow Catalog

## What is FlowKits?
AI-enhanced automation workflows. Not n8n JSON you can't debug. Real Python code with error handling, retry logic, and AI reasoning built in. Every workflow is tested, documented, and ready to run.

## Why FlowKits Over n8n?
- **Runs anywhere** — no n8n server, no Docker, just `python workflow.py`
- **AI-enhanced** — every workflow uses AI for smarter automation
- **Battle-tested** — retry logic, graceful degradation, proper error handling
- **AI-agent ready** — AGENTS.md files let Claude, Cursor, and Copilot extend any workflow
- **Zero vendor lock-in** — your code, your infrastructure

---

## Workflow Catalog

### 🆓 Free Workflows (Lead Magnets)

#### 1. Gmail AI Email Labeler
**Category:** AI / Personal Productivity
**What it does:** Monitors Gmail, uses GPT to categorize emails, applies labels automatically
**Best for:** Anyone drowning in email who wants AI-powered inbox organization
**Tech:** Gmail API, OpenAI GPT-4o-mini
**Files:** `gmail-ai-labeler/`

#### 2. AI Landing Page Analyzer
**Category:** Marketing
**What it does:** Feed it a URL, get a full CRO audit with actionable fixes
**Best for:** Marketers, founders, and agencies who need quick landing page feedback
**Tech:** HTTP requests, OpenAI GPT-4
**Files:** `landing-page-analyzer/`

### 💰 Premium Workflows ($15-25)

#### 3. Pre-Meeting AI News Briefing
**Category:** Sales
**Price:** $15
**What it does:** Scans Google Calendar, fetches company news, generates pre-meeting briefings with talking points
**Best for:** Sales teams and founders who want to walk into every meeting informed
**Tech:** Google Calendar API, NewsAPI, OpenAI GPT-4o-mini, SMTP
**Files:** `pre-meeting-briefing/`

#### 4. Google Sheets Email Campaign Sender
**Category:** Marketing
**Price:** $19
**What it does:** Personalized email campaigns from Google Sheets with AI personalization and auto follow-up
**Best for:** Founders and marketers running outbound campaigns
**Tech:** Google Sheets API, OpenAI GPT-4o-mini, SMTP
**Files:** `sheets-email-campaign/`

#### 5. Human-in-the-Loop AI Email Responder
**Category:** Support
**Price:** $19
**What it does:** AI drafts email responses, sends to you for approval, then sends when you say "SEND"
**Best for:** Support teams, founders who want AI help but won't let it send unsupervised
**Tech:** IMAP, SMTP, OpenAI GPT-4o-mini
**Files:** `human-in-loop-email/`

---

## Coming Soon

| Workflow | Category | Price | Status |
|----------|----------|-------|--------|
| SSL Certificate Monitor | IT Ops | $15 | Planned |
| AI Security Digest | IT Ops | $15 | Planned |
| Discord AI Bot | Support | $15 | Planned |
| RAG Document Chatbot | AI | $25 | Planned |
| YouTube Video Summarizer | Marketing | $15 | Planned |
| Lead Gen from Google Maps | Sales | $25 | Planned |
| Salesforce Sheet Sync | Sales | $19 | Planned |

---

## Every FlowKit Includes

- ✅ `workflow.py` — Production-ready Python code
- ✅ `README.md` — Setup guide, usage examples, configuration
- ✅ `AGENTS.md` — Operating manual for your AI agent (Claude, Cursor, Copilot) to run, monitor, fix, and extend the workflow autonomously
- ✅ Error handling with retry logic
- ✅ Graceful degradation (fails safe, not loud)
- ✅ Zero external dependencies beyond what's necessary
- ✅ Designed for AI-agent operation — your agent is the host, not a server

## License
Each workflow is licensed for single-user use. Team and enterprise licenses available.
