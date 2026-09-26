---
source: https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/
source_date: 2013-05
researched: 2026-09-26
---

# Expectations, Outcomes, and Challenges of Modern Code Review (Bacchelli and Bird, ICSE 2013)

Primary source: peer-reviewed study at Microsoft. How it was read this time: the Microsoft page was fetched with curl and read (abstract only); the paper PDF on microsoft.com returned an HTML bot-block page, so the full text was read from an archive.org copy of that PDF (pdftotext, read for the introduction, results and challenges sections).

- Method (paper): observed 17 developers across 16 product teams, interviewed them, manually classified 570 review comments (CodeFlow), and surveyed 165 managers and 873 programmers.
- Finding defects is the top stated motivation (first motivation for 383 of the surveyed programmers, 44%), but "the practice and the actual outcomes are less about finding errors than expected". In the 570 comments, "code improvements" are most frequent (165, 29%); "defect" is only fourth of nine categories, 78 comments (14%), "mostly address 'micro' level and superficial concerns" (mostly uncomplicated logic errors). Other benefits: knowledge transfer, team awareness, alternative solutions.
- Understanding is the central challenge: "no other code review challenge emerged as clearly as understanding the submitted change". Scheduling and time issues also appeared challenging, but the authors "could always trace them back to the first challenge" (understanding). A tester is quoted: "understanding the code takes most of the review time"; current tools mostly do not meet the understanding need.
- Correction to the earlier note: time pressure is not a separate finding; the paper folds it into the understanding challenge.
- Relevance: general baseline that review finds fewer defects than assumed and depends on reviewer understanding. 2013, human-authored changes, Microsoft only; applying it to tests and agent diffs is our extension. The paper does not distinguish test files.
