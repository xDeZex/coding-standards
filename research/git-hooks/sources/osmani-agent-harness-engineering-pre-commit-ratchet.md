---
source: https://addyosmani.com/blog/agent-harness-engineering/
source_date: 2026-04-19
researched: 2026-09-26
---

# Addy Osmani, Agent Harness Engineering (addyosmani.com)

Read in full via curl and html-to-text (raw page, 21,000 characters). Dated "April 19, 2026" on the page. The page says he is "a Member of Technical Staff at Anthropic, where he works on Claude Code" after 14 years at Google leading developer experience (Chrome, then AI). Counts as trusted through a long record of widely read engineering writing and a role on the Claude Code team. Much of the article summarises others (HumanLayer, "Viv", Khan); only what he states himself is recorded.

- The "ratchet": "If the agent ships a PR with a commented-out test and I merge it by accident, that's an input. The next version of my AGENTS.md says 'never comment out tests; delete them or fix them.' The next version of my pre-commit hook greps for .skip( and xit( in the diff. The next version of my reviewer subagent flags commented-out tests as a blocker." So for one failure he uses an instruction, a git hook and a review agent together.
- "You only add constraints when you've seen a real failure. You only remove them when a capable model has made them redundant."
- Hooks section: "Hooks are what separate 'I told the agent to do X' from 'the system enforces X.'" "A hook is a script that runs at a specific lifecycle point: before a tool call, after a file edit, before commit, on session start." Uses listed: typecheck, lint and tests after every edit, blocking destructive bash (`rm -rf`, `git push --force`, `DROP TABLE`), approval before opening a PR or pushing to main, auto-format on write. He draws no line between agent hooks and git hooks here; "before commit" is listed as one lifecycle point beside agent events.
- "success is silent, failures are verbose" (attributed to HumanLayer, "I've come to agree with"): a passing check tells the agent nothing, a failure injects the error text.
- On instruction files: keep short, and every line should trace to a past failure.
- Not on the page: `--no-verify`, hook speed, or when to prefer CI.
