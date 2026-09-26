---
source: https://arxiv.org/abs/2607.27250
source_date: 2026-07
researched: 2026-09-26
---

# Do Context Files Help Coding Agents? A Two-Agent Ablation Study on Real Repositories

Preprint (Prakhar Khatri), arXiv 2607.27250, 28 Jul 2026. Only the abstract page was read (via a summarising fetch tool).

- Claude Code and Codex, 17 real tasks from 3 repositories, 288 runs, graded by gold tests.
- Reported: "Context strategy does not measurably move correctness on either agent (bounded to <=10-15pp via equivalence testing)". A manipulation probe found that context files never turned a near-miss attempt into a pass.
- The author attributes failures to implementation difficulty (feature design, pattern choice, wiring) and not to missing repository knowledge.
- Small sample (17 tasks, 3 repos); single author; not peer reviewed as far as shown. Consistent in direction with [Gloaguen et al.](gloaguen-evaluating-agents-md.md) but with a wide bound.
