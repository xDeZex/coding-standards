---
source: https://www.microsoft.com/en-us/research/publication/expectations-outcomes-and-challenges-of-modern-code-review/
source_date: 2013-05
researched: 2026-09-26
---

# Expectations, Outcomes, and Challenges of Modern Code Review (Bacchelli and Bird, ICSE 2013)

Primary source: peer-reviewed study at Microsoft (observation, interviews, survey, manual classification of hundreds of review comments). Only a search-result summary was read, not the paper.

- Finding defects is the main stated motivation, but review is less about defects than expected; it also delivers knowledge transfer, team awareness and alternative solutions.
- Understanding the code and the change is the central activity, and it takes most of the review time; current tools mostly do not meet that understanding need.
- Scheduling and time pressure are challenges.
- Relevance: this is the general baseline that review is weaker at defect finding than assumed and depends on reviewer understanding. It is from 2013 and human-authored changes; applying it to tests and agent diffs is our extension.
