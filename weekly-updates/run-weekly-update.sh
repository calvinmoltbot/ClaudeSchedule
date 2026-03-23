#!/usr/bin/env bash
# weekly-update.sh
# Run this every Monday at 8am via cron:
#   0 8 * * 1 /path/to/ClaudeSchedule/weekly-updates/run-weekly-update.sh
#
# Requires: claude (Claude Code CLI), git, ANTHROPIC_API_KEY in environment.

set -euo pipefail

REPO_DIR="$(cd "$(dirname "$0")/.." && pwd)"
DATE="$(date +%Y-%m-%d)"
OUTPUT="$REPO_DIR/weekly-updates/$DATE.md"

cd "$REPO_DIR"

claude --bare -p "
Search the web for the latest Claude Desktop and Claude Code updates, new features,
and announcements from the past 7 days (week ending $DATE).

Write a clear, concise markdown summary covering:
- New features or changes shipped
- Anything announced but not yet released
- Community buzz or interesting use cases spotted

Save the summary to: $OUTPUT

Use this exact format for the file header:
# Claude Weekly Update — $DATE

> Covering the week of $(date -d '7 days ago' +%Y-%m-%d)–$DATE

Then commit and push it:
  git add weekly-updates/$DATE.md
  git commit -m 'weekly update: $DATE'
  git push -u origin master
" --settings "$REPO_DIR/.claude/settings.json" 2>/dev/null || true
