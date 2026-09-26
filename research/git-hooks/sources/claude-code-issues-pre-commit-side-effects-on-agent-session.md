---
source: https://github.com/anthropics/claude-code/issues/45073
source_date: 2026-04-08
researched: 2026-09-26
---

# Claude Code issues 45073, 65575, 66498, 28823, 7714: how hook side effects and output reach the agent

How read: each issue's body and comments read as raw JSON from the GitHub REST API (bodies truncated in the read for 28823 and 7714). All are user reports, unverified; 45073 and 65575 closed as not planned by github-actions for inactivity, 66498 closed as a duplicate of #61109 (not read), 28823 closed completed, 7714 auto-closed.

- #45073 (v2.1.85, macOS): a pre-commit hook that modifies files in place (trailing-whitespace, end-of-file-fixer) fails the first commit and modifies the file; the agent re-stages and commits; on later turns the agent's view of the file reverts to pre-edit content ("was modified, either by the user or by a linter"), so it re-applies edits. On-disk file and git history were correct. Workaround: the user commits manually.
- #65575 (macOS): the Edit tool's "file modified since read" guard fires after the agent's own commit triggered an auto-formatter (ruff, black) that touched unrelated lines, costing a re-Read.
- #66498 (2026-06-09): output from a pre-commit hook (a pytest run) is visible to the model in the tool result but not shown to the user, who then cannot verify tests ran; the model "argued with user that output was shown when it was not" (issue 66404, not read).
- #28823 (v2.1.58, macOS; one-paragraph report): when lint-staged fails in a pre-commit hook and is still cleaning up its `index.lock`, "Claude Code sees the failure, immediately retries (sometimes bypassing hooks), and hits the lock file". The reporter's summary, no logs; the "sometimes bypassing hooks" claim has no transcript.
- #7714 (2025-09, a git-manager subagent): when hooks fail on a test runner, the agent does not clearly say the commit was blocked and leaves staged uncommitted files; the reporter expects it to "offer alternatives (--no-verify, fix tests, disable hooks, etc.)".
- Common thread: formatting and test hooks that run at commit change the state the agent is holding (files, index, lock files) and its output reaches the agent, and sometimes the user, in different ways. These are formatting, lint and test hooks; no source here covers secret-scanning hooks except the gitleaks step in the [40117 note](../../hooks-as-test-gate/sources/claude-code-issue-40117-agent-bypasses-precommit.md).
