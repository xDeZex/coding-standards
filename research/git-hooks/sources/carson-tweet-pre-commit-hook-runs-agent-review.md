---
source: https://x.com/ryancarson/status/1948869082511802648
source_date: 2025-07-25
researched: 2026-09-26
---

# Ryan Carson, tweet on a pre-commit hook that asks an agent to review

Read as JSON from `api.fxtwitter.com/ryancarson/status/1948869082511802648` (full text of one post; no thread or replies read). Posted 25 July 2025.

Speaker: Ryan Carson, founder of Treehouse and a public builder using Amp and Claude Code. Weakest trust case in this set: an enthusiast's tip, not a long-run account; included because it shows a pattern (a git hook that calls an agent) no other source does.

- "Did you know you can add a pre-commit hook to ask your AI agent to check your work before committing code? This can be done both in Claude Code and @AmpCode." Steps: install Husky, `npx husky init`, edit `.husky/pre-commit` "to add your checks (tests, linting, etc.)", "Commit and enjoy automatic quality gates".
- His example runs the agent non-interactively from the hook: `amp -x "Oracle, review changes we're about to commit"` (`-p` in Claude Code). That makes the commit gate an inferential control, model-judged and non-deterministic, and running one model call on every commit.
- No claim about results, cost, latency or failure. Contrast [Böckeler](bockeler-harness-engineering-hook-placement-and-timing.md), who says LLM checks are "expensively and probabilistically. Not on every commit."

The speaker description above is background I know, not read from the page (except where the page itself says it), and is unverified.
