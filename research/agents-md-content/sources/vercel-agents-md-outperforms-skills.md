---
source: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
source_date: 2026-01-27
researched: 2026-09-26
---

# AGENTS.md outperforms skills in our agent evals (Vercel)

Vendor engineering blog post by Jude Gao, 27 Jan 2026. Read through a summarising fetch tool, plus search snippets; quotes should be rechecked. Not peer reviewed; the agent and model were not named in the summary.

- Task: getting agents to use up-to-date Next.js 16 APIs (knowledge absent from model training). Evals scored build, lint and test.
- Results, pass rate: baseline (no docs) 53%; skill with default behaviour 53%; skill with explicit instructions to use it 79%; an AGENTS.md compressed docs index (about 8 KB after an 80% reduction) 100%. Test-only pass rates: baseline 63%, skill with instructions 84%, AGENTS.md 100%.
- Skill invocation: in 56% of eval cases the skill was never invoked under default behaviour; explicit instructions raised invocation to 95% or more.
- Wording sensitivity: "You MUST invoke the skill" made agents anchor on documentation patterns and miss project context; "explore project first, then invoke skill" did better.
- The authors' stated caveat: agents not reliably using available tools is a known limitation of current models. Their conclusion is limited to general framework knowledge, where passive context beat on-demand retrieval.
- Relevance and limits: this is the only first-hand measurement found that compares always-loaded AGENTS.md with a skill. It concerns reference documentation, not test-running instructions, and the "tests" here are the eval's own checks, not the agent running tests. The skill setup (one skill, its description quality) is the vendor's own, so a better description might change the invocation rate ([SkillsBench](skillsbench-benchmark.md) mentions poorly designed descriptions).
