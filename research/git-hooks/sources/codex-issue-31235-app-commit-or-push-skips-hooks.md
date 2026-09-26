---
source: https://github.com/openai/codex/issues/31235
source_date: 2026-07-06
researched: 2026-09-26
---

# Codex issue 31235: the desktop app's "Commit or push" action does not run pre-commit hooks

How read: issue body and all three comments read as raw JSON from the GitHub REST API; the cited source files were fetched raw and grepped (see the [docs and source note](codex-docs-sandbox-protected-git-path.md)). Open, labels bug, app, hooks, at fetch time; no maintainer comment seen. A user report of the Codex App 26.623 on macOS.

- Reporter: a `pre-commit` hook running lint-staged and `tsc --noEmit` runs on a terminal `git commit` but not when the commit is created by the app's UI action "Commit or push". A trivial hook that echoes and `exit 1` reproduces it as described: the commit is still created.
- Reporter's diagnosis, explicitly unconfirmed by them: shared internal git helpers in codex-rs/git-utils force `core.hooksPath=/dev/null`. Our check of those files found the override is on Codex's internal helper commands (status and similar); whether the commit action uses them was not established by us or by the reporter.
- Comments: a suggested invariant that a UI commit should either run the hook chain or leave an explicit bypass record, and a second user reporting the same (2026-08-06).
- What it shows: a vendor's own commit button can run under a different hook policy than the terminal commit, so "the same git hook works for a human and an agent" (CONTEXT.md's phrasing) depends on which path in the tool makes the commit. One report, one platform.
