---
source: https://code.claude.com/docs/en/hooks-guide
source_date: undated
researched: 2026-09-26
---

# Claude Code hooks guide: what to automate, limitations, troubleshooting

Read as raw page text (curl and html.parser, about 54 KB); the parts below were read directly. Not via WebFetch. Sibling notes from the earlier topic cover the Stop loop guard and block cap: [loop guard](../../hooks-as-test-gate/sources/claude-code-hooks-guide-stop-hook-loop-guard.md), [cap](../../hooks-as-test-gate/sources/claude-code-hooks-guide-stop-hook-cap.md).

- Uses the guide names: "format files after edits, block commands before they execute, send notifications when Claude needs input, inject context at session start". Worked examples on the page: a Notification hook (desktop notification when Claude needs input), PostToolUse `Edit|Write` running `npx prettier --write` on the edited path, a PreToolUse `Edit|Write` script that exits 2 when the path contains `.env`, `package-lock.json` or `.git/`, a SessionStart hook with a `compact` matcher that re-injects context after compaction (plain stdout is added to context), a ConfigChange audit hook, and CwdChanged/FileChanged environment reload.
- Format hook detail: the example passes the edited path from `jq` into Prettier; the page does not mention that a formatter can rewrite a file the agent has already read (see [issue 41797](claude-code-issue-41797-formatter-stale-read-docs.md)).
- Limitations section, verbatim points: "Command hooks communicate through stdout, stderr, and exit codes only. They can't trigger / commands or tool calls." "PostToolUse hooks can't undo actions since the tool has already executed." "Stop hooks fire whenever Claude finishes responding, not only at task completion. They don't fire on user interrupts." Default timeouts: 10 minutes for command, http and mcp_tool (30 seconds for UserPromptSubmit and two model-switch events, 10 seconds for MessageDisplay), 30 seconds for prompt, 60 seconds for agent; SessionEnd hooks share a 1.5-second budget.
- Non-interactive: with `-p` a PermissionRequest hook has no prompt to answer, so "use PreToolUse hooks for automated permission decisions instead". A background subagent that cannot prompt has its call denied if no hook returns a decision.
- Best-effort `if` filter: "Because the filter is best-effort, use the permission system rather than a hook to enforce a hard allow or deny." When Claude Code cannot tell which commands a Bash input runs, it runs the hook regardless of the pattern.
- Prompt-based hooks: "For decisions that require judgment rather than deterministic rules, use type: 'prompt' hooks", a single-turn call to a Claude model, Haiku by default, returning `ok` true or false. What `ok: false` does depends on the event (Stop continues the agent with the reason; PreToolUse denies and by default ends the turn; PostToolUse ends the turn unless `continueOnBlock`).
- Hooks are "not firing" troubleshooting: matchers are case-sensitive; check `/hooks`; if a settings edit does not show up, "the file watcher may have missed the change: restart your session".
- Where to put a hook: user settings (personal), project settings (shareable), local settings (gitignored), managed settings (organization-wide), plugins, skill or subagent frontmatter. `/hooks` is a read-only browser; "To add, modify, or remove hooks, edit your settings JSON directly or ask Claude to make the change."
- Hook run output is not in the transcript on success: the reference says "A successful hook's stdout is never shown in the transcript and is recorded in the debug log" (see the reference note), apart from stdout on SessionStart and UserPromptSubmit which is added to context.
