---
source: https://code.claude.com/docs/en/hooks
source_date: undated
researched: 2026-09-26
---

# Claude Code hooks reference: Stop, SubagentStop, PreToolUse, exit codes, timeouts

Fetched as raw page text (not through a summarising tool) on 2026-09-26; a summarising fetch of the reference page returned a wrong Stop schema, so only raw text is recorded here. Vendor first-party docs; the page is very large and versioned in text (v2.1.x), so specifics drift. Link to it rather than copy. Anchors used by the page: #stop, #subagentstop, #pretooluse, #exit-code-2-behavior-per-event, #timeouts, #bash-if-matching.

- Exit codes: "Exit 2 means a blocking error. On events that can block, exit 2 blocks whether or not you print JSON: even a JSON permissionDecision of \"allow\" can't override it." Blocking message is the JSON reason if given, else stderr.
- Warning in the page: "For most hook events, exit code 2 is the only exit code that blocks through the code alone. Without valid JSON on stdout, Claude Code treats exit code 1 as a non-blocking error and proceeds with the action, even though 1 is the conventional Unix failure code. If your hook is meant to enforce a policy, use exit 2." So a script that runs `npm test` and passes its status through with exit 1 does not gate.
- Per-event exit 2: PreToolUse blocks the tool call; Stop "Prevents Claude from stopping, continues the conversation"; SubagentStop "Prevents the subagent from stopping"; PostToolUse cannot block (tool already ran; stderr shown to Claude); TaskCompleted blocks completion; StopFailure ignored.
- Stop input: common fields plus `stop_hook_active`, `last_assistant_message`, `background_tasks`, `session_crons`. "The stop_hook_active field is true when Claude Code is already continuing as a result of a stop hook. Check this value or process the transcript to avoid blocking on a condition that will never resolve."
- Loop cap: "Claude Code applies an 8-consecutive-continuation cap: after stop hooks have continued the turn eight times in a row, Claude Code overrides the next block and ends the turn. To raise the cap, set CLAUDE_CODE_STOP_HOOK_BLOCK_CAP."
- Stop decision control (JSON on exit 0): `{"decision": "block", "reason": "..."}`; "block prevents Claude from stopping. Omit to allow Claude to stop"; `reason` required when blocking. Alternative: `hookSpecificOutput.additionalContext` (hookEventName "Stop") keeps the conversation going as non-error "Stop hook feedback", under the same stop_hook_active and 8-cap protections. Exit 2 with stderr routes the same as reason.
- SubagentStop uses the same decision format; block keeps the subagent running and delivers reason as its next instruction. Not every SubagentStop comes from a subagent Claude spawned (internal agents such as prompt suggestions and /btw also fire it; agent_type may then be empty).
- Stop fires on every finished response, not only at task completion; it does not fire on user interrupts; API errors fire StopFailure instead (hooks guide, Limitations).
- Timeouts: default 600 s for command, http, mcp_tool hooks (30 s on UserPromptSubmit, PreModelSwitch, PostModelSwitch; 10 s on MessageDisplay); prompt hooks 30 s; agent hooks 60 s; per-hook `timeout` field in seconds. On timeout the hook is cancelled and its output discarded, "so on most events a timed-out hook renders no decision". On PreToolUse a timed-out command hook "doesn't block the tool call ... so don't count on a stalled hook to act as a gate." (Agent SDK callback hooks differ: a timeout blocks.) Implication for tests: a slow suite that hits the timeout fails open on PreToolUse.
- Matching a git commit: two-level filter. `matcher` is on tool name (e.g. "Bash"); handler-level `if` uses permission-rule syntax such as "Bash(git *)", evaluated only on tool events (PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest, PermissionDenied). Table in the page: leading VAR=value assignments are stripped; each subcommand of `a && b` is checked; commands inside $() and backticks are checked; where the command name is a variable (`$TOOL git push`) the hook runs anyway. The page has no dedicated git-commit example; a "Bash(git commit *)" pattern is our inference from the syntax, not a documented recipe.
- Config locations: ~/.claude/settings.json (user), .claude/settings.json (project, committable), .claude/settings.local.json (gitignored), managed policy, plugin hooks/hooks.json, skill and subagent frontmatter. Hooks from all sources merge. "disableAllHooks": true disables user/project hooks (not managed hooks).
- Hook types: command, http, mcp_tool, prompt, agent.
- Events include PreToolUse, PostToolUse, Stop, SubagentStop, TaskCompleted, TeammateIdle, among many others (long list; changes between versions).

Unverified: no statement in this page about hooks and a non-interactive run beyond what the guide note records; behaviour when a tool is not Bash (e.g. an editor writing files) not examined.
