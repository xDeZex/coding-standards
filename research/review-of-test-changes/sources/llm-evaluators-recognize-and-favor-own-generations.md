---
source: https://arxiv.org/abs/2404.13076
source_date: 2024-04
researched: 2026-09-26
---

# Panickssery, Bowman, Feng: LLM Evaluators Recognize and Favor Their Own Generations

Primary source: NeurIPS 2024 paper. Read as the arXiv abstract page through a summarising fetch tool; numbers not extracted.

- Models such as GPT-4 and Llama 2 have "non-trivial accuracy at distinguishing themselves from other LLMs and humans" out of the box; fine-tuning raises it.
- Finding: "a linear correlation between self-recognition capability and the strength of self-preference bias"; controlled experiments suggest the link is causal.
- Self-preference means rating own outputs higher than others' even when human judges rate them equal.
- Evidence limits: tasks were summarisation and similar text tasks (per the abstract), not code review or test changes. Applying it to "the same model reviews its own agent's diff" is an inference; the paper does not test it. A follow-up (arXiv 2504.03846, "Do LLM Evaluators Prefer Themselves for a Reason?") appeared in search results and was not read.
