---
source: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
source_date: 2026-01-27
researched: 2026-09-26
---

# AGENTS.md outperforms skills in our agent evals (Vercel)

Re-read 2026-09-26: the page's text and tables read from the raw HTML (curl, html.parser), not a summarising tool. Vendor engineering blog post by Jude Gao, dated 27 Jan 2026 on the page. Not peer reviewed; the agent and model are not named on the page; no sample sizes are given.

- Task: getting agents to use Next.js 16 APIs absent from model training data. The final suite was "hardened" after an initial one had leakage and ambiguous prompts; results below are from the hardened suite.
- Final pass rates (page's table): baseline (no docs) 53%; skill, default behaviour 53% (+0 points); skill with explicit instructions 79% (+26); AGENTS.md compressed docs index 100% (+47). Build / Lint / Test breakdown: baseline 84 / 95 / 63%; skill default 84 / 89 / 58%; skill with explicit instructions 95 / 100 / 84%; AGENTS.md 100 / 100 / 100%. The page notes the default skill did worse than baseline on some metrics (58% versus 63% on tests) and suggests an unused skill may add noise.
- Invocation: "In 56% of eval cases, the skill was never invoked" (in the default-behaviour section). The explicit instruction ("Before writing code, first explore the project structure, then invoke the nextjs-doc skill for documentation") was itself added to AGENTS.md, and raised invocation to "95%+" and pass rate to 79%.
- Wording sensitivity: "You MUST invoke the skill" led agents to read docs first and anchor on doc patterns, missing project context; "Explore project first, then invoke skill" did better. Illustrated on one eval (the `use cache` test).
- The docs index was compressed from about 40 KB to 8 KB (80%) with the 100% pass rate kept; it points to doc files the agent reads as needed, and carries the line "IMPORTANT: Prefer retrieval-led reasoning over pre-training-led reasoning".
- Authors' working theory for the gap: no decision point, consistent availability (skills load only when invoked), no ordering issues. Their caveat: "Agents not reliably using available tools is a known limitation of current models", and the gap "may close as models get better at tool use". They also write that skills are not useless and "work better for vertical, action-specific workflows that users explicitly trigger" (upgrade, migrate), while for "general framework knowledge, passive context currently outperforms on-demand retrieval".
- Limits: reference documentation for one framework, not test-running instructions; the "Test" column is the eval's own pass/fail checks on the generated code. One skill built by the vendor, so a better description could change the invocation rate.
