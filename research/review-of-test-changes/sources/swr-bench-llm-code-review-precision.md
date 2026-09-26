---
source: https://arxiv.org/abs/2509.01494
source_date: 2025-09
researched: 2026-09-26
---

# Zeng et al.: Benchmarking and Studying the LLM-based Code Review (SWR-Bench)

Published as "SWR-Bench: Assessing LLM Performance in Real-World Code Review Comment Generation" (Proc. ACM Softw. Eng. 3, FSE, July 2026; arXiv v2 5 Jun 2026). How it was read this time: PDF of arXiv 2509.01494v2 via pdftotext; abstract, dataset construction and RQ2 (Table 4) read. The figures previously marked unverified are now checked against Table 4.

- Benchmark: 1,000 manually verified GitHub PRs, 500 "Change-PRs" with real issues and 500 "Clean-PRs" (no known defect, checked with SZZ), so any comment on a Clean-PR counts as a false positive. Trivial change types (formatting, docs) filtered out. Evaluation: an LLM checks whether ground-truth issues ("change-actions") are covered, with about 90% agreement with humans.
- Tools tested with Gemini-2.5-Pro, Claude-3.7-Sonnet and DeepSeek-R1: LLM-Review, SWR-Agent, CR-Agent, Hybrid-Review, PR-Review, plus fine-tuned Code-Reviewer and Llama-Reviewer.
- Table 4 mean overall precision: PR-Review 15.39%, LLM-Review 9.22%, SWR-Agent 9.11%, CR-Agent 6.23%, Hybrid-Review 2.79% (fine-tuned models about 4%). The text says four of the tools had precision below 10%. Best single combination: PR-Review with Gemini-2.5-Pro, precision 16.65%, recall 23.18%, F1 19.38% ("only 19.38%"). Some combinations average over 7 false positives per PR. Precision is "hit-based".
- Recall falls sharply as the number of issues per PR grows (38.35% at one issue to 8.88% at five or more); tools do better on functional than "evolutionary" (style, approach) changes; best F1 on logic changes 26.20% for PR-Review.
- Multi-review aggregation: Gemini-2.5-Flash with 10 aggregated runs reached F1 21.91%, a 43.67% relative increase over its own baseline, and recall 30.44%.
- Relevance: LLM reviewers of ordinary PRs, mid-2025 models, have low precision and recall. Not specific to test changes (tests appear only as one example of a solution-approach change), and the models are older than the 2026 tools.
