---
source: https://code.claude.com/docs/en/hooks-guide
source_date: undated
researched: 2026-09-26
---

# Claude Code hooks guide: Stop hook loop guard

Reading method: page fetched by a summarising tool; the loop-guard passage was then read verbatim from the saved tool output. Only the loop-guard and determinism claims were taken; general hook mechanics belong to the vendor-mechanics notes in this folder.

- Framing: hooks give "deterministic control: certain actions always happen rather than relying on the LLM to choose to run them."
- Loop guard, verbatim: "Claude Code overrides a Stop hook after it blocks eight times in a row without progress. Your hook script needs to check whether it already triggered a continuation. Parse the `stop_hook_active` field from the JSON input and exit early if it's `true`". The page's example script exits 0 (allows the stop) when `stop_hook_active` is true.
- Reference page (https://code.claude.com/docs/en/hooks) table row read: Stop "Prevents Claude from stopping, continues the conversation" on exit code 2.
- Consequence to note: a Stop gate that exits early on `stop_hook_active` lets the agent stop after one forced continuation even if tests are still red, and the harness override after eight blocks does the same. So a stop hook is a bounded nudge, not a guarantee of green. This reading is ours; the page does not say what happens to the red state afterwards.
- Not found in the read: whether the agent can edit its own hook config mid-session. The reference says direct edits to hooks in settings files are "normally picked up automatically by the file watcher", which suggests edits take effect but the page read did not address agent edits; unverified.
