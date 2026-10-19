# Claude Desktop & Claude Code Weekly Update
**Week of October 13–19, 2026**

---

## New Features Shipped

### Claude Desktop

- **Dashboards (beta, Oct 8):** New Dashboards feature lets paid plan users generate live dashboards from business data using plain-language prompts.
- **Motion (beta, Oct 8):** Available for Team and Enterprise plans, Motion converts text and charts into editable animated explainers exportable as MP4.
- **Docs, Slides, and Design out of beta:** All three tools are now available on every plan including Free.
- **Google Workspace add-on (public beta, Oct 6):** Claude gained Docs, Sheets, and Slides connectors, enabling creation and editing of Google Workspace files directly. Claude can also build slides from a deck's existing layouts and themes.
- **Cowork moved to cloud (Oct 6):** New Cowork tasks on Pro and Max plans now run in the cloud by default. The "Only on your computer" toggle was removed; existing local tasks remain on-device.
- **Bundled Claude Code 2.1.299 (Oct 15):** Latest Desktop release bundles Claude Code v2.1.299 and deprecates several older managed-configuration keys.

### Claude Code

- **v2.1.301 (mid-October):** 51+ changes including enhanced OpenTelemetry support with cache-token fields, binary file detection fixes, Vim bracket-matching navigation, and VS Code math rendering improvements.
- **v2.1.302:** Adds client-side auto mode model selection, idle compaction controls, and faster startup with many plugins installed.
- **v2.1.296:** Introduced a setting to pin every subagent in a workflow to a single model, plus per-subagent context-window controls.
- **Auto mode server-side:** Auto mode now runs server-side by default; auto mode calls no longer count against usage limits.
- **Retry watchdog:** New `retry-watchdog` usage-limit setting added.
- **Claude Mods plugin system:** Community roundups highlight Claude Mods, a plugin system that hooks into Claude's behavior at tool call and prompt boundaries.

### Models

- **Haiku 5.5** released Oct 7
- **Sonnet 5.5** released Sep 28 (last week, still fresh)

---

## Announced but Not Yet Released

- No confirmed "announced but not yet shipped" items surfaced in this week's search. Community timelines mention potential Opus 5.5 and Opus 5 milestones, but dates were inconsistent across sources — treat those as unconfirmed.

---

## Community Buzz & Interesting Use Cases

- **Claude Mods gaining traction:** Developers are experimenting with plugin hooks for custom pre/post-processing of tool calls, enabling tighter integration with internal toolchains.
- **Motion demos:** Early users of Claude Motion are sharing animated explainers generated from static charts and bullet points, particularly for exec-facing presentations.
- **Cowork cloud migration:** Community discussion is active around the shift to cloud-only Cowork tasks — some power users are testing edge cases around long-running local tasks that predate the Oct 6 cutover.
- **Google Workspace integration:** The public beta Google Workspace add-on is drawing attention from teams that previously relied on Zapier-style glue scripts to get Claude output into Docs/Sheets.

---

## Sources

- [Claude Code Changelog – Claude Code Docs](https://code.claude.com/docs/en/changelog)
- [Claude Code v2.1.301 Major Updates – Classmethod](https://dev.classmethod.jp/en/articles/20261016-cc-updates-v2-1-301/)
- [Claude Code Changelog – agentgid](https://agentgid.com/agents/claude-code/changelog/)
- [Claude Code Changelog – gradually.ai](https://www.gradually.ai/en/changelogs/claude-code/)
- [Claude Updates – Releasebot](https://releasebot.io/updates/anthropic/claude)
- [Claude Code Updates – Releasebot](https://releasebot.io/updates/anthropic/claude-code)
- [What Are the New Features of Claude? October 2026 – Oxford AI School](https://www.theoxfordaischool.com/new-features-of-claude)
- [Use Claude Cowork on web, desktop, and mobile – Anthropic Support](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)
- [Claude New Features Oct 2026 – memoryplugin blog](https://blog.memoryplugin.com/claude-new-features-october-2026/)
- [Claude Code Cheat Sheet, October 2026 – DEV Community](https://dev.to/anglo_lima/claude-code-cheat-sheet-october-2026-the-complete-state-of-play-1j26)
