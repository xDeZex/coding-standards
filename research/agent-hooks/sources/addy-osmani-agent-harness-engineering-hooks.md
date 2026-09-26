---
source: https://addyosmani.com/blog/agent-harness-engineering/
source_date: 2026-04-19
researched: 2026-09-26
---

# Addy Osmani, "Agent Harness Engineering" (hooks passages)

Speaker: Addy Osmani, engineering leader at Google Chrome, author of widely read books and posts on engineering, and a regular writer on agent workflows. Counts as trusted: sustained first-hand writing on running several agents in parallel on real work, and wide readership. The page is a synthesis of others' ideas (HumanLayer, Viv Trivedy, Anthropic, Böckeler) plus his own habits, so on hooks it mostly repeats HumanLayer's position.

How read: raw HTML via curl and html-to-text; whole page searched for "hook" (11 hits) and those passages read. The page's date line reads "April 19, 2026".

- Enforcement: "Hooks are what separate 'I told the agent to do X' from 'the system enforces X.'" Uses: "Run typecheck and lint and tests after every edit and surface failures. Block destructive bash (rm -rf, git push --force, DROP TABLE). Require approval before opening a PR or pushing to main. Auto-format on write so the agent doesn't waste tokens on whitespace."
- Adopts HumanLayer's rule: "success is silent, failures are verbose."
- Incident-driven growth: "You only add constraints when you've seen a real failure. You only remove them when a capable model has made them redundant." His example: after merging a PR with a commented-out test, "The next version of my AGENTS.md says 'never comment out tests; delete them or fix them.' The next version of my pre-commit hook greps for .skip( and xit( in the diff. The next version of my reviewer subagent flags commented-out tests as a blocker." So the same failure is answered in an instruction file, a git hook and a review agent at once, not by an agent hook.
- Loops: "a hook intercepts the model's attempt to exit and re-injects the original prompt into a fresh context window, forcing the agent to continue against a completion goal" (the Ralph loop); and after each step "hooks run a pre-defined test suite and loop failures back to the model with the error text".
- Elsewhere on the page: "the agent ran a destructive command, so you add a hook that blocks it".

He gives no measurements, no failure modes of hooks, and no first-hand hook incident of his own here.
