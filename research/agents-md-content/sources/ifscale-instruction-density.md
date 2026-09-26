---
source: https://arxiv.org/abs/2507.11538
source_date: 2025-07
researched: 2026-09-26
---

# How Many Instructions Can LLMs Follow at Once? (IFScale)

Preprint (Jaroslawicz et al.), arXiv 2507.11538, July 2025. Abstract page plus search-result snippets, via summarising tools. Synthetic setting, not agentic coding.

- Benchmark of 500 keyword-inclusion instructions inside a business-report writing task; 20 models from 7 providers.
- Best frontier models reached only 68% accuracy at 500 instructions.
- Three decay patterns by model type (search snippet, unverified against the paper): threshold decay for reasoning models, linear decay for models such as gpt-4.1 and claude-sonnet-4, exponential decay for smaller or older models. Models show bias toward earlier instructions.
- Relevance: general evidence that adherence falls as instruction count rises. The instructions are trivial keyword rules, so the numbers do not transfer to an AGENTS.md of a few dozen rules read once per session. Complements [the factorial study](instruction-adherence-config-files-factorial.md), which found no size effect in real Claude Code sessions.
