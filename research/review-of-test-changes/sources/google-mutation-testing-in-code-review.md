---
source: https://research.google/pubs/state-of-mutation-testing-at-google/
source_date: 2018
researched: 2026-09-26
---

# State of Mutation Testing at Google (Petrovic and Ivankovic, ICSE-SEIP 2018)

Primary source: Google paper; abstract read in full, body not read.

- Mutation testing "assesses test suite efficacy by inserting small faults into programs and measuring the ability of the test suite to detect them"; classic mutation analysis is computationally prohibitive.
- Approach: diff-based and probabilistic; drops lines without statement coverage and "arid" lines, so far fewer mutants are made, and "we make it easier for humans to understand and evaluate the result of mutation analysis."
- It "focus[es] on a code-review based approach": surviving mutants appear to the author and reviewer inside the mandatory review, and the paper considers "the effects of surfacing mutation results on developer attention."
- Scale: used by 6,000 engineers on all changes they author or review, affecting more than 14,000 authors; processes about 30% of all diffs that have statement coverage.
- This is the clearest primary example of a computational signal shown to a human reviewer. It is about missed faults in new code, not about detecting weakened existing tests, and the abstract gives no usefulness figures.
