---
source: https://arxiv.org/abs/2507.11538
source_date: 2025-07
researched: 2026-09-26
---

# How Many Instructions Can LLMs Follow at Once? (IFScale)

Re-read 2026-09-26: full paper PDF (arxiv.org/pdf/2507.11538, pdftotext), not the abstract page and not search snippets. Synthetic setting, not agentic coding.

Preprint (Jaroslawicz, Whiting, Shah, Maamari; Distyl AI), arXiv 2507.11538v1, 15 Jul 2025.

- Benchmark: business-report writing with keyword-inclusion instructions (each instruction is "include this keyword"), density scaled from 10 to 500 in steps of 10, five runs per level; 20 models from seven providers.
- Best frontier models reach only 68% accuracy at 500 instructions (abstract). Examples at 500: o3 62.8%, grok-3 61.9%, claude-3.7-sonnet 52.7%, claude-opus-4 44.6%, claude-sonnet-4 42.9%.
- Three decay patterns (from the paper's section 4.4 and Figure 1): threshold decay for reasoning models, with near-perfect performance through about 150 or more instructions before declining (gemini-2.5-pro, o3); linear decay; exponential decay for smaller models, levelling off at 7 to 15% accuracy. The paper is internally inconsistent about which Claude model is the linear example: the Figure 1 caption names claude-sonnet-4, the text names claude-3.7-sonnet.
- Bias toward earlier instructions (primacy): measured as the ratio of error rates in the last third to the first third of instructions. It is low at small densities, peaks around 150 to 200 instructions, and falls back toward 1.0 to 1.5 above 300 instructions as models fail more uniformly. So the bias is not monotonic in instruction count.
- Relevance: general evidence that adherence falls as instruction count rises and that near-perfect adherence holds up to about 100 to 150 instructions for the best reasoning models. The instructions are trivial keyword rules in a writing task, so the numbers do not transfer directly to an AGENTS.md. Complements [the factorial study](instruction-adherence-config-files-factorial.md).
