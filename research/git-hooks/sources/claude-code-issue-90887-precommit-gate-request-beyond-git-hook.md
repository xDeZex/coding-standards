---
source: https://github.com/anthropics/claude-code/issues/90887
source_date: 2026-08-31
researched: 2026-09-26
---

# Claude Code issue 90887: request for a harness-level commit gate because a git hook is advisory to the agent

How read: issue body and the first two comments read as raw JSON from the GitHub REST API. Open, labelled enhancement, area:security, area:hooks. A user's feature request with the requester's own usage claims; no vendor response seen. The referenced issues #4834 and #40117 were not re-read here ([40117 is in a sibling note](../../hooks-as-test-gate/sources/claude-code-issue-40117-agent-bypasses-precommit.md)).

- Request: a native PreCommit gate that intercepts commits at the tool-call level "not only via git hooks", blocks until an independent reviewer subagent has reviewed the exact staged diff, and refuses `--no-verify` and stash-and-recommit itself. Their statement of the problem: "A client-side git hook is advisory to an agent that controls the shell."
- Their alternatives, with the requester's own assessment: a git pre-commit hook running an adversarial reviewer ("I run this today and it works, but it is bypassable by the agent"); CLAUDE.md instructions ("rationalized past under pressure"); PR-time review (valuable, but "too late"). Asks that the gate block only on confirmed correctness, security and data-loss findings, not style, since "false-positive fatigue creates pressure to disable it".
- Requester's usage claims (unverified, from follow-up comments): a userland version, a pre-commit hook demanding an external model's verdict keyed to the staged file hashes, ran for about 2.5 days across nine repositories and about 68 gated commits, with a docket of catches. The requester lists what userland cannot do: stop the agent bypassing the hook.
- What it shows: the demand for a commit gate outside the agent's shell is expressed by users, and the git hook is described by one power user as a real gate for review only if not bypassed. The inferential (model-judged) check inside a git hook is a use not covered elsewhere in the folder.
