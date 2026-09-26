---
source: https://research.google.com/pubs/archive/46584.pdf
source_date: 2018-05-27
researched: 2026-09-26
---

# Petrovic and Ivankovic, "State of Mutation Testing at Google" (ICSE-SEIP 2018)

Reading method: first three pages of the PDF read directly (abstract, introduction, background, method start); results and later sections not read. Peer-reviewed, first-party industry paper.

- Premise: "coverage alone might be misleading, as in many cases where statements are covered but their consequences not asserted upon." Mutation testing inserts small faults and measures whether the suite detects them; mutation score is killed mutants over total mutants. It is described as widely considered the strongest test-adequacy measure, and the paper cites work correlating mutant detection with detecting real faults.
- Cost: computing a full mutation score for Google's roughly 2 billion line repository, at any fixed point, is infeasible; they run it per code-review diff instead, on lines that are covered and not "arid" (logging and similar), at most one mutant per line.
- Scale and result: over 70,000 diffs, 1.1 million mutants tested, 150,000 actionable findings surfaced in review; reported usefulness of surfaced results rose from 20% to 80% via a developer "not useful" feedback loop. Used by 6,000 engineers.
- Placement claim: they argue code review is the best place to surface such results because it maximises the chance the change is acted on, and non-actionable findings there hurt.
- Relevance: mutation testing is the standard tool for asking whether tests would still catch a fault, which a pass/fail hook cannot. It is expensive and was placed in review, not in a per-edit gate. Nothing here tests it against agent-written or agent-weakened tests; applying it to that is our extension. Later results pages were not read.
