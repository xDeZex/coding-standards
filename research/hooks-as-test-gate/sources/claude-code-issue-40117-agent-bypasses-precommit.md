---
source: https://github.com/anthropics/claude-code/issues/40117
source_date: 2026-03-28
researched: 2026-09-26
---

# anthropics/claude-code issue 40117: agent bypasses pre-commit hooks

Reading method: fetched through a summarising tool; quotes as returned. A single user's bug report, unverified by Anthropic. Status when read: closed as not planned. Weak evidence as to frequency: one incident, one reporter, no logs checked by us.

- Reporter (slguardo) says Claude Code with Opus 4.6 bypassed a pre-commit hook on six consecutive commits on 2026-03-27, using `--no-verify`, `git stash` to change staged state, and quiet flags to suppress output, and misrepresented what it had done when asked.
- Explicit instructions existed and were violated: a project-memory rule "Do not use `--no-verify` on `git commit`" and a note to never skip hooks unless the user asks.
- The hook covered secret scanning, lint-staged, unit tests with coverage thresholds, 44 integration test files and Playwright E2E. Commits landed with failing tests (104 passed, up to 63 failed per commit).
- Reporter's workarounds: `permissions.deny` rules and a pre-push verification hook.
- What it shows: an instruction is not enforcement, and a commit hook is only a gate if the agent cannot skip it. What it does not show: how common this is. Related: [git hooks docs](git-githooks-pre-commit-bypass.md), [guide on defences](pydevtools-stop-agents-bypassing-precommit.md).
