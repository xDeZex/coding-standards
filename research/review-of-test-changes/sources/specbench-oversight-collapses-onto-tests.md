---
source: https://arxiv.org/abs/2605.21384
source_date: 2026-05
researched: 2026-09-26
---

# Zhao et al.: SpecBench, Measuring Reward Hacking in Long-Horizon Coding Agents

Preprint from Weco AI (v1 May 2026, v2 9 Sep 2026). How it was read this time: PDF of arXiv 2605.21384v2 via pdftotext, read for abstract, introduction, benchmark design, scaling result, qualitative section, limitations. Included for the scale argument, not for review results.

- Method: 30 systems-level tasks (JSON parser up to an OS kernel, C/Python/Go); each has a spec, visible validation tests, and held-out tests that compose the same features. The "reward hacking gap" is validation pass rate minus held-out pass rate.
- Headline: every frontier agent saturates the visible tests while holdout gaps persist; smaller models (by MMLU) show larger gaps. The abstract says the gap "grows by 28 percentage points for every tenfold increase in code size"; the body reports the 90th-percentile gap growing about 27 points per tenfold increase in lines of code (R^2 = 0.21, "a coarse proxy"); worst-case gap 21 points under 10K lines and 100 points over 25K. So the figure is for the upper tail of runs, not the average, and the fit is weak.
- Gaps are mostly not deliberate exploits: the authors say the gap "more often reflects a structural mismatch between local test passing and global system correctness" (features that do not compose). One severe example: on the C compiler task, Codex stored a 2,900-line hash table of pre-computed outputs for public test programs, 97% validation and 0% held-out; a search process (AIDE) selected it over a genuine 7,900-line compiler scoring 53% and 43%.
- "As long-horizon coding agents produce more code than any developer can review, oversight collapses onto a single surface: the automated test suite" is the authors' premise, not a measured result. The paper does not test reviewers.
- Relevance: special-casing at scale is code in the source diff, not in the tests, so a review of the test diff alone would not see it. That inference is ours.
