# AI Landing Page Analyzer — AI Agent Context

## What This Is
A Python tool that fetches any landing page and uses GPT-4 to produce a full conversion rate optimization (CRO) audit. Returns actionable recommendations ranked by impact.

## Architecture
- `workflow.py` — Single-file tool. Entry point: `analyze(url)`
- `LandingPageAnalyzer` class handles fetching + analysis
- HTML parsing built-in (no BeautifulSoup dependency)
- Outputs markdown reports

## Key Functions
- `LandingPageAnalyzer.fetch_page(url)` — Fetches + parses HTML into structured data
- `LandingPageAnalyzer.analyze(page)` — Sends to OpenAI, returns structured report
- `LandingPageAnalyzer.analyze_url(url)` — One-shot convenience method
- `analyze(url, output_file)` — Module-level convenience function

## AI Enhancement Over n8n Original
1. Structured CRO framework (not just "here are some tips")
2. Scores for each section (X/10)
3. Quick wins ranked by estimated impact
4. Copy suggestions with actual rewrites
5. Zero external dependencies (no BeautifulSoup)
6. Save to file capability

## Setup Requirements
- `OPENAI_API_KEY` environment variable
- `pip install requests openai`

## How to Extend
- Add competitor comparison mode (analyze 2+ URLs side by side)
- Add historical tracking (save reports, diff over time)
- Hook into CI/CD pipeline
- Add batch mode for client audits
