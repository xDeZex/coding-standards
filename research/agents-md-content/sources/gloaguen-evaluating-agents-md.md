---
source: https://arxiv.org/abs/2602.11988
source_date: 2026-06
researched: 2026-09-26
---

# Evaluating AGENTS.md: Are Repository-Level Context Files Helpful for Coding Agents?

Preprint (Gloaguen, Mundler, Raychev, Muller, Vechev; ETH Zurich and LogicStar.ai), arXiv 2602.11988 v2, dated 23 Jun 2026 on the PDF (first version February 2026). Not peer reviewed as far as the page shows. Read from the PDF text (full paper), not only the abstract.

- Design: four coding agents and four LLMs (Sonnet-4.5, GPT-5.2, GPT-5.1 Mini, Qwen3-30B-Coder) on SWE-bench with LLM-generated context files, and on a new benchmark, CtxBench (138 instances, 12 niche Python repos that commit their own context files), comparing no file, an LLM-generated file (agent vendor's recommended /init-style prompt), and the developer-committed file. Success means the generated patch passes the tests.
- Headline: context files "do not generally improve task success rates" while raising inference cost by over 20% on average (20% and 23% for the two file types, with 2.45 and 3.92 more steps). LLM-generated files had a marginal negative effect on success (about 0.5% and 2% on average); developer-committed files a marginal gain (2.4% on average, p = 21%, so not significant). Developer-committed files beat LLM-generated ones by about 7%.
- Instructions are followed: when a tool name appears in the context file its use rises sharply ("uv, pytest, or repository-specific tools ... are used almost exclusively if they are mentioned in the context file"). Across models, with a context file present agents ran more tests, searched, read and wrote more files, and used more repo-specific tooling; reasoning tokens rose (for example +22% for GPT-5.2 with LLM-generated files on SWE-bench). The authors conclude that a lack of instruction following does not explain the missing accuracy gain.
- Repository overviews did not help: 95 to 100% of LLM-generated files (36% for GPT-5.1 Mini) contained an overview, and agents did not reach files touched by the fix faster; they still read the documented files repeatedly.
- Ablation (GPT-5.2 only, one model): removing each category from the LLM-generated file (overview, tooling, testing) changed accuracy insignificantly. Removing the testing category significantly lowered cost on both benchmarks; removing tooling lowered it on SWE-bench. Omitting test-harness details raised SWE-bench accuracy but slightly lowered CtxBench accuracy, so the authors read no effect on accuracy.
- Length: no clear dependence of success or cost on context-file length (binned analysis).
- Documentation effect: when other documentation in the repo was removed, LLM-generated files improved success by 2.7% on average, so the authors suggest the files mostly duplicate existing docs.
- Authors' conclusion: omit LLM-generated files for now; human-written files should contain only instructions not already in the README (specific conventions, non-functional requirements) and be evaluated before adoption. Limits stated or visible: Python only, benchmark tasks resolved by tests, few agents and models, cost measured but not wall-clock, one-model ablation.
- Not measured: whether test-running instructions in a skill versus AGENTS.md change test-running or success; the study has no skills condition.
