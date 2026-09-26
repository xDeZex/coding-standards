---
source: https://lefthook.dev/
source_date: 2026
researched: 2026-09-26
---

# Lefthook docs: how it works, and the LEFTHOOK switch

Read 2026-09-26: raw page fetched with curl, HTML stripped to text with a python html.parser script, the relevant sections read in full. No WebFetch. Pages: https://lefthook.dev/ and https://lefthook.dev/usage/envs/LEFTHOOK/. The page footer says 2026; no other date. The pages are rendered by a docs engine; body text was extracted from the HTML. Only the intro and the LEFTHOOK env page were read; the options pages (skip, fail_on_changes, interactive, parallel) were listed in navigation and not read.

- "Lefthook is a Git hooks manager." "Run lefthook install. Lefthook installs the configured hooks into .git/hooks/. Hook is a simple script that calls lefthook run {hook-name} when executed." Config is `lefthook.yml`; example runs linters in parallel on staged files with `stage_fixed: true`. Built by Evil Martians.
- Disable: "Use LEFTHOOK=0 git ... or LEFTHOOK=false git ... to disable lefthook when running git commands." Example `LEFTHOOK=0 git commit -am "Lefthook skipped"`.
- CI: when the CI sets `CI=true` and the NPM package is installed, "use LEFTHOOK=1 or LEFTHOOK=true to install hooks in the postinstall script", which implies hooks are not installed by default under CI.
- Navigation lists config options that were not read: `no_tty`, `interactive`, `use_stdin`, `fail_on_changes`, `assert_lefthook_installed`, `skip`, `min_version`.
