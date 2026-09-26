---
source: https://cursor.com/docs/agent/hooks
source_date: undated
researched: 2026-09-26
---

# Cursor hooks: categories, cloud agents, prompt hooks, fail-open and fire-and-forget behaviour

Read as raw page text (curl and html.parser; the page text appears twice in the extraction, once per language variant). Not via WebFetch. The stop hook and beforeShellExecution are covered in the sibling note [cursor-hooks](../../hooks-as-test-gate/sources/cursor-hooks.md); this note records the rest.

- Definition and purposes: "Hooks let you observe, control, and extend the agent loop using custom scripts ... Hooks are spawned processes that communicate over stdio using JSON in both directions." Listed uses: run formatters after edits, analytics, scan for PII or secrets, gate risky operations such as SQL writes, control subagents, inject context at session start.
- Hook surfaces: agent hooks (sessionStart/End, preToolUse, postToolUse, postToolUseFailure, subagent start/stop, beforeShellExecution and after, beforeMCPExecution and after, beforeReadFile, afterFileEdit, beforeSubmitPrompt, preCompact, stop, afterAgentResponse, afterAgentThought), separate Tab hooks for inline completions (beforeTabFileRead, afterTabFileEdit) and an app lifecycle hook (workspaceOpen). The page says these separate surfaces "let you apply different policies to autonomous Tab operations, user-directed Agent operations, and workspace startup".
- Fail behaviour: exit 0 uses the JSON output; for permission hooks (beforeShellExecution, beforeMCPExecution, beforeReadFile, subagentStart, preToolUse) invalid JSON or a schema mismatch blocks the action. Exit 2 blocks. "Other exit codes - Hook failed, action proceeds (fail-open by default)". `failClosed: true` makes a crash, timeout, non-zero exit or empty output block, "Useful for security-critical hooks". Default timeout is "platform default".
- Prompt-based hooks (`type: "prompt"`): "use an LLM to evaluate a natural language condition ... useful for policy enforcement without writing custom scripts", returning `{ok, reason}` from "a fast model". Cloud agents "run command-based hooks only" because prompt hooks need authentication wiring not available there.
- Cloud agents: run project `.cursor/hooks.json`, and on Enterprise team and enterprise-managed hooks; user-level hooks are unavailable; "Cloud agents sometimes begin in a read-only environment for early exploratory turns. Hooks do not run during those turns." sessionStart, sessionEnd, MCP hooks, Tab hooks and workspaceOpen are not supported in cloud agents.
- sessionStart is "fire-and-forget; the agent loop does not wait for or enforce a blocking response"; the schema accepts `continue` but "current callers do not enforce them". It can set session environment variables and inject additional context. sessionEnd is fire-and-forget and "The response is logged but not used".
- afterFileEdit (used in the page's quickstart for a formatter) and afterTabFileEdit have no supported output fields for blocking (afterTabFileEdit: "No output fields currently supported").
- beforeSubmitPrompt "Can prevent submission" with `continue: false`.
- Sources and merging: enterprise (MDM), team (cloud-distributed, synced every thirty minutes), project, user; "any deny wins over ask, and ask wins over allow, regardless of source". Project hooks "run in any trusted workspace". Cursor "watches hooks config files and reloads them automatically". Cursor can also load hooks from third-party tools such as Claude Code (details not read).
- Debug: a Hooks tab in Customize and a Hooks output channel.
- Partners listed for hook-based security and governance include Semgrep ("automatically scan AI-generated code for vulnerabilities with real-time feedback to regenerate code until security issues are resolved"), Snyk, Endor Labs and 1Password. Vendor marketing, no measurements.
