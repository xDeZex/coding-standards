---
source: https://github.com/anthropics/claude-code/issues/66069
source_date: 2026-06-07
researched: 2026-09-26
---

# Claude Code issue 66069: commit-msg hook not firing on agent commits (cause contested)

How read: issue body and all comments read as raw JSON from the GitHub REST API. Closed as not planned by github-actions for inactivity on 2026-07-14, locked 2026-09-12. A user report; the counter-analysis is a community comment, neither verified by us or the vendor.

- Reporter (macOS, Opus 4.6): `pre-commit` hook output is visible when Claude Code commits, but a `commit-msg` hook (conventional-commit check, symlinked into `.git/hooks`) never fires and non-conforming commits go through. Reporter's guess: the harness runs `pre-commit` separately and then `git commit --no-verify`.
- Commenter yurukusa (community) argues that cannot be: `--no-verify` would also skip `pre-commit`, which did fire. Says they reproduced a scratch repo where the harness-style `git commit` ran both hooks and a rejecting `commit-msg` aborted it. Their explanation: `core.hooksPath` was set (by the pre-commit framework or husky), so git reads all hooks from that directory and ignores `.git/hooks/`; the framework installs only the `pre-commit` stage unless `pre-commit install --hook-type commit-msg` is run. Gives `git config --get core.hooksPath` and `GIT_TRACE=1` as diagnostics. The reporter did not reply in the thread.
- What it shows: a missed commit-msg check on agent commits was plausibly a hook-installation issue, not agent bypass, and the report cannot separate the two. It is an example of how a git hook can look enforced but be partly wired; nothing here is specific to agents.
