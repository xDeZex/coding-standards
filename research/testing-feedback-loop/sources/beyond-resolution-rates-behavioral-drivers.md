---
source: https://arxiv.org/abs/2604.02547
source_date: 2026-04-02
researched: 2026-09-26
---

# Beyond Resolution Rates: Behavioral Drivers of Coding Agent Success and Failure

Primary source: arXiv preprint (submitted 2 Apr 2026). Read via the arXiv abstract and HTML page through a summarising fetch tool, not the full PDF; numbers below are as relayed and lightly verified. Observational study of existing benchmark runs, not a controlled experiment.

- Data: 9,374 trajectories from 19 agents (8 frameworks, 14 LLMs) on the same 500 SWE-bench Verified tasks.
- Validation is encoded in trajectories as test run passing (Vp), test run with test failure (Vf), test run with runtime error (Ve), and reproduction scripts (Vr).
- "Validation effort" (share of trajectory spent validating) correlates positively with success across agents: rho = +0.50, p < 0.05. It ranges from 0.1% (Trae/doubao) to 39.3% (Sonar/claude-opus-4.5). One outlier: Trae/doubao reaches 78% resolution with near-zero validation.
- Validation behaviour is agent-determined rather than task-adaptive: strong agents keep roughly 35-37% validation effort across task complexity, weaker agents 12-19%; "agents employ fixed strategies that do not adapt to a given task."
- Abstract-level claim: "agents that gather context before editing and invest in validation succeed more often." Trajectory length's link to failure reverses once task difficulty is controlled (a confound).
- In this benchmark the test run is part of what agents do while working (the harness does not necessarily prompt for it); the study does not examine test editing or deletion.
