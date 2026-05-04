#!/usr/bin/env python3
"""
Generates a weekly Claude Desktop & Claude Code update summary using the
Anthropic API with built-in web search, then saves a dated markdown file.

Run directly or via the GitHub Actions weekly-updates.yml workflow.
Requires: ANTHROPIC_API_KEY environment variable, `pip install anthropic`.
"""
import os
import sys
from datetime import date, timedelta
from pathlib import Path

import anthropic


def main() -> None:
    today = date.today()
    week_ago = today - timedelta(days=7)
    date_str = today.strftime("%Y-%m-%d")
    today_long = today.strftime("%B %-d, %Y")
    week_ago_short = week_ago.strftime("%B %-d")
    today_short = today.strftime("%B %-d, %Y")

    repo_root = Path(__file__).resolve().parent.parent
    output_path = repo_root / "weekly-updates" / f"{date_str}.md"

    if output_path.exists():
        print(f"Weekly update for {date_str} already exists, skipping.")
        sys.exit(0)

    client = anthropic.Anthropic()

    prompt = f"""Today is {date_str}. Search the web for the latest Claude Desktop and \
Claude Code updates, new features, and announcements from the past 7 days \
(covering {week_ago.strftime('%Y-%m-%d')} to {date_str}).

Write a clear, concise markdown summary. Use exactly this structure:

# Claude Weekly Update — {today_long}

_Covering: {week_ago_short}–{today_short}_

---

## Shipped This Week

[One subsection per notable feature/change, with a short paragraph each.]

---

## Announced / In Preview — Not Yet Fully Released

| Feature | Status | What It Is |
|---|---|---|
[rows]

---

## Community Buzz

[2-4 short paragraphs on community reaction, interesting use cases, debates.]

---

## Sources
- [Title](URL)

Rules:
- Use ## headings per feature/topic under "Shipped This Week"
- Keep each section tight — no fluff
- List every referenced URL in Sources
- Do not wrap the output in a code block"""

    print(f"Searching and generating update for week ending {date_str}...")

    response = client.messages.create(
        model="claude-opus-4-7",
        max_tokens=4096,
        tools=[{
            "type": "web_search_20250305",
            "name": "web_search",
            "max_uses": 12,
        }],
        messages=[{"role": "user", "content": prompt}],
    )

    text_blocks = [b.text for b in response.content if b.type == "text"]
    if not text_blocks:
        print("ERROR: No text content in response.", file=sys.stderr)
        sys.exit(1)

    content = "\n".join(text_blocks).strip()

    output_path.write_text(content + "\n", encoding="utf-8")
    print(f"Wrote {output_path}")


if __name__ == "__main__":
    main()
