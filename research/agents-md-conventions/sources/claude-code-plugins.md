---
source: https://code.claude.com/docs/en/plugins
source_date: undated
researched: 2026-09-26
---

# Claude Code plugins overview

Source line as first recorded: https://code.claude.com/docs/en/plugins (plugin overview). Source date: undated. Researched: 2026-09-26.

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere.

- A plugin is "a directory of skills, agents, hooks, MCP servers, or other components that Claude Code installs and loads as one unit"; manifest at `.claude-plugin/plugin.json`. Distributed via a marketplace: a repo with `.claude-plugin/marketplace.json` listing plugins; installed by name (`plugin@marketplace`) at user, project or local scope.
- Stated trade-offs: an enabled plugin's skill/agent names and descriptions sit in context every turn (token cost); MCP servers and hooks run in every session; "what the plugin runs, it runs as you". Skills, subagents, hooks and MCP servers also work standalone without a plugin; the docs say to use a plugin when you want several packaged as one unit with versioned updates.
- The overview lists no component type for CLAUDE.md or AGENTS.md content (unverified beyond the page read; the components page was not fetched).
