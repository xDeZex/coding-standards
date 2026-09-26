---
source: https://cursor.com/docs/agent/hooks
source_date: undated
researched: 2026-09-26
---

# Cursor hooks (stop hook with followup_message, beforeShellExecution)

Re-read pass 2026-09-26: page (the URL redirects to https://cursor.com/docs/hooks) downloaded with curl as HTML and converted to text; the whole hooks page was searched and the exit-code, stop, matcher, configuration, cloud-agent and loop_limit sections read in full. No summarising tool. First-party vendor docs; page is long and changes with releases.

- Hooks are "spawned processes that communicate over stdio using JSON in both directions", defined in hooks.json at <project>/.cursor/hooks.json (committable, run from project root), ~/.cursor/hooks.json (user), or enterprise paths (/etc/cursor/hooks.json on Linux, /Library/Application Support/Cursor/hooks.json on macOS, C:\ProgramData\Cursor\hooks.json on Windows). All matching hooks from every source run and responses merge; "any deny wins over ask, and ask wins over allow". Cloud agents: "Cloud agents run command-based hooks from your repository" (.cursor/hooks.json at the project root); on Enterprise plans they also run team and enterprise-managed hooks; prompt-based hooks are not available there; "Hooks do not run during" the read-only early exploratory turns of a cloud agent. The page does not say user-level hooks are unavailable in cloud agents (an earlier version of this note claimed it; not supported by the page). Priority order is Enterprise, Team, Project, User.
- Relevant events: beforeShellExecution / afterShellExecution, preToolUse / postToolUse / postToolUseFailure, subagentStart / subagentStop, afterFileEdit, and `stop` ("Handle agent completion").
- Exit codes: 0 = use the JSON output; for permission hooks (beforeShellExecution, beforeMCPExecution, beforeReadFile, subagentStart, preToolUse and others) invalid JSON or a schema mismatch blocks the action. "Exit code 2 - Block the action (equivalent to returning permission: \"deny\")". "Other exit codes - Hook failed, action proceeds (fail-open by default)." Option `failClosed` (default false) makes crashes, timeouts and non-zero exits block instead.
- beforeShellExecution matcher runs "against the shell command string" (regex-like, e.g. "curl|wget|nc"), so a matcher on "git commit" is possible; the page gives no git-commit example (our inference).
- stop hook: input `{"status": "completed"|"aborted"|"error", "loop_count": 0}`; output `{"followup_message": "<text>"}`. "When provided and non-empty, Cursor will automatically submit it as the next user message. This enables loop-style flows (e.g., iterate until a goal is met)." Note the mechanism is a follow-up message, not exit 2. Loop guard: `loop_count` counts prior automatic follow-ups; "The default limit is 5 auto follow-ups per script, configurable via the loop_limit option. Set loop_limit to null to remove the cap." The same applies to subagentStop. Table says default is null for hooks loaded from Claude Code configuration.
- Config fields include `command`, `type` ("command" or "prompt"), `timeout` (seconds, "platform default"), `matcher`, `loop_limit`, `failClosed`.
- Cursor can also load hooks from other tools' config: the page says "See Third Party Hooks for details" but that link redirects back to this same page, so the compatibility rules were not readable. The loop_limit row refers to "Claude Code hooks".

Also on the page: a `beforeShellExecution` example hooks.json wires a `block-git.sh` script (its body is not shown); for subagentStop the followup_message is "Only consumed when status is 'completed'" (the stop hook's section does not say this). Cursor's doc says exit code 2 "matches Claude Code behavior for compatibility".

Unverified: the default timeout value ("platform default" is all the page says); which Claude Code config Cursor imports.
