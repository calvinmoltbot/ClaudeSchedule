"""
Weekly Claude update generator.
Searches for the latest Claude Desktop and Claude Code news,
then uses claude-sonnet to write a clean markdown summary.
"""

import os
import datetime
import pathlib
import anthropic


SEARCH_QUERIES = [
    "Claude Code new features updates this week",
    "Claude Desktop new features updates this week",
    "Anthropic Claude announcements release notes this week",
    "Claude Code Claude Desktop community use cases this week",
]

SYSTEM_PROMPT = """\
You are a technical writer producing a weekly update digest for developers who
use Claude Desktop and Claude Code. Be concise, accurate, and use markdown.
Separate clearly: (1) shipped features, (2) announced-but-not-released items,
(3) community buzz. Cite sources inline as markdown links where available.
Always open with the date range covered.\
"""


def run_web_search(client: anthropic.Anthropic, query: str) -> str:
    """Run a single web search via the Claude API with web_search tool."""
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=[{"type": "web_search_20250305", "name": "web_search"}],
        messages=[{"role": "user", "content": query}],
    )
    # Collect all text blocks from the response
    parts = []
    for block in response.content:
        if hasattr(block, "text"):
            parts.append(block.text)
    return "\n".join(parts)


def generate_summary(client: anthropic.Anthropic, raw_results: str, date_range: str) -> str:
    """Ask Claude to synthesise raw search results into a weekly digest."""
    prompt = (
        f"Date range: {date_range}\n\n"
        "Below are raw search results gathered this morning. "
        "Write the weekly Claude update digest based on these.\n\n"
        f"{raw_results}"
    )
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=4096,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
        # Enable prompt caching on the (potentially long) system prompt
        extra_headers={"anthropic-beta": "prompt-caching-2024-07-31"},
    )
    return response.content[0].text


def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise RuntimeError("ANTHROPIC_API_KEY environment variable is not set")

    client = anthropic.Anthropic(api_key=api_key)

    today = datetime.date.today()
    week_start = today - datetime.timedelta(days=6)
    date_range = f"{week_start.strftime('%B %-d')} – {today.strftime('%B %-d, %Y')}"

    # Gather search results
    all_results = []
    for query in SEARCH_QUERIES:
        print(f"Searching: {query}")
        result = run_web_search(client, query)
        all_results.append(f"### Query: {query}\n\n{result}")

    raw = "\n\n---\n\n".join(all_results)

    # Synthesise into a markdown digest
    print("Generating summary…")
    summary = generate_summary(client, raw, date_range)

    # Prepend a standard header
    filename_date = today.strftime("%Y-%m-%d")
    header = f"# Claude Weekly Update — {today.strftime('%B %-d, %Y')}\n\n> Covering **{date_range}** | Claude Code & Claude Desktop\n\n---\n\n"
    content = header + summary

    # Write file
    output_path = pathlib.Path("weekly-updates") / f"{filename_date}.md"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(f"Saved: {output_path}")


if __name__ == "__main__":
    main()
