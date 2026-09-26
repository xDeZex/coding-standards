---
source: https://developers.openai.com/codex/agent-approvals-security
source_date: undated
researched: 2026-09-26
---

# Codex docs and source: .git is read-only in the default sandbox, with hook risk as the stated reason in a test

How read: the docs page fetched with curl and stripped to text with a small html.parser script (searched for git, hook, protected, commit, worktree); two source files (codex-rs/sandboxing/src/seatbelt_tests.rs and codex-rs/git-utils/src/operations.rs, info.rs) fetched raw from raw.githubusercontent.com main and grepped for hook. Page is undated; code is main at fetch time. Only the matching passages were read, not the whole page.

- Docs, "Protected paths in writable roots": "In the default workspace-write sandbox policy, writable roots still include protected paths: `<writable_root>/.git` is protected as read-only whether it appears as a directory or file"; a `gitdir:` pointer file's resolved directory is also read-only; `.agents` and `.codex` directories too; "Protection is recursive, so everything under those paths is read-only." The page as read gives no reason for it.
- The same page: Codex recommends "Auto (workspace write + on-request approvals)" for version-controlled folders; `--ask-for-approval never` works with all sandbox modes.
- Source, seatbelt_tests.rs: a test writes `.git/hooks/pre-commit` under the sandbox and asserts it fails. A comment on the test fixture gives the reason: "a bad actor could write to .git/hooks/pre-commit so an unsuspecting user would run code as privileged the next time they ran `git commit` themselves, or modified .codex/config.toml to contain `sandbox_mode = \"danger-full-access\"`". So in Codex a git hook is treated as a code-execution persistence path that the agent must not write, which also means the agent cannot install or edit hooks under the default sandbox.
- Source, operations.rs and info.rs: Codex's internal git helper commands (status, worktree info and similar; the code comments say "Keep internal Git helper commands independent of configured hook directories" and "repository-selected hooks and fsmonitor helpers") are run with `-c core.hooksPath=/dev/null` (NUL on Windows). That is for Codex's own read-side helper calls; the files read do not show how the agent's own `git commit` in the shell or the desktop app's commit action is run (see [issue 31235](codex-issue-31235-app-commit-or-push-skips-hooks.md)).
- The docs page's hooks page examples call `git rev-parse --show-toplevel` to locate `.codex/hooks/*.py` (agent hooks); the pages read do not compare agent hooks with git hooks.
- Related: [issue 7071](codex-issue-7071-sandbox-git-readonly-blocks-commit.md).
