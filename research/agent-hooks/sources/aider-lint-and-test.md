---
source: https://aider.chat/docs/usage/lint-test.html
source_date: undated
researched: 2026-09-26
---

# Aider: linting and testing after edits (no hook system)

Read in full as raw page text (curl and html.parser). Included as a contrast: a harness that runs checks after edits through built-in settings rather than a general hook mechanism. The page does not say whether Aider has hooks; that was not researched.

- "Aider can automatically lint and test your code every time it makes changes." By default it lints files it edits (disable with `--no-auto-lint`); `--lint-cmd` sets the linter, which must print errors and return a non-zero exit code. Tests run with `/test <command>`, or automatically with `--test-cmd` plus `--auto-test`, again "expects the command to print them on stdout/stderr and return a non-zero exit code".
- Formatter interaction: "Many people use code formatters as linters ... These tools sometimes return non-zero exit codes if they make changes, which will confuse aider into thinking there's an actual lint error." The page's workaround is a wrapper script that runs the formatter twice (`pre-commit run --files "$@" || pre-commit run --files "$@"`) so only a real problem fails.
- The page shows a per-edit check fixed to Aider's own loop; it does not describe blocking, timeouts or bypass.
