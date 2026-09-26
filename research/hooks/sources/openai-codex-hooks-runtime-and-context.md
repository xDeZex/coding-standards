---
source: https://developers.openai.com/codex/hooks
source_date: undated
researched: 2026-09-26
---

# OpenAI Codex hooks: trust review, tool coverage, context limits

Read as raw page text (curl and html.parser). Not via WebFetch. The extraction includes site navigation before the page body; only the Hooks body was used. The Stop, exit-code and timeout material is in the sibling note [openai-codex-hooks](../../hooks-as-test-gate/sources/openai-codex-hooks.md).

- Purposes listed: send chats to a logging or analytics engine, "Scan your team's prompts to block accidentally pasting API keys", summarise chats into persistent memories, "Run a custom validation check when a chat turn stops, enforcing standards", customise prompting in a directory.
- Runtime: matching hooks from multiple files all run; multiple matching command hooks for an event "are launched concurrently, so one hook can't prevent another matching hook from starting". Events during a turn: PreToolUse, PermissionRequest, PostToolUse, PreCompact, PostCompact, UserPromptSubmit, SubagentStop, Stop; plus SessionStart, SubagentStart, SessionEnd and Interrupt.
- Trust: "Non-managed hooks must be reviewed and trusted before they run." Codex records trust against the hook's hash, "so new or changed hooks are marked for review and skipped until trusted". Project-local hooks load only when the project `.codex/` layer is trusted. Managed hooks count as trusted by policy and cannot be disabled from the user hook browser; `--dangerously-bypass-hook-trust` runs enabled hooks without persisted trust for one invocation. Plugin-bundled hooks are skipped until reviewed. `allow_managed_hooks_only = true` skips user, project, session and plugin hooks. Hooks are on by default; `[features] hooks = false` turns them off.
- Coverage: PreToolUse and PostToolUse observe shell commands, unified exec, `apply_patch` (matched as apply_patch, Edit or Write), MCP tools and other local function tools; hosted tools such as WebSearch do not use the hook path ("No" for both). `write_stdin` does not re-run PreToolUse for input sent to a command that already passed. "Some specialized tool paths can opt out of the default hook path. Treat tool hooks as a useful guardrail, not a complete enforcement boundary."
- Context injection: `additionalContext` from SessionStart, UserPromptSubmit, PreToolUse and PostToolUse is "added as extra developer context". Default threshold 2,500 tokens per handler; larger output "spills" to a file under a temp `hook_outputs` directory with a head-and-tail preview. `additionalContextLimit` can raise it; the page warns "Context from multiple hooks and plugins adds up and can degrade model performance", and "avoid returning secrets or other sensitive data in hook output" because oversized output is written to disk. No measurement is given for the degradation.
- Errors: plain text on stdout is ignored for most events; unsupported fields returned by a PreToolUse hook make Codex mark the run failed, report it, "and continue the tool call". SessionEnd hooks are advisory and cannot steer or keep the thread open. Async hooks are supported ("Run hooks in the background").
- MCP-tool hooks use an existing connection; SessionStart hooks can run before an MCP server is ready.
