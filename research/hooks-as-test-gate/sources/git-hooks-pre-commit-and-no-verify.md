---
source: https://git-scm.com/docs/githooks
source_date: undated
researched: 2026-09-26
---

# Git hooks: pre-commit, pre-push, and the --no-verify bypass

Re-read 2026-09-26 as raw HTML fetched with curl, stripped to text with a python html.parser script; githooks, git-commit, git-push, git-clone and the Pro Git chapter https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks were read and quotes checked; no WebFetch used. Primary docs (Git project).

- pre-commit: "invoked by git-commit, and can be bypassed with the --no-verify option. It takes no parameters, and is invoked before obtaining the proposed commit log message and making a commit. Exiting with a non-zero status from this script causes the git commit command to abort before creating a commit." (Any non-zero status, unlike Claude Code hooks where only exit 2 blocks.)
- git-commit option: "-n / --no-verify: Bypass the pre-commit and commit-msg hooks." commit-msg can likewise be bypassed. prepare-commit-msg is "not suppressed by the --no-verify option" per the page, so it should not replace pre-commit, but it can also gate.
- pre-push: "If this hook exits with a non-zero status, git push will abort without pushing anything." The githooks page names no flag, but https://git-scm.com/docs/git-push documents `--no-verify` (synopsis lists `[--no-verify]`): "Toggle the pre-push hook (see githooks[5]). The default is --verify, giving the hook a chance to prevent the push. With --no-verify, the hook is bypassed completely."
- Location: $GIT_DIR/hooks/*, or the directory named by `core.hooksPath`; files without the executable bit are ignored.
- Hooks are not copied on clone. The Pro Git book (https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks) says: "It’s important to note that client-side hooks are not copied when you clone a repository. If your intent with these scripts is to enforce a policy, you’ll probably want to do that on the server side". The githooks and git-clone reference pages do not say it. This repo's own README enables its hook with `git config core.hooksPath .githooks`, per research/README.md, an example of per-clone opt-in.
- Relevance to agents: the bypass is a flag on the same command the agent runs, so an agent can skip a git hook with -n; an agent-side hook (Claude Code PreToolUse on Bash) can match and deny it, but no source read documents that recipe.

Unverified: whether agent tools pass --no-verify by default (not stated).
