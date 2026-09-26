---
source: https://sback.it/publications/icse2019a.pdf
source_date: 2019
researched: 2026-09-26
---

# Test-Driven Code Review: An Empirical Study (Spadini, Palomba, Baum, Hanenberg, Bruntink, Bacchelli, ICSE 2019)

Primary source: peer-reviewed controlled experiment. Text read from the PDF (pdftotext) for the abstract and introduction; results sections were not read.

- Test-Driven Code Review (TDR) means the reviewer reads the changed tests before the changed production code.
- Experiment: 92 valid participants (77 with at least two years' professional experience) completed 154 reviews, using TDR or production-first or production-only order. Two external developers rated review comment quality. Follow-up: 9 interviews and a survey of 103 respondents.
- Result: with TDR, developers find "the same proportion of defects in production code, but more in test code, at the expenses of less maintainability issues in production code." Comment quality was rated comparable across strategies.
- Perception: "most developers prefer to review production code as they deem it more important and tests should follow from it"; poor test code quality and no tool support hinder TDR.
- Quotes a Google testing blog author (P. Zembrod): tests "expose interfaces and state use cases", so they answer what a change is supposed to do.
- The study is on Java, human-written changes and seeded defects in an online tool; it says nothing about agent-generated diffs. Its finding that reviewers under-attend to test code is a self-report and an experiment, not a measure of test weakening.
