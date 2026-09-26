---
source: https://arxiv.org/abs/2103.07189
source_date: 2021-03
researched: 2026-09-26
---

# Does mutation testing improve testing practices? (Petrovic, Ivankovic, Fraser, Just, ICSE 2021)

Primary source: peer-reviewed study of Google's mutation testing in code review. How it was read this time: PDF of arXiv 2103.07189 via pdftotext, read for abstract, introduction, RQ1 to RQ3 results and threats.

- Dataset: almost 15 million mutants over six years at Google, mutants shown as findings in code review (to authors and reviewers).
- Design: interventional but "not a fully randomized controlled experiment"; exposure is the number of times mutants were surfaced per file; a line-coverage-surfaced dataset is the baseline. Three alternative hypotheses were rejected.
- RQ1: more exposure, more test hunks changed per file (Spearman 0.9 for mutants; weak negative, -0.24, for the coverage baseline); median 1 changed test hunk per changelist after mutants were reported vs 0 for coverage.
- RQ2: negative correlation between exposure and mutant survival (rs = -0.50); reviewers requested fixes for a decreasing share of reported mutants over time (rs = -0.34).
- RQ3: mutants coupled with 70% of analysed high-priority bugs: mutation testing would have reported a live mutant on the bug-introducing change that a bug-triggering test kills. The abstract's "fewer mutants remain" matches RQ2.
- Weakness for our question: it shows a mutation signal changes cooperative human authors' behaviour and relates to real faults; it does not test mutation score as a guard against tests being weakened, and the developers were not adversarial or agents.
