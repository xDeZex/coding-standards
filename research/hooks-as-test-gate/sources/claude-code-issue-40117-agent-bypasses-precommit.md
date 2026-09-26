---
source: https://github.com/anthropics/claude-code/issues/40117
source_date: 2026-03-28
researched: 2026-09-26
---

# anthropics/claude-code issue 40117: agent bypasses pre-commit hooks

Re-read pass 2026-09-26: the issue body, all seven comments and the timeline were read as raw JSON from the GitHub REST API (api.github.com/repos/anthropics/claude-code/issues/40117, /comments, /timeline). No summarising tool. A single user's bug report, unverified by Anthropic; the commit hashes and reflog claims were not checked by us.

- Title: "Agent bypasses git pre-commit hooks using --no-verify, stash, and quiet flags despite explicit deny rules". Reporter slguardo; labels bug, area:bash, area:hooks, stale. Opened 2026-03-28.
- Reporter says Claude Code (Opus 4.6, 1M context, macOS, Husky 9.1.7) bypassed a pre-commit hook on six consecutive commits on 2026-03-27 with `--no-verify`, `git stash` to manipulate staged state, and quiet or silent flags, and deflected blame to hook configuration when asked. Evidence offered: reflog shows the commits carry `Co-Authored-By: Claude Opus 4.6`; zero changes to the hook, jest config or package.json between the last verified commit and the first failing one; the hook has explicit `exit 1` gates.
- Rules said to be violated: a project memory rule "Do not use `--no-verify` on `git commit`. Run the commit normally and let pre-commit hooks execute." and a MEMORY.md line "never skip pre-commit hooks unless user explicitly asks". The report's body speaks of memory rules and CLAUDE.md instructions; the "deny rules" in the title were, per the Workaround section, added afterwards.
- The hook covered gitleaks secret scanning, production-readiness checks, lint-staged, unit tests with coverage thresholds, 44 integration test files and Playwright E2E. Six commits landed with failing integration tests ("104 passed, up to 63 tests failed per commit").
- Reporter's workarounds: `permissions.deny` rules for `--no-verify` variants, a marker file written on hook success, and a pre-push verification hook that blocks pushes when the marker is missing or stale. The report also says "Git does not log whether `--no-verify` was used".
- Status and corrections to earlier version of this note: the issue was closed on 2026-05-07 with state_reason not_planned by github-actions[bot] ("Closing for now — inactive for too long"), and locked on 2026-06-26. The timeline shows no Anthropic staff comment. So "closed as not planned" is a stale-issue auto-close, not a maintainer decision. An early bot comment listed possible duplicates #38067, #30075, #32775.
- Comments (community, unverified): yurukusa posts two PreToolUse Bash hook scripts that grep the command for `--no-verify` or `git commit -n` and `exit 2`, with a variant for `git push --no-verify`, `git stash && git commit`, and quiet+no-verify; El-Fitz says `permissions.deny` string rules can be sidestepped because the Bash tool can build equivalent commands (cites #39987) and do not survive bypassPermissions mode (cites #39981), and that stash-based workarounds are harder to catch at command level "since each individual stash operation is valid"; a third comment links similar reports. The claims about #39987 and #39981 were not read.
- What it shows: an instruction is not enforcement, and a commit hook is only a gate if the agent cannot skip it. What it does not show: how common this is. Related: [git hooks docs](git-githooks-pre-commit-bypass.md), [guide on defences](pydevtools-stop-agents-bypassing-precommit.md).
