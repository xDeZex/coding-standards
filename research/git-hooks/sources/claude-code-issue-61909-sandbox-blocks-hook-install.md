---
source: https://github.com/anthropics/claude-code/issues/61909
source_date: 2026-05-23
researched: 2026-09-26
---

# Claude Code issue 61909: sandbox denies all .git/hooks writes, blocking hook installation by the agent

How read: issue body and comments read as raw JSON from the GitHub REST API. Closed as not planned by github-actions for inactivity (2026-06-24), locked later; no maintainer comment seen. A user's feature request, version 2.1.150.

- Reporter: the sandbox's default deny blocks writes to `hooks/` and `.git/hooks/`, and `sandbox.filesystem.allowWrite` does not override it, so `cp hooks/pre-push .git/hooks/pre-push` fails with "Operation not permitted". This blocks a `make install-hooks` step run by the agent.
- Reporter's rationale for the deny (their words): "git hooks are a classic persistence vector for prompt-injected malicious agents. A `post-commit` or `pre-push` hook installed by a compromised agent runs on every git event, with user credentials, outliving the agent session." Calls the blanket deny reasonable but all-or-nothing.
- A commenter suggests `git config core.hooksPath hooks` instead, so hooks are read from a checked-in directory with no copy step, noting it is per-clone (`.git/config`) and does not propagate on clone.
- Consistent with the docs: [Claude Code docs note](claude-code-docs-git-hook-paths-in-permissions-and-sandbox.md). The rationale is the reporter's inference; the docs pages read do not state a reason.
