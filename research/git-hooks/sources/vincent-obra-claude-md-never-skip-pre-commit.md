---
source: https://github.com/obra/dotfiles/blob/main/.claude/CLAUDE.md
source_date: 2026-08-08
researched: 2026-09-26
---

# Jesse Vincent (obra), personal CLAUDE.md and Superpowers worktree spec

Read raw from raw.githubusercontent.com: `obra/dotfiles/main/.claude/CLAUDE.md` (about 9,000 characters, whole file read for the Version Control and Testing sections) and, from the obra/superpowers repo, `docs/superpowers/specs/2026-04-06-worktree-rototill-design.md` (only the hooks passage and its header). Date is the last commit to the CLAUDE.md file (2026-08-08 "Resolve contradictions in CLAUDE.md"). A grep of the whole superpowers repo's markdown, shell and JSON for "no-verify", "pre-commit" and "git hook" found only the items below plus release notes about excluding a `.pre-commit-config.yaml` from a sync.

Speaker: Jesse Vincent, author of the widely used Superpowers skills and workflow plugin for coding agents and long-time open-source maintainer (Request Tracker, K-9 Mail). Counts as trusted for authoring a widely used agent practice and publishing his working instructions.

- His own instruction file, under "Version Control": "Be vigilant to make sure nobody ever skips, evades or disables a pre-commit hook." Nearby: "Commit frequently throughout the development process, even if your high-level tasks are not yet done." Under Testing: "Reducing test coverage is worse than failing tests." So he assumes pre-commit hooks exist in his projects and uses an instruction, not a block, to stop bypass. The file gives no reason and no incident.
- The Superpowers worktree design spec (status Draft, 2026-04-06) has a "Hooks awareness" step: "Git worktrees do not inherit the parent repo's hooks directory. After creating a worktree ... symlink the hooks directory from the main repo if one exists ... This prevents pre-commit checks, linters, and other hooks from silently stopping when work moves to a worktree. (Idea from PR #965.)" This is a first-hand note that agent worktrees can silently lose git hooks. A statement in a draft spec, not a confirmed shipped behaviour; his claim about what git does is not checked here (see [claude-code-issue-27474](claude-code-issue-27474-worktree-overwrites-hookspath.md) for a related report).
- Not found: an essay from him on git hooks. The `blog.fsck.com` feed returned 404.

The speaker description above is background I know, not read from the page (except where the page itself says it), and is unverified.
