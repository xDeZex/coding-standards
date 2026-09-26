---
source: https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents-part-2
source_date: 2026-02-19
researched: 2026-09-26
---

# Stripe, Minions: one-shot, end-to-end coding agents, Part 2 (stripe.dev)

Read via curl; the article body is inside the page's HTML, and the section "... and iterate" was read in full from there (the html-to-text output only showed the page chrome). Date "2026.2.19" is the stamp near this page's metadata; the author line I saw belongs to the Part 1 page (Alistair Gray, Leverage team), so the Part 2 author is not confirmed. The rest of the post (devboxes, blueprints, MCP tooling) was not read closely.

Speaker: Stripe engineering, describing its internal coding agents ("minions", over a thousand merged PRs a week per the post's own summary). Counts as trusted through a first-party, production-scale account of running agents on real work; it is a company statement, not measured data.

- "We try to operate under the principle of 'shifting feedback left'... if we know an automated check will fail CI, it's best if it's also enforced in the IDE and presented to the engineer right away".
- "For example, we have pre-push hooks to fix the most common lint issues. A background daemon precomputes lint rule heuristics that apply to a change and caches the results of running those lints, so developers can usually get lint fixes in well under a second on a push." This is a git hook, for human developers as well.
- "Minions naturally integrate with this framework as well, so they don't have to waste tokens or CI minutes by iterating against an auto-formatter or similar. We run a subset of linters as a deterministic node within the agent devloop blueprint, and loop on that lint node locally before pushing an agent's branch, so that the branch has a fair shot at passing CI the first time around." So for the agent, the lint check is a step in Stripe's own orchestration code (a "blueprint" node), not a hook that fires on the agent's own git command.
- "It's infeasible to run all tests locally, so we also include one iteration against the full CI suite" and, after that, "we send the failure back ... one more chance", then to the human. "CI runs cost tokens, compute, and time, and we think there are diminishing marginal returns if an LLM is running against indefinitely many rounds of a full CI loop." The 3 million tests run in CI, not in a hook.
- The safety line is separate: minions run in isolated devboxes with no production access and an internal security control framework to stop destructive tool use.
- Not stated: whether agents' `git push` goes through the same pre-push hook, bypass, or how often the hook catches anything.
