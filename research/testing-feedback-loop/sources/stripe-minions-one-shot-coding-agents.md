---
source: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents
source_date: 2026-02-09
researched: 2026-09-26
---

# Minions: Stripe's one-shot, end-to-end coding agents (Alistair Gray)

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere. Author and date as reported by the fetch: Alistair Gray, 9 February 2026. First-party account of one organisation's setup, cited by Böckeler.

- Layered tests the agent iterates against. First layer: "an automated local executable, which uses heuristics to select and automatically run selected lints on each git push", in under five seconds.
- Shift feedback left: "it's best for humans and agents if any lint step that would fail in CI is enforced in the IDE or on a git push, and presented to the engineer immediately."
- Capped CI loop: "at most two rounds of CI. If tests fail after an initial push, we prompt the minion to fix failing tests and push a second time, but are then done." Reason given: "there are diminishing marginal returns for an LLM to run many rounds of a full CI loop."
- Autofix: "Many of our tests have autofixes for failures, which we automatically apply."
- Instruction files: the agents use several agent rule file formats also used by human tools; "almost all agent rules at Stripe are conditionally applied based on subdirectories" rather than always loaded.

Unverified: one company's practice, no measured comparison of controls; not read line by line.
