---
source: https://developers.openai.com/codex/hooks
source_date: undated
researched: 2026-09-26
---

# OpenAI Codex hooks (lifecycle hooks with Stop and PreToolUse)

Fetched as raw page text (not through a summarising tool) on 2026-09-26. The URL redirects (HTTP 308) to https://learn.chatgpt.com/docs/hooks, the same host the existing Codex AGENTS.md note records, so the canonical link is unstable; link the developers.openai.com path and expect a redirect. First-party vendor docs.

- Codex has hooks, on by default: "Hooks are enabled by default"; feature key `hooks` (older `codex_hooks` still works); can be turned off in config.toml or by requirements.toml. Non-managed hooks "must be reviewed and trusted before they run"; project-local hooks load only when the project .codex/ layer is trusted.
- Events during a turn: PreToolUse, PermissionRequest, PostToolUse, PreCompact, PostCompact, UserPromptSubmit, SubagentStop, Stop; also Interrupt, SessionStart, SubagentStart, SessionEnd.
- Locations: ~/.codex/hooks.json, ~/.codex/config.toml, <repo>/.codex/hooks.json, <repo>/.codex/config.toml (inline [hooks] tables), plus plugin-bundled hooks/hooks.json. All matching hooks load; higher layers do not replace lower ones.
- Timeout: "timeout is in seconds. If timeout is omitted, Codex uses 600 seconds for most hooks." Interrupt hooks default to 1 s, configurable 1 to 3 s. Async command handlers are supported.
- Stop: matcher not used. Input has `stop_hook_active` ("Whether this turn was already continued by Stop"), `turn_id`, `last_assistant_message`. "Stop expects JSON on stdout when it exits 0. Plain text output is invalid." To keep going return `{"decision": "block", "reason": "Run one more pass over the failing tests."}`; "You can also use exit code 2 and write the continuation reason to stderr." "decision: block doesn't reject the turn. Instead, it tells Codex to continue and automatically creates a new continuation prompt that acts as a new user prompt, using your reason as that prompt text." If any matching Stop hook returns `continue: false` it takes precedence over continuation decisions.
- PreToolUse: matcher on tool name; covers Bash (shell and unified exec), apply_patch (matcher aliases Edit, Write) and MCP tools. To deny: `hookSpecificOutput.permissionDecision: "deny"` with a reason, an older `decision: "block"` shape, or exit code 2 with stderr. PostToolUse cannot undo a completed command. To gate a commit one would match Bash and inspect tool_input.command (our inference; no git-commit recipe on the page).
- No loop cap like Claude Code's 8 was found in the sections read (only the stop_hook_active field).
- notify (separate, older mechanism) in https://developers.openai.com/codex/config-advanced : `notify = ["python3", "/path/to/notify.py"]` runs an external program on "supported events (currently only agent-turn-complete)", passing one JSON argument; it is for notifications ("desktop toasts, chat webhooks, CI updates") and the page describes no way for it to block or continue a turn.

Unverified: whether a Stop-hook loop cap exists in Codex (not stated in the text read); the schemas on the page note "linked main branch schemas may include hook fields that are not in the current release", so behaviour is release-specific.
