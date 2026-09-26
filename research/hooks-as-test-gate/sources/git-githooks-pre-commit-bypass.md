---
source: https://git-scm.com/docs/githooks
source_date: undated
researched: 2026-09-26
---

# git documentation: githooks (pre-commit bypass and hook location)

Reading method: fetched through a summarising tool; quotes as returned.

- On pre-commit: "This hook is invoked by git-commit, and can be bypassed with the `--no-verify` option." So a git commit hook is advisory by design: whoever runs the commit can skip it.
- Hooks live in the git directory (`.git/hooks/`), which is not version controlled; `git init` may copy hooks from a template directory, and the fetch reported they are not shared by clone. So a hook is per-clone unless the team arranges otherwise (for example a tracked hooks directory with `core.hooksPath`; this repo's README does that, the git page summary did not state it).
- Relevance: a git commit hook can only block an agent that does not add `--no-verify`. See [issue 40117](claude-code-issue-40117-agent-bypasses-precommit.md).
