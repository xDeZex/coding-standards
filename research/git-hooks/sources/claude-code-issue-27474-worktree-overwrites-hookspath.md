---
source: https://github.com/anthropics/claude-code/issues/27474
source_date: 2026-02-21
researched: 2026-09-26
---

# Claude Code issues 27474, 66993, 88747: creating an agent worktree rewrites core.hooksPath

How read: three issues and their comments read as raw JSON from the GitHub REST API (27474 first 8 comments, 66993 and 88747 first comments in part). 27474 and 88747 are open, labelled bug and reproduced or has repro; 66993 was auto-closed as not planned for inactivity with a bot duplicate flag pointing at 27474. All are user reports; the mechanism claims are the reporters' from their own tests and, in one case, from reading the binary, and were not verified by us.

- #27474 (opened 2026-02-21, v2.1.50 macOS; still reported not fixed in v2.1.114, 2.1.140 on Windows, 2.1.146 on Linux, 2.1.163 and later): `claude --worktree` (and the EnterWorktree tool and `Agent` with `isolation: "worktree"`) runs `git config core.hooksPath <main repo>/.git/hooks` against the shared config, overwriting a custom `core.hooksPath` such as `.githooks`. A commenter says the setup code checks for `.husky` and `.git/hooks` and does not check whether `core.hooksPath` is already set.
- #66993 (v2.1.170, Linux): the rewrite lands in shared `.git/config`, so a committed-hooks setup (`core.hooksPath=hooks`) is "silently disabled" for the main checkout and every other worktree, and re-asserted on each new worktree. A commenter: "silently disabled a pre-commit guardrail in the main checkout three separate times before we found the writer".
- #27474 comment (Windows, 2026-05-13): "When `core.hooksPath` points at a stale absolute path, git silently runs zero hooks (verified — invalid `core.hooksPath` does NOT fall back to `.git/hooks`). In one drift event, ~25 commits bypassed the entire local chain before CI caught a TLS violation the local hook would have rejected." Self-reported.
- #88747 (v2.1.237, macOS): the shared config is no longer clobbered, but the tool writes an absolute `core.hooksPath` into the worktree's `config.worktree`, so with husky the hook scripts that run in the worktree are the main checkout's, on whatever branch it sits on. The reporter's control table says plain `git worktree add` writes no `config.worktree` while 5 of 5 tool-made worktrees carry the pair. Consequence claimed: a PR that removes a hook step still runs the old stronger hook; a PR that adds one gets no local run. Later comments report the Windows form (backslash absolute path) blocking every commit in the worktree, and a census of 107 worktrees in one repo where 13 of 13 tool-made ones carried the override (a comment, unverified).
- Workarounds mentioned: SessionStart hook to re-set `core.hooksPath`; forwarding shims in `.git/hooks`; a `WorktreeCreate` hook (one commenter says it replaces native creation entirely, so it cannot just fix config).
- What it shows: a coding agent's own worktree setup can silently turn a git hook off or point it at other code; git gives no error when the hook path is stale. Frequency unknown beyond the reports.
