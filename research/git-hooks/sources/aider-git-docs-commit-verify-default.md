---
source: https://github.com/Aider-AI/aider/blob/main/aider/website/docs/git.md
source_date: undated
researched: 2026-09-26
---

# Aider git integration docs and source: commits skip hooks by default

How read: raw files fetched with curl from raw.githubusercontent.com (docs/git.md, aider/repo.py, aider/args.py on the main branch, fetched 2026-09-26) and read as text. No summarising tool. The docs page carries no date; the code is the main branch at fetch time, not a pinned release.

- Docs (git.md): Aider "commits those changes with a descriptive commit message" whenever it edits a file, and first commits pre-existing uncommitted changes of the user's ("dirty commits").
- The same page, under "Disabling git integration", says: "`--git-commit-verify` will run pre-commit hooks when making git commits. By default, aider skips pre-commit hooks by using the `--no-verify` flag (`--git-commit-verify=False`)."
- args.py: `--git-commit-verify` is a BooleanOptionalAction with `default=False`, help text "Enable/disable git pre-commit hooks with --no-verify (default: False)".
- repo.py, in the commit method: `if not self.git_commit_verify: cmd.append("--no-verify")`, so the flag is added to every Aider commit unless the user opts in. The commit is built as `-m <message>` plus either the named files or `-a`.
- So this is the one agent among those read where the tool itself passes `--no-verify` by design and says so in its docs. The docs give no rationale for the default.
- The docs page says nothing about what Aider does when a commit fails because a hook rejected it (with `--git-commit-verify` on).
- Related: [issue 5057](aider-issue-5057-default-commits-skip-precommit.md), [issue 802](aider-issue-802-precommit-ignored-test-cmd-answer.md).
