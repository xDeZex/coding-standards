---
source: https://github.com/anthropics/claude-code/issues/41797
source_date: 2026-04-01
researched: 2026-09-26
---

# anthropics/claude-code issue 41797: hooks docs omit the stale-read warning for formatter and linter workflows

Documentation issue by one user, read as raw JSON from the GitHub API (body and five comments, all by the reporter). Closed `not_planned` by github-actions for inactivity on 2026-08-14. Practitioner-level source, but it quotes a vendor changelog entry that we did not open.

- The reporter quotes the changelog for v2.1.89: "Improved Bash tool to warn when a formatter/linter command modifies files you have previously read, preventing stale-edit errors" (quoted second-hand; the changelog was not read).
- The point: the hooks guide recommends a PostToolUse `Edit|Write` Prettier hook, but the docs do not explain what happens when a formatter rewrites a file the agent already read, and the agent may need to re-read it before its next edit. The reporter lists six doc pages that recommend format or lint hooks.
- The reporter re-verified on 2026-04-27, 2026-05-18, 2026-06-05 and 2026-06-27 that the docs did not mention it, then it was closed by the stale bot. The first-party guide as read on 2026-09-26 (see the guide note) still shows the Prettier example without a note on this.
- What it shows: a formatting hook changes files behind the agent's back, and a known interaction between that and the agent's edit flow had to be handled by a separate warning. No source measures how often this costs a retry.
