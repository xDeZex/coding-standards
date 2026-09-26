---
source: https://code.claude.com/docs/en/permission-modes
source_date: undated
researched: 2026-09-26
---

# Claude Code docs: git hook files as protected paths, sandbox denies, runner hooks, changelog

How read: the whole docs set fetched as one text file (https://code.claude.com/docs/llms-full.txt, 10 MB, fetched 2026-09-26) with curl and searched for no-verify, hooksPath, pre-commit, husky, git hook, worktree; the matching passages were read in context. Pages are undated, versioned in text; changelog entries carry version and date. Only matches were read, not every page.

- Permission modes page: protected directories include `.git` and `.husky`; protected files include `.pre-commit-config.yaml`, `lefthook.yml` and variants. `permissions.allow` rules "do not pre-approve protected-path writes". The changelog records `.husky` added to protected directories in v2.1.90 (2026-04-01) and `.pre-commit-config.yaml` among build-tool configs prompted in `acceptEdits` mode in v2.1.160 (2026-06-02). The companion mode table (read in the [test-gate conclusion](../../hooks-as-test-gate/conclusion.md)) says writes are allowed in bypassPermissions mode.
- Sandbox pages (sandbox-environments, sandboxing): "At the project root, the runtime denies `.git/hooks`, denies `.git/config` unless you set `filesystem.allowGitConfig: true`". In a linked worktree the sandbox allows the shared `.git` directory so `git commit` can update refs and index, but "Writes to `hooks/` and `config` inside that directory remain denied." Changelog v2.1.149 (2026-05-22) records fixing the worktree allowlist that had covered the whole main repository root. So under the sandbox the agent can run `git commit` (hooks then execute) but not edit installed hooks.
- Settings reference: `includeGitInstructions` (default true) controls whether Claude Code's built-in "commit and pull request workflow instructions" and a git status snapshot are in context; the page does not say what those instructions say about hooks or `--no-verify`. Changelog v2.1.229 (2026-08-12): `/commit-push-pr` no longer auto-approves git/gh commands with dangerous flags (`--force`, `--amend`, `--no-verify`, etc.).
- Self-hosted runner docs: with `--configure-git` the runner sets `core.hooksPath` to a runner-managed directory whose `commit-msg` and `prepare-commit-msg` hooks add a `Co-authored-by:` trailer; if the image already sets `core.hooksPath` the runner leaves it and skips those hooks. A sample runner-snapshot script pins `core.hooksPath=/dev/null` so that "session-written fsmonitor, hook-path, and gpg-program config" cannot execute code with the hook's privileges. The `plugin eval` docs say Claude Code switches off a repository's git hooks and helper programs for eval runs (needs git 2.31).
- `claude -p` docs list "pre-commit hooks" as a place to call Claude non-interactively (a git hook that calls an agent).
- Not found in the docs text: any statement that the agent passes or avoids `--no-verify` by default, any comparison of git hooks with agent hooks, any statement on hooks running in headless mode for the agent's commits.
- Related: [what's new week 13, git commit hook example](claude-code-whats-new-w13-hook-if-git-commit-example.md).
