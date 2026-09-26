---
source: https://arxiv.org/abs/2404.13076
source_date: 2024-04
researched: 2026-09-26
---

# Panickssery, Bowman, Feng: LLM Evaluators Recognize and Favor Their Own Generations

How it was read this time: PDF of arXiv 2404.13076v1 via pdftotext, read for abstract, introduction, setup and headline findings (not every appendix). The arXiv PDF does not state a venue; the earlier "NeurIPS 2024" label is unverified from the pages read.

- Abstract: out of the box, "LLMs such as GPT-4 and Llama 2 have non-trivial accuracy at distinguishing themselves from other LLMs and humans"; "by fine-tuning LLMs, we discover a linear correlation between self-recognition capability and the strength of self-preference bias; using controlled experiments, we show that the causal explanation resists straightforward confounders." (The earlier note said the experiments "suggest" causality; the authors' claim is that the causal explanation resists straightforward confounders.)
- Setup: summarisation (CNN/DailyMail in-domain, XSum out-of-domain); models Llama-2-7b-chat, GPT-3.5, GPT-4; fine-tuning on GPT-3.5 and Llama 2 with 500 examples gives over 90% self-recognition. Self-preference means rating own outputs higher than others' while human annotators consider them equal.
- All three evaluators showed ordering bias in pairwise comparisons; GPT-4 and GPT-3.5 showed self-preference out of the box.
- Limits: summarisation tasks, not code review or test changes. Applying it to "the same model reviews its own agent's diff" is an inference; the paper does not test it. The follow-up arXiv 2504.03846 was not read.
