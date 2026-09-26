---
source: https://opencode.ai/docs/plugins/
source_date: 2026-09-26
researched: 2026-09-26
---

# OpenCode plugins: in-process hooks

Read as raw page text (curl and html.parser). The page shows "Last updated: Sep 26, 2026". Only the parts named were read; the full event list is partly summarised.

- OpenCode's hook mechanism is a plugin: a JavaScript or TypeScript module in `.opencode/plugins/` or `~/.config/opencode/plugins/`, or an npm package listed in `opencode.json`, exporting a function that returns an object of hook implementations. Plugins are "loaded from all sources and all hooks run in sequence", and local and npm plugins install dependencies with Bun at startup.
- Hook points include `tool.execute.before`, `tool.execute.after`, `shell.env`, plus events for commands, files (`file.edited`), LSP diagnostics, messages, permissions, sessions (`session.idle`, `session.compacted`, `session.error`), and others.
- Examples on the page: a `session.idle` handler sending a desktop notification through `osascript`; an "`.env` protection" plugin whose `tool.execute.before` throws an Error when the tool is `read` and the path includes `.env` ("Do not read .env files"); an env-injection plugin using `shell.env`.
- Difference from the command-hook harnesses: the hook is code running inside the harness process with a client handle (`client`) and a shell helper (`$`), not a separate process reading JSON over stdin. The page does not describe timeouts, fail-open behaviour or trust prompts.
