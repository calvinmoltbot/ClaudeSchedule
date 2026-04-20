#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_DIR"

DATE=$(date +%Y-%m-%d)
OUTFILE="weekly-updates/${DATE}.md"

if [[ -f "$OUTFILE" ]]; then
  echo "Weekly update for ${DATE} already exists, skipping."
  exit 0
fi

PROMPT="Today is ${DATE}. Search the web for the latest Claude Desktop and Claude Code updates, new features, and announcements from the past 7 days. Write a clear, concise markdown summary covering:
- New features or changes shipped
- Anything announced but not yet released (previews, betas, roadmap items)
- Community buzz or interesting use cases spotted

Format: Use ## headings per feature/topic. Include a Sources section at the end with markdown links to all referenced URLs.

Save the summary as a file named ${OUTFILE} inside the repository at $(pwd). Then run: git add ${OUTFILE} && git commit -m 'weekly update: ${DATE}' && git push -u origin master"

claude --print "$PROMPT"
