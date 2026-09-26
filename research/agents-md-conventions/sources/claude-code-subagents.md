---
source: https://code.claude.com/docs/en/sub-agents
source_date: undated
researched: 2026-09-26
---

# Claude Code subagents

Source line as first recorded: https://code.claude.com/docs/en/sub-agents. Source date: undated. Researched: 2026-09-26.

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere.

- Markdown file with YAML frontmatter; only `name` and `description` required; body is the system prompt. Locations by priority: managed settings, `--agents` flag, `.claude/agents/`, `~/.claude/agents/`, plugin `agents/`.
- Non-fork subagents load the CLAUDE.md hierarchy (including AGENTS.md loaded as project instructions) unless `omitClaudeMd: true`; built-in Explore and Plan skip it.
- Plugin subagents ignore `hooks`, `mcpServers`, `permissionMode`.
