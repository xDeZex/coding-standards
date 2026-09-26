---
source: https://github.com/anthropics/claude-code/issues/55754
source_date: 2026-05-03
researched: 2026-09-26
---

# anthropics/claude-code issue 55754: Stop hook returning ok:false loops until the session limit

Re-read pass 2026-09-26: the issue body and all three comments were read as raw JSON from the GitHub REST API (api.github.com/repos/anthropics/claude-code/issues/55754 and /comments). No summarising tool. A single user's report against Claude Code 2.1.126 (Windows, PowerShell, Anthropic API).

- A user-defined `Stop` hook, configured in ~/.claude/settings.json, evaluated whether the user's request was fully answered and returned `{"ok": false, "reason": ...}` whenever it judged the task incomplete. The reporter states it did not check `stop_hook_active`. The report does not say whether the hook was a prompt or command hook (the `ok`/`reason` shape is the prompt-hook schema in the reference).
- Trigger: a custom skill (/testRunner) launched several subagents with `run_in_background: true` and told Claude to stay idle, with no tool calls, until completion notifications arrived. Each idle text turn was graded incomplete, so the hook forced another turn.
- Reported cost: the loop repeated ">100 times over ~50 min" and "consumed my entire session quota" before an external background result arrived and broke the cycle.
- The reporter asks the harness to honour `stop_hook_active` automatically, add a hard cap "e.g. 5 or 10", expose pending background subagents to hooks, and allow skill-side opt-out. Relation to the documented cap: the cap of eight consecutive blocks was added in Claude Code v2.1.143 per the CHANGELOG (see the guide cap note); this report is on v2.1.126, so it predates the cap and says nothing about behaviour with the cap in place.
- Status, corrected from the earlier note: closed on 2026-05-06 by github-actions[bot] as a duplicate of #54360 (the bot's early comment had suggested #54360 and #43906). The reporter's body cites #3573, #10205 and #20221 as the same class of bug, but the closure was not to those. No maintainer comment; locked 2026-06-25. The other issue numbers listed in the previous version of this note (#58348, #94041 and others) came from search results and were not checked here; treat them as unverified.
- What it shows: a stop gate whose pass condition the agent cannot reach becomes a loop, at least on versions without the cap. Failure comes from the hook's condition (here model-judged, waiting on background work), not from tests. It is not evidence about test-running stop hooks. The vendor's own guard is in [hooks guide note](claude-code-hooks-guide-stop-hook-loop-guard.md).
