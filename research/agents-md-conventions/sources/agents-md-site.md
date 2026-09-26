---
source: https://agents.md
source_date: undated
researched: 2026-09-26
---

# AGENTS.md site (agents.md)

Source line as first recorded: https://agents.md (site). Source date: undated. Researched: 2026-09-26.

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere.

- Format: "a simple, open format for guiding coding agents"; standard Markdown, no required fields; "use any headings you like; the agent simply parses the text you provide." Common sections listed: project overview, build/test commands, code style, security.
- Purpose: "a dedicated, predictable place to provide the context and instructions"; README is "for humans", AGENTS.md is for agents.
- Nesting/precedence: for monorepos, "place another AGENTS.md inside each package. Agents automatically read the nearest file in the directory tree, so the closest one takes precedence." Also: explicit user chat prompts override everything.
- Size: the site gives no size limit or recommendation (as fetched). Unverified whether one exists elsewhere on the site.
- Adoption claims: "over 25 agents" support it (Codex, Jules, Cursor, Copilot, VS Code, Devin, Aider, Zed, Warp) and "over 60k open-source projects" use it. These are the site's own claims, not independently verified.
- FAQ: agents will try to run test commands listed; file is "living documentation"; legacy migration via symbolic links; example config for Aider and Gemini CLI.
