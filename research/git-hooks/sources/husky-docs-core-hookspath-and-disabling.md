---
source: https://typicode.github.io/husky/how-to.html
source_date: undated
researched: 2026-09-26
---

# Husky docs: how it installs, and how it is disabled

Read 2026-09-26: raw page fetched with curl, HTML stripped to text with a python html.parser script, the relevant sections read in full. No WebFetch. Pages: the home page, Get started and How To on typicode.github.io/husky. The How it works page returned "404" and the GitHub raw docs guesses also 404, so the mechanism comes only from the home page's feature list.

- Home page: husky "Uses new Git feature (core.hooksPath)", "All 13 client-side Git hooks", "Husky doesn't force Git hooks" ("Opt-in/opt-out options", "Can be globally disabled"). "Husky is used in over 1.5M projects on GitHub" (self-reported).
- Install: `npm install --save-dev husky`, then `npx husky init` creates `.husky/pre-commit` and updates the `prepare` script in `package.json`. So installation happens when a developer runs the package manager's install, not by clone.
- Hook file: "echo 'npm test' > .husky/pre-commit". Scripts should be POSIX shell.
- Disabling, verbatim: "Most Git commands include a -n/--no-verify option to skip hooks"; "For commands without this flag, disable hooks temporarily with HUSKY=0: HUSKY=0 git ...". `export HUSKY=0` disables for a session; in `~/.config/husky/init.sh` for a machine ("Husky won't install and won't run hooks on your machine").
- CI and Docker: "To avoid installing Git Hooks on CI servers or in Docker, use HUSKY=0." The `prepare` script may fail in production installs; suggested `"prepare": "husky || true"`. So husky assumes hooks do not run in CI.
- Not in the git root: "Husky doesn't install in parent directories (../) for security reasons".
- Startup files (`~/.config/husky/init.sh`, `~/.huskyrc`) run before hooks, which lets local environment (e.g. node version managers) load; the page does not discuss non-interactive shells or GUI clients beyond "Git GUIs" support claims.
