---
source: https://pre-commit.com/
source_date: undated
researched: 2026-09-26
---

# pre-commit framework docs: install per clone, SKIP, staged-only stash, CI

Read 2026-09-26: raw page fetched with curl, HTML stripped to text with a python html.parser script, the relevant sections read in full. No WebFetch. The page is one long document (the whole page was read for the passages below). Version-specific: the page documents `hook.*` config-based installation, so it is a recent version.

- Not automatic: "Run pre-commit install to install pre-commit into your git hooks. pre-commit will now run on every commit. Every time you clone a project using pre-commit running pre-commit install should always be the first thing you do." The install writes a script into `.git/hooks/pre-commit` ("pre-commit installed at .git/hooks/pre-commit"); the config file `.pre-commit-config.yaml` is what is shared.
- Bypass beyond git's: "pre-commit solves this by querying a SKIP environment variable. The SKIP environment variable is a comma separated list of hook ids. This allows you to skip a single hook instead of --no-verifying the entire commit." Example `SKIP=flake8 git commit -m "foo"`.
- Which files: "usually pre-commit will only run on the changed files during git hooks"; `pre-commit run --all-files` runs everything. Hooks with no matching files show "(no files to check)Skipped" unless `always_run: true`.
- Staged content only: "Running hooks on unstaged changes can lead to both false-positives and false-negatives during committing. pre-commit only runs on the staged contents of files by temporarily stashing the unstaged changes while running hooks."
- Hooks may edit files: example output "Files were modified by this hook", exit code 1, so an auto-fixing hook fails the commit once and the fixed files must be re-staged.
- `fail_fast` (default false) stops after the first failing hook; `require_serial` and `pass_filenames` control parallelism and arguments.
- CI: "adding pre-commit run --all-files as a CI step will ensure everything stays in tip-top shape", or "pre-commit run --from-ref origin/HEAD --to-ref HEAD" for changed files only. Also pre-commit.ci as a hosted option.
- Global install through config-based hooks: "with git config set --global ... this can automatically enable pre-commit for all repositories", but "this setup not recommended as it can lead to accidentally running hooks when interacting with an untrusted repository", and `--skip-on-missing-config` is recommended.
- The page never uses the word agent. It states no timeout or runtime expectation for the hooks.
