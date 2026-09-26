---
source: https://kiro.dev/docs/hooks/
source_date: undated
researched: 2026-09-26
---

# Kiro hooks

Read as raw page text (curl and html.parser). Read the overview, the triggers table and the file schema; the linked Hook Triggers, Hook Actions, Best Practices and Troubleshooting pages were not opened.

- Definition: hooks "run shell commands or agent prompts automatically when specific events happen in your session". Uses named: enforce standards (linters, formatters, type checks after agent file changes), gate dangerous operations (PreToolUse), generate companion files, validate before commit, inject context.
- Two action types: `command` (shell command in the project root, receiving JSON on stdin; default timeout 60 seconds, 0 disables) and `agent` (injects a prompt into the current conversation, "steering the agent's behavior"). An agent-action hook is a model-read instruction fired by an event, not deterministic code.
- Triggers with a "Can block?" column: Prompt Submit (yes), Agent Stop (no), Session Start (no), Agent Spawn (CLI, no), Pre Tool Use (yes), Post Tool Use (no), File Create, File Save and File Delete (no), Pre Task Execution (yes), Post Task Execution (no). "File triggers respond only to changes made by the agent. Saving, creating, or deleting a file manually in the editor does not trigger" the file hooks. Availability differs across IDE, CLI and web.
- Stop hooks: Agent Stop is listed as unable to block, so it does not continue the agent (per the table); a Stop command hook can ask for confirmation before it runs.
- Hooks are stored as JSON in `.kiro/hooks/` and "activate automatically when a session starts". An `enabled: false` field skips a hook without deleting it. The format changed between IDE 0.x, IDE 1.0 and CLI 2.x to 3.0 (a migration command exists), so a hook file's format is version-dependent.
