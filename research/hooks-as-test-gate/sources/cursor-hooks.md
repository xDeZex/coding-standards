---
source: https://cursor.com/docs/agent/hooks
source_date: undated
researched: 2026-09-26
---

# Cursor hooks (stop hook with followup_message, beforeShellExecution)

Fetched as raw page text (not through a summarising tool) on 2026-09-26. First-party vendor docs; page is long and changes with releases.

- Hooks are "spawned processes that communicate over stdio using JSON in both directions", defined in hooks.json at <project>/.cursor/hooks.json (committable, run from project root), ~/.cursor/hooks.json (user), or enterprise paths (/etc/cursor/hooks.json on Linux, /Library/Application Support/Cursor/hooks.json on macOS, C:\ProgramData\Cursor\hooks.json on Windows). All matching hooks from every source run and responses merge; "any deny wins over ask, and ask wins over allow". Cloud agents run project hooks; user-level hooks are not available in cloud agents.
- Relevant events: beforeShellExecution / afterShellExecution, preToolUse / postToolUse / postToolUseFailure, subagentStart / subagentStop, afterFileEdit, and `stop` ("Handle agent completion").
- Exit codes: 0 = use the JSON output; for permission hooks (beforeShellExecution, beforeMCPExecution, beforeReadFile, subagentStart, preToolUse and others) invalid JSON or a schema mismatch blocks the action. "Exit code 2 - Block the action (equivalent to returning permission: \"deny\")". "Other exit codes - Hook failed, action proceeds (fail-open by default)." Option `failClosed` (default false) makes crashes, timeouts and non-zero exits block instead.
- beforeShellExecution matcher runs "against the shell command string" (regex-like, e.g. "curl|wget|nc"), so a matcher on "git commit" is possible; the page gives no git-commit example (our inference).
- stop hook: input `{"status": "completed"|"aborted"|"error", "loop_count": 0}`; output `{"followup_message": "<text>"}`. "When provided and non-empty, Cursor will automatically submit it as the next user message. This enables loop-style flows (e.g., iterate until a goal is met)." Note the mechanism is a follow-up message, not exit 2. Loop guard: `loop_count` counts prior automatic follow-ups; "The default limit is 5 auto follow-ups per script, configurable via the loop_limit option. Set loop_limit to null to remove the cap." The same applies to subagentStop. Table says default is null for hooks loaded from Claude Code configuration.
- Config fields include `command`, `type` ("command" or "prompt"), `timeout` (seconds, "platform default"), `matcher`, `loop_limit`, `failClosed`.
- Cursor can also load hooks from other tools' config (the loop_limit row refers to "Claude Code hooks"); the extent was not read.

Unverified: the default timeout value ("platform default" is all the page says); which Claude Code config Cursor imports.
