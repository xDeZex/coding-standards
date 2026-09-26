---
source: https://www.aihero.dev/tips-for-ai-coding-with-ralph-wiggum
source_date: 2026-01-08
researched: 2026-09-26
---

# Matt Pocock, 11 Tips For AI Coding With Ralph Wiggum (AI Hero)

Read in full via curl and html-to-text (23,700 characters). Byline "Matt Pocock", "20 min read - Updated Jan 8, 2026" (last-updated stamp). Speaker and why trusted: see [pocock-feedback-loops-husky-pre-commit](pocock-feedback-loops-husky-pre-commit.md). This is the Ralph-loop article the leads file listed as unread.

What the page says about the commit gate (tip 5, "Use Feedback Loops"):

- A table of feedback loops lists TypeScript types, unit tests, a Playwright MCP server, ESLint, and "Pre-commit hooks: Blocks bad commits entirely". Under it: "The best setup blocks commits unless everything passes. Ralph can't declare victory if the tests are red."
- Rationale: "Great programmers don't trust their own code. They don't trust external libraries. They especially don't trust their colleagues. Instead, they build automations and checks to verify what they ship. This humility produces better software."
- He also gives an instruction-file version for the loop prompt, next to the hook: "Before committing, run ALL feedback loops: 1. TypeScript: npm run typecheck (must pass with no errors) 2. Tests: npm run test (must pass) 3. Lint: npm run lint (must pass). Do NOT commit if any feedback loop fails. Fix issues first." So the article uses both a prompt instruction and the hook, and does not say which is more reliable.
- Tip 6 on small steps: "The rate at which you can get feedback is your speed limit. Never outrun your headlights." Ralph commits after each feature, and "Ralph can pile dozens of commits into a repo in hours", so low-quality commits compound ("software entropy"). He says the answer is feedback loops (linting, types, tests) to enforce standards, and a clean codebase before starting.
- He says the loop can run in a container for safety ("Ralph can edit project files and commit - but can't touch your home directory, SSH keys, or system files"), which is a different control from the commit gate.
- Not on the page: bypassing the hook, or hook speed limits.
