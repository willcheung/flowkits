# FlowKits Workflow: AI Landing Page Analyzer
# Category: Marketing
# Original inspiration: n8n workflow #3100
# Price: FREE (lead magnet)

import os
import json
import logging
from dataclasses import dataclass
from typing import Optional

import requests
from openai import OpenAI

# --- Configuration ---
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
USER_AGENT = "FlowKits-LandingPageAnalyzer/1.0"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("landing-page-analyzer")

SYSTEM_PROMPT = """You are a senior conversion rate optimization (CRO) expert and UX analyst. 
Analyze the provided landing page content and give actionable, specific feedback.

Structure your response as:
## Overall Impression
One paragraph summary.

## What's Working (Score: X/10)
List specific strengths with quotes from the page.

## What Needs Fixing (Score: X/10)  
List specific problems with suggested fixes. Be brutal but fair.

## Quick Wins (Priority Order)
Numbered list of changes that would have the biggest impact, estimated as % improvement each.

## Missing Elements
Critical things the page is missing (social proof, CTA, trust signals, etc.)

## Copy Suggestions
Specific headline/value prop rewrites if the current ones are weak.

Keep it actionable. No fluff. A developer should be able to implement your suggestions today."""

USER_PROMPT_TEMPLATE = """Analyze this landing page for conversion optimization:

URL: {url}
Title: {title}
Meta Description: {meta_description}
H1: {h1}
Word Count: {word_count} words
Links: {link_count}
Images: {image_count}

### Page Content (cleaned text):
{content}

### All Headings Found:
{headings}

Give me a full CRO audit with specific, actionable recommendations."""


@dataclass
class PageContent:
    url: str
    title: str
    meta_description: str
    h1: str
    headings: list[str]
    content: str
    word_count: int
    link_count: int
    image_count: int
    status_code: int


@dataclass
class AnalysisResult:
    url: str
    overall_score: str
    quick_wins: list[str]
    full_report: str
    raw_response: str


class LandingPageAnalyzer:
    """AI-powered landing page analyzer with retry and error handling."""

    def __init__(self):
        self.openai = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": USER_AGENT})

    def fetch_page(self, url: str, timeout: int = 15) -> Optional[PageContent]:
        """Fetch and parse a landing page. Returns None on failure."""
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()

            # Simple HTML parsing (no BeautifulSoup dependency)
            html = response.text

            # Extract title
            title = self._extract_tag(html, "title") or ""

            # Extract meta description
            meta_desc = self._extract_meta(html, "description") or ""

            # Extract H1
            h1 = self._extract_tag(html, "h1") or ""

            # Extract all headings
            headings = []
            for tag in ["h1", "h2", "h3"]:
                matches = self._extract_all_tags(html, tag)
                headings.extend(matches)

            # Extract visible text content
            content = self._extract_text(html)

            # Count links and images
            link_count = html.lower().count("<a ")
            image_count = html.lower().count("<img ")

            return PageContent(
                url=url,
                title=title,
                meta_description=meta_desc,
                h1=h1,
                headings=headings,
                content=content[:8000],  # Truncate for token limits
                word_count=len(content.split()),
                link_count=link_count,
                image_count=image_count,
                status_code=response.status_code,
            )

        except requests.exceptions.Timeout:
            logger.error(f"Timeout fetching {url}")
            return None
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch {url}: {e}")
            return None

    def analyze(self, page: PageContent) -> Optional[AnalysisResult]:
        """Send page content to OpenAI for analysis."""
        if not self.openai:
            logger.error("OpenAI API key not set")
            return None

        prompt = USER_PROMPT_TEMPLATE.format(
            url=page.url,
            title=page.title,
            meta_description=page.meta_description,
            h1=page.h1,
            word_count=page.word_count,
            link_count=page.link_count,
            image_count=page.image_count,
            content=page.content,
            headings="\n".join(f"- {h}" for h in page.headings),
        )

        try:
            response = self.openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.3,
                max_tokens=2000,
            )
            report = response.choices[0].message.content

            # Parse quick wins from the report
            quick_wins = []
            for line in report.split("\n"):
                if line.strip().startswith(("1.", "2.", "3.", "4.", "5.")):
                    quick_wins.append(line.strip())

            return AnalysisResult(
                url=page.url,
                overall_score="see report",
                quick_wins=quick_wins,
                full_report=report,
                raw_response=report,
            )

        except Exception as e:
            logger.error(f"OpenAI analysis failed: {e}")
            return None

    def analyze_url(self, url: str) -> Optional[AnalysisResult]:
        """One-shot: fetch + analyze a URL."""
        logger.info(f"Analyzing: {url}")
        page = self.fetch_page(url)
        if not page:
            return None

        logger.info(f"  Fetched: {page.word_count} words, {page.link_count} links")
        result = self.analyze(page)
        if result:
            logger.info(f"  Analysis complete. {len(result.quick_wins)} quick wins found.")
        return result

    # --- HTML Parsing Helpers (no external dependencies) ---

    def _extract_tag(self, html: str, tag: str) -> Optional[str]:
        """Extract text content of the first occurrence of an HTML tag."""
        import re
        pattern = rf"<{tag}[^>]*>(.*?)</{tag}>"
        match = re.search(pattern, html, re.DOTALL | re.IGNORECASE)
        if match:
            return self._strip_html(match.group(1))
        return None

    def _extract_all_tags(self, html: str, tag: str) -> list[str]:
        """Extract text content of all occurrences of an HTML tag."""
        import re
        pattern = rf"<{tag}[^>]*>(.*?)</{tag}>"
        matches = re.findall(pattern, html, re.DOTALL | re.IGNORECASE)
        return [self._strip_html(m).strip() for m in matches if self._strip_html(m).strip()]

    def _extract_meta(self, html: str, name: str) -> Optional[str]:
        """Extract a meta tag's content."""
        import re
        pattern = rf'<meta[^>]*name=["\']{name}["\'][^>]*content=["\']([^"\']*)["\']'
        match = re.search(pattern, html, re.IGNORECASE)
        if match:
            return match.group(1)
        # Try reversed attribute order
        pattern = rf'<meta[^>]*content=["\']([^"\']*)["\'][^>]*name=["\']{name}["\']'
        match = re.search(pattern, html, re.IGNORECASE)
        return match.group(1) if match else None

    def _extract_text(self, html: str) -> str:
        """Extract visible text from HTML, removing scripts, styles, and tags."""
        import re
        # Remove script and style blocks
        html = re.sub(r"<(script|style)[^>]*>.*?</\1>", "", html, flags=re.DOTALL | re.IGNORECASE)
        # Remove HTML tags
        text = re.sub(r"<[^>]+>", " ", html)
        # Clean up whitespace
        text = re.sub(r"\s+", " ", text)
        # Remove HTML entities
        text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
        text = text.replace("&quot;", '"').replace("&#39;", "'").replace("&nbsp;", " ")
        return text.strip()


def analyze(url: str, output_file: Optional[str] = None) -> Optional[str]:
    """Convenience function: analyze a URL and optionally save to file."""
    analyzer = LandingPageAnalyzer()
    result = analyzer.analyze_url(url)
    if result:
        report = f"# Landing Page Analysis: {url}\n\n{result.full_report}"
        if output_file:
            os.makedirs(os.path.dirname(output_file) or ".", exist_ok=True)
            with open(output_file, "w") as f:
                f.write(report)
            logger.info(f"Report saved to {output_file}")
        return report
    return None


if __name__ == "__main__":
    import sys
    url = sys.argv[1] if len(sys.argv) > 1 else "https://flowkits.ai"
    report = analyze(url)
    if report:
        print(report)
    else:
        print(f"Failed to analyze {url}")
