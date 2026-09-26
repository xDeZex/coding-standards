---
source: https://research.google.com/pubs/archive/46584.pdf
source_date: 2018-05-27
researched: 2026-09-26
---

# Petrovic and Ivankovic, "State of Mutation Testing at Google" (ICSE-SEIP 2018)

Reading method: re-read 2026-09-26, all 9 pages, via pdftotext -layout of the PDF (two-column layout, so passages were read with some interleaving). Peer-reviewed, first-party industry paper (ICSE-SEIP 2018, Gothenburg, 27 May to 3 June 2018).

- Premise: "coverage alone might be misleading, as in many cases where statements are covered but their consequences not asserted upon." Mutation testing inserts small faults and measures whether the suite detects them; mutation score is killed mutants over total mutants. It is described as widely considered the strongest test-adequacy measure, and the paper cites work correlating mutant detection with detecting real faults.
- Cost: "At present it is infeasably expensive to compute the absolute mutation score for the codebase at any given fixed point" (repository about two billion lines; about 40,000 changes committed per workday); they run it per code-review diff instead, on lines that are covered and not "arid" (logging and similar), at most one mutant per line.
- Scale and result: abstract says more than 70,000 diffs, 1.1 million mutants, 150,000 actionable findings surfaced in code review; "the reported usefulness of the surfaced results improved from 20% to 80%" using the developer feedback loop (one-click "not useful"). Section 5: 72,425 diffs, 1,159,723 mutants, 150,854 actionable results, of which 11,049 got developer feedback; the conclusion says 75% of surfaced findings with feedback were reported useful. Used by 6,000 engineers on all changes they author or review, processing about 30% of diffs that have statement coverage.
- Survival: over 87% of test runs over mutants fail (kill the mutant); the paper says this is not the mutation score, because only a probabilistic subset of mutants is generated. Survival by language ranged from 1.0% (Common Lisp) to 14.7% (Python).
- Placement claim: they argue code review is the best place to surface such results because it maximises the chance the change is acted on, and non-actionable findings there hurt.
- Relevance: mutation testing is the standard tool for asking whether tests would still catch a fault, which a pass/fail hook cannot. It is expensive and was placed in review, not in a per-edit gate. Nothing here tests it against agent-written or agent-weakened tests; applying it to that is our extension. Later results pages were not read.
