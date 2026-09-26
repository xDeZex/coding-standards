---
source: https://arxiv.org/abs/2510.15061
source_date: 2025-10
researched: 2026-09-26
---

# Antislop: Identifying and Eliminating Repetitive Patterns in Language Models

- Authors: Paech, Roush, Goldfeder, Shwartz-Ziv. Defines "slop" as characteristic repetitive LLM phraseology that makes text recognisable and degrades quality.
- Some patterns are over 1,000x more frequent in LLM output than in human text.
- Three tools: an inference-time sampler that backtracks to suppress strings (8,000+ patterns), a pipeline that profiles model-specific slop against human baselines, and Final Token Preference Optimization (FTPO), a token-level fine-tune.
- Reports FTPO cuts slop about 90% while holding GSM8K, MMLU and creative-writing performance; reports DPO degraded writing quality despite weaker suppression.
- Author Samuel Paech also runs EQ-Bench (see the eqbench source note); a possible conflict of interest is noted, not verified.
- Read through the arXiv abstract page via a page-to-Markdown summariser; the full paper was not read, so numbers below are the abstract-level claims only.
