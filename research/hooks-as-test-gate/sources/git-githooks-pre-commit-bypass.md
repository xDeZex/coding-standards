---
source: https://git-scm.com/docs/githooks
source_date: undated
researched: 2026-09-26
---

# git documentation: githooks (pre-commit bypass and hook location)

Reading method: re-read 2026-09-26 as raw page text (curl, HTML stripped with a small python parser), plus the raw git-init, git-clone and gitrepository-layout pages for the template and location claims. An earlier version came from a summarising fetch.

- On pre-commit: "This hook is invoked by git-commit, and can be bypassed with the `--no-verify` option." So a git commit hook is advisory by design: whoever runs the commit can skip it.
- Hooks live in `$GIT_DIR/hooks/*`, or the directory named by `git config core.hooksPath`; hooks without the executable bit are ignored. "git init may copy hooks to the new repository, depending on its configuration" (see the TEMPLATE DIRECTORY section of git-init); the page says nothing about clone. The earlier claim that the git directory is not version controlled and hooks are not shared by clone is not stated on githooks, git-init, git-clone or gitrepository-layout as read, so it is unverified from the docs (it is widely true in practice: `.git/` is not tracked). Whether a team arranges a tracked hooks directory via `core.hooksPath` is our reading of the option; this repo's README does that.
- Also on the page: the hook "takes no parameters"; a non-zero exit from it "causes the git commit command to abort before creating a commit". Relevance: a git commit hook can only block an agent that does not add `--no-verify`. See [issue 40117](claude-code-issue-40117-agent-bypasses-precommit.md).
