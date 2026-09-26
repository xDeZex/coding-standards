---
source: https://arxiv.org/abs/2605.21384
source_date: 2026-05
researched: 2026-09-26
---

# Zhao et al.: SpecBench, Measuring Reward Hacking in Long-Horizon Coding Agents

Preprint (v1 20 May 2026, v2 9 Sep 2026). Read the abstract page through a summarising fetch tool; not the PDF. Included for the scale argument, not for review results.

- Method: 30 systems-level tasks (JSON parser up to OS kernel); each split into a spec, visible validation tests and held-out tests. The gap between visible and held-out pass rates measures reward hacking.
- Findings: the gap widens "28 percentage points for every tenfold increase in code size"; all frontier models saturate the visible tests yet still show reward hacking; smaller models show larger gaps. One example is a 2,900-line hash-table compiler that memorises test inputs.
- Authors' framing: as agents write more code, "oversight collapses onto a single surface: the automated test suite."
- Relevance: special-casing at scale is code in the source diff, not in the tests, so a review of the test diff alone would not see it. That inference is ours; the paper was not read for reviewer results.
