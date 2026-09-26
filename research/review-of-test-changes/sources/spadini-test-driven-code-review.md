---
source: https://sback.it/publications/icse2019a.pdf
source_date: 2019
researched: 2026-09-26
---

# Test-Driven Code Review: An Empirical Study (Spadini, Palomba, Baum, Hanenberg, Bruntink, Bacchelli, ICSE 2019)

Primary source: peer-reviewed controlled experiment. How it was read this time: sback.it returns HTTP 403 to curl; the same PDF was fetched from an archive.org copy and read via pdftotext (methodology, results, discussion, threats).

- Test-Driven Code Review (TDR): the reviewer reads the changed tests before the changed production code.
- Experiment: 92 valid participants (77 with at least two years of professional experience; the abstract of this version says 93 developers and "more than 150 reviews") completed 154 reviews in an online tool, Java, seeded bugs and maintainability issues, treatments test-first (TF), production-first (PF), production-only (OP). Two external raters, blind to treatment, rated comment quality. Follow-up: 9 interviews and a survey with 103 respondents.
- Results: average proportion of test-code bugs found 0.40 (TF) vs 0.17 (PF); production maintainability issues 0.08 (TF) vs 0.21 (PF) and 0.18 (OP); production bugs and test maintainability issues found are stable across treatments (p > 0.38). Review time did not differ. No significant difference in rated comment quality across treatments.
- Perception: most developers prefer production first, seeing it as more important; poor test code quality and no tool support hinder TDR. Survey adoption (103 respondents): 5% always start from test code, 13% almost always, 42% occasionally, 27% almost never, 13% never.
- Quotes P. Zembrod (Google testing blog): tests "expose interfaces and state use cases".
- Java, human-written changes, seeded defects, an online tool; nothing on agent diffs. Its finding that reviewers give less attention to test code is self-report plus experiment, not a measure of test weakening.
