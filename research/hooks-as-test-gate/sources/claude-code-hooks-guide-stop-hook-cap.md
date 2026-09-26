---
source: https://code.claude.com/docs/en/hooks-guide
source_date: undated
researched: 2026-09-26
---

# Claude Code hooks guide: Limitations, permission modes and the Stop block cap

Fetched as raw page text (not through a summarising tool) on 2026-09-26; a summarising fetch of the reference page returned a wrong Stop schema, so only raw text is recorded here. Companion to the reference note in this folder; complements (does not redo) research/testing-feedback-loop/sources/claude-code-hooks-as-test-gates.md.

- Troubleshooting entry "Stop hook hits the block cap": "Claude Code overrides a Stop hook after it blocks eight times in a row without progress. Your hook script needs to check whether it already triggered a continuation. Parse the stop_hook_active field from the JSON input and exit early if it's true", with a bash example (`jq -r '.stop_hook_active'`, then `exit 0`). "If your hook legitimately needs more than eight iterations to converge, raise the cap with CLAUDE_CODE_STOP_HOOK_BLOCK_CAP." Note the tension: exiting 0 whenever stop_hook_active is true means the hook only ever forces one extra turn; the cap alone bounds the loop otherwise. The page does not say which to prefer for a test gate.
- Limitations: command hooks communicate through stdout, stderr and exit codes only; PostToolUse cannot undo actions; Stop hooks "fire whenever Claude finishes responding, not only at task completion. They don't fire on user interrupts."
- Permission modes: "PreToolUse hooks fire before any permission-mode check, in every permission mode, including dontAsk. A hook that returns permissionDecision: \"deny\" blocks the tool even in bypassPermissions mode or with --dangerously-skip-permissions." Hooks can tighten but not loosen permission rules.
- Multiple hooks on one event run in parallel.
- Prompt-based Stop hook: type "prompt" returns `{"ok": false, "reason": "..."}` and the reason is fed back so Claude keeps working, unless the response sets "impossible": true (then the stop is allowed). Default model Haiku, 30 s timeout. This is a model judgement, not a deterministic test run.
- Hooks in shell-form command run via `sh -c` (Git Bash/PowerShell on Windows); profile output that prepends text to stdout makes JSON unparseable and, on exit 0, is silent.
- Config sharing: project hooks live in .claude/settings.json and can be committed.

Unverified: the guide has no worked example of a test-running Stop or commit-gating PreToolUse hook; those designs are not stated by the page.
