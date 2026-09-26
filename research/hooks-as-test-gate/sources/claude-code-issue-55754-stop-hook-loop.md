---
source: https://github.com/anthropics/claude-code/issues/55754
source_date: 2026-05-03
researched: 2026-09-26
---

# anthropics/claude-code issue 55754: Stop hook returning ok:false loops until the session limit

Reading method: fetched through a summarising tool; quotes as returned. A single user's report, closed as a duplicate of #3573, #10205 and #20221, with no maintainer reply visible in what was read. Search results also listed several similar Stop-hook loop reports (#3573, #54360, #58348, #94041 in this repo, plus reports in third-party plugin repos); their bodies were not read, so their claims are unverified.

- A user-defined Stop hook judged whether the request was fully answered and returned `{"ok": false, "reason": ...}` whenever it thought the task incomplete. It did not check `stop_hook_active`.
- The user's skill told Claude to stay idle while background subagents finished, so each forced continuation could only be a text turn, was judged incomplete again, and the loop never ended.
- Reported cost: the whole session quota, about 50 minutes.
- What it shows: a stop gate whose pass condition the agent cannot reach becomes a loop. Failure comes from the hook's condition, here a model-judged one, not from tests. It is not evidence about test-running stop hooks specifically. The vendor's own guard is in [hooks guide note](claude-code-hooks-guide-stop-hook-loop-guard.md).
