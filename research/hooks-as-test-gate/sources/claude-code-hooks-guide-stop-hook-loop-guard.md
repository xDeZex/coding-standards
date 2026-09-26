---
source: https://code.claude.com/docs/en/hooks-guide
source_date: undated
researched: 2026-09-26
---

# Claude Code hooks guide: Stop hook loop guard

Re-read pass 2026-09-26: the earlier version of this note came from a summarising fetch; this time the page was downloaded raw with curl, converted to text and the quoted passages checked against it. Only the loop-guard and determinism claims are recorded here; general mechanics are in the companion notes.

- Framing, verbatim: hooks give "deterministic control: certain actions always happen rather than relying on the LLM to choose to run them." The same page adds that for judgment rather than deterministic rules there are prompt and agent hooks.
- Loop guard, verbatim: "Claude Code overrides a Stop hook after it blocks eight times in a row without progress. Your hook script needs to check whether it already triggered a continuation. Parse the stop_hook_active field from the JSON input and exit early if it's true". The page's example script exits 0 (allows the stop) when `stop_hook_active` is true. Checked: quotes match the page.
- Reference page row read raw: Stop on exit code 2 "Prevents Claude from stopping, continues the conversation".
- Consequence to note (ours, not on the page): a Stop gate that exits early on `stop_hook_active` lets the agent stop after one forced continuation even if tests are still red, and the harness override after eight blocks does the same. The page does not say what happens to the red state afterwards.
- Editing hook config mid-session (previously unverified): the guide says "If you edit settings files directly while Claude Code is running, the file watcher normally picks up hook changes automatically" and that the /hooks menu is read-only, "to add, modify, or remove hooks, edit your settings JSON directly or ask Claude to make the change." Details and the protected-path rules are in the cap note.
