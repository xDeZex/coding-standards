---
source: https://arxiv.org/abs/2607.21656
source_date: 2026-07-22
researched: 2026-09-26
---

# Xiang et al.: Cross-Model LLM Code Review (Claude and Codex)

Preprint (arXiv v1, 22 Jul 2026), Agentic SE workshop at KDD '26. How it was read this time: PDF from arxiv.org via pdftotext, read for abstract, method, results, discussion and limitations. The earlier note (abstract page via a summarising tool) said there was no same-model arm; that was wrong.

- Setup: 116 hard and medium LiveCodeBench problems (released after 2025), Claude Opus 4.7 and Codex GPT-5.5, six conditions: both solo baselines, both cross-model orderings, both same-model orderings. The reviewer sees the problem and the draft, cannot execute tests, cannot see hidden tests, and returns a final program. Single review pass, high reasoning effort.
- Results (pass rate): Codex solo 71.6%; reviewed by Claude 89.7% (BH-adjusted p = .001); reviewed by Codex itself 84.5% (p = .022). Claude solo 91.4%; reviewed by Claude itself 91.4% (unchanged; 3 fixes, 3 regressions); reviewed by Codex 82.8% (p = .046; 3 fixes, 13 regressions).
- The direct contrast between the two cross-model orderings does not survive multiple-comparison correction (p_BH = .1444). Claude solo was on the accuracy Pareto frontier; no reviewed condition beat it.
- Authors' limits: single model pair, self-contained competitive programming problems rather than repository patches, static review without execution, sensitivity to prompt wording, models change quickly.
- Relevance: a second model as reviewer helped one draft source and hurt the other; same-model review helped the weaker writer (Codex) and did nothing for the stronger (Claude). The task is generating a corrected program, not judging test changes; the paper does not study tests being weakened and says reviewers could not see the hidden tests and does not describe any test files in the review input.
