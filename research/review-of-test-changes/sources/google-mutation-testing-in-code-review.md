---
source: https://research.google/pubs/state-of-mutation-testing-at-google/
source_date: 2018
researched: 2026-09-26
---

# State of Mutation Testing at Google (Petrovic and Ivankovic, ICSE-SEIP 2018)

Primary source: Google paper. How it was read this time: the research.google page via curl (abstract), plus the full paper PDF (storage.googleapis.com link from that page) via pdftotext, full text.

- Mutation testing "assesses test suite efficacy by inserting small faults into programs and measuring the ability of the test suite to detect them"; classic analysis is computationally prohibitive.
- Approach: diff-based and probabilistic; at most one mutant per line; drops lines without statement coverage and "arid" lines (for example log statements); heuristic per language, refined from developer "Not useful" clicks. Mutants surface in the code review tool as findings with "Please fix" and "Not useful" links, to author and reviewers.
- Scale: abstract says used by 6,000 engineers on all changes they author or review; the research.google abstract says "more than 14,000 code authors", the paper PDF says "more than 13,000" (a version discrepancy); about 30% of all diffs with statement coverage processed.
- Evaluation in the body: more than 70,000 diffs, 1.1 million mutants, 150,000 actionable findings surfaced in review; reported usefulness of surfaced results rose from 20% to 80% with the feedback loop; 75% of findings with feedback were marked useful; median 2 living mutants per diff (99th percentile 43). "Usefulness" is developer-reported.
- The system is a review-integrated signal about missed faults in new code. It is not about detecting weakened existing tests, and the paper does not test that.
