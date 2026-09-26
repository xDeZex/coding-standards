---
source: https://code.claude.com/docs/en/goal
source_date: undated
researched: 2026-09-26
---

# Claude Code /goal: a built-in shortcut for a session-scoped Stop hook

Fetched as raw page text 2026-09-26 (first part read only). First-party vendor docs; a vendor-specific alternative to hand-writing a Stop hook.

- "/goal sets a completion condition and Claude keeps working toward it without you prompting each step. After each turn, a small fast model checks whether the condition holds." It clears when the condition is met, judged impossible, or a turn fails on an error the user must fix.
- Example uses include "Migrating a module to a new API until every call site compiles and tests pass".
- Comparison table on the page: /goal, /loop and a Stop hook. "/goal and a Stop hook both fire after every turn. /goal is a session-scoped shortcut ... A Stop hook lives in your settings file, applies to every session in its scope, and can run a script for deterministic checks or a prompt for model-evaluated ones."
- The hooks reference also says /goal "is a built-in shortcut for a session-scoped prompt-based Stop hook".

Unverified: /goal's condition is judged by a model reading the conversation, so the page as read does not say it runs the test command itself; rest of the page not read.
