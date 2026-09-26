---
source: https://code.claude.com/docs/en/goal
source_date: undated
researched: 2026-09-26
---

# Claude Code /goal: a built-in shortcut for a session-scoped Stop hook

Re-read pass 2026-09-26: whole page downloaded with curl as HTML, converted to text and read end to end (no summarising tool). The hooks reference (https://code.claude.com/docs/en/hooks, Stop section) was read raw for the last bullet. First-party vendor docs; a vendor-specific alternative to hand-writing a Stop hook.

- "The /goal command sets a completion condition and Claude keeps working toward it without you prompting each step. After each turn, a small fast model checks whether the condition holds." The goal clears when the condition is met, when the model judges it impossible, or when a turn fails on an error the user must fix (authentication failure, exhausted credit balance, context overflow that auto-compaction could not clear, unavailable model).
- Example use on the page: "Migrating a module to a new API until every call site compiles and tests pass".
- Comparison table (/goal, /loop, Stop hook). Below it: "/goal and a Stop hook both fire after every turn. /goal is a session-scoped shortcut: you type a condition and it's active for the current session only. A Stop hook lives in your settings file, applies to every session in its scope, and can run a script for deterministic checks or a prompt for model-evaluated ones."
- Evaluator does not run the tests: "The evaluator judges your condition against what Claude has surfaced in the conversation. It doesn't run commands or read files independently, so write the condition as something Claude's own output can demonstrate. 'All tests in test/auth pass' works because Claude runs the tests and the result appears in the transcript for the evaluator to read." Later: "It does not call tools, so it can only judge what Claude has already surfaced in the conversation." Verdicts are not met, met, impossible. Default model is Haiku on the Claude API.
- Stall guard on the page: "If Claude keeps answering the evaluator without making progress (no tool use for several turns in a row), Claude Code stops the loop, prints a warning, and returns control to you with the goal still set." The page gives no numeric turn cap; it suggests writing a turn or time clause into the condition.
- Other stated behaviour: "/goal is a wrapper around a session-scoped prompt-based Stop hook"; it is unavailable when disableAllHooks is true or allowManagedHooksOnly is set, and follows the same workspace trust rule as settings-file hooks; it works with `claude -p`; evaluation is skipped for a turn while a subagent or background shell is still running.
- The hooks reference says the same: "The /goal command is a built-in shortcut for a session-scoped prompt-based Stop hook."

Now settled from the page: /goal does not itself run the test command; it reads the transcript. Not on the page: a numeric cap on evaluated turns.
