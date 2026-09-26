---
source: https://git-scm.com/docs/githooks
source_date: undated
researched: 2026-09-26
---

# Git hooks: pre-commit, pre-push, and the --no-verify bypass

Fetched as raw page text (not through a summarising tool) on 2026-09-26. Also read https://git-scm.com/docs/git-commit for the option. Primary docs (Git project).

- pre-commit: "invoked by git-commit, and can be bypassed with the --no-verify option. It takes no parameters, and is invoked before obtaining the proposed commit log message and making a commit. Exiting with a non-zero status from this script causes the git commit command to abort before creating a commit." (Any non-zero status, unlike Claude Code hooks where only exit 2 blocks.)
- git-commit option: "-n / --no-verify: Bypass the pre-commit and commit-msg hooks." commit-msg can likewise be bypassed. prepare-commit-msg is "not suppressed by the --no-verify option" per the page, so it should not replace pre-commit, but it can also gate.
- pre-push: "If this hook exits with a non-zero status, git push will abort without pushing anything." The page as read does not name a flag; `git push --no-verify` bypass is not confirmed here (unverified; check git-push docs).
- Location: $GIT_DIR/hooks/*, or the directory named by `core.hooksPath`; files without the executable bit are ignored.
- This repo's own README enables its hook with `git config core.hooksPath .githooks`, per research/README.md, illustrating that hooks are per-clone opt-in (git does not copy hooks on clone; the page as read does not state this outright, so treat it as unverified from the docs).
- Relevance to agents: the bypass is a flag on the same command the agent runs, so an agent can skip a git hook with -n; an agent-side hook (Claude Code PreToolUse on Bash) can match and deny it, but no source read documents that recipe.

Unverified: pre-push bypass; hooks-not-cloned claim; whether agent tools pass --no-verify by default (not stated).
