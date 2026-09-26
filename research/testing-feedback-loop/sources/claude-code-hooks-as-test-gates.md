---
source: https://code.claude.com/docs/en/hooks-guide
source_date: undated
researched: 2026-09-26
---

# Hooks guide and reference (one agent product's first-party docs)

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere. Used here only for how a hook-based control works; product details are one implementation, not general guidance. Pages carry no date (docs change; versions named in text are v2.1.x). Also read: https://code.claude.com/docs/en/hooks (Stop section only).

- Framing: hooks are "user-defined shell commands" run at lifecycle points, "which gives you deterministic control: certain actions always happen rather than relying on the LLM to choose to run them." For judgment rather than rules, prompt-based hooks (single-turn model evaluation, Haiku by default) and agent-based hooks (multi-turn with tool access, "experimental") exist.
- Events include PreToolUse (can block a call), PostToolUse and Stop. Exit 0 = proceed; exit 2 = block, with stderr as the reason; where the reason lands depends on the event, some events feed it to the model as feedback, others show it to the user only. JSON output on exit 0 gives finer control; mixing exit codes and JSON in one hook is discouraged.
- Stop hook: "Prevents Claude from stopping, continues the conversation" on exit 2, so a script that runs a check can hold the turn open until it passes. Input carries `stop_hook_active`, true when a Stop hook is already forcing continuation; the docs suggest scripts check it to avoid loops.
- Loop cap: to prevent infinite loops the product overrides a Stop hook after consecutive blocks without progress; the troubleshooting text says eight in a row and names an environment variable to raise it (the reference page did not state the number in the summary read).
- Pre-tool hooks fire before permission-mode checks and can deny even in bypass modes, so they enforce policy that the user's mode cannot skip.
- Hooks in parallel: several hooks on one event run in parallel; a deny wins. If several rewrite tool input, order is non-deterministic.
- Timeouts vary by hook type; agent hooks default to 60 seconds and up to 50 turns. Hook errors that are not exit 2 are non-blocking: the action proceeds.
- Prompt-hook block on PostToolUse/PreToolUse ends the turn by default unless `continueOnBlock` is set, in which case the reason is fed back.

Unverified: exact per-event tables not read in full; hook behaviour is product- and version-specific.
