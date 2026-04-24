# AI Landing Page Analyzer
# Feed it a URL. Get a full CRO audit with actionable fixes.

## What It Does
Analyzes any landing page using GPT-4 and returns a structured report: what's working, what's broken, quick wins ranked by impact, missing elements, and copy suggestions.

## Why This Beats the n8n Version
- **No server required** — runs from terminal, one command
- **Zero dependencies** — pure Python (no BeautifulSoup needed)
- **Better analysis** — structured CRO framework, not just "here are some tips"
- **Retry + timeout handling** — won't hang on slow pages
- **Save to file** — outputs markdown reports you can share

## Setup

```bash
export OPENAI_API_KEY="sk-..."
pip install requests openai
```

## Usage

```bash
# Analyze any URL
python workflow.py https://example.com

# Save report to file
python workflow.py https://example.com > report.md

# Use as a library
python -c "from workflow import analyze; print(analyze('https://example.com'))"
```

## What You Get
- Overall impression with scores (X/10)
- Specific strengths with quotes from the page
- Specific problems with suggested fixes
- Quick wins ranked by estimated impact (% improvement)
- Missing elements checklist (social proof, CTA, trust signals)
- Copy suggestions (headline/value prop rewrites)

## Integration Ideas
- Run as a cron job to monitor competitor landing pages weekly
- Hook into CI/CD to audit landing pages before deploy
- Batch analyze multiple URLs for client audits
- Add to Slack bot for team requests

## Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | env var | Your OpenAI API key |
| Max content length | 8000 chars | Truncated for token limits |

## Requirements
- Python 3.10+
- `requests`, `openai` packages
- OpenAI API key (GPT-4 recommended for quality analysis)
