---
source: https://arxiv.org/abs/2601.20404
source_date: 2026-01
researched: 2026-09-26
---

# On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents

Preprint (Lulla, Mohsenimofidi, Galster, Zhang, Baltes, Treude), arXiv 2601.20404, submitted 28 Jan 2026, revised 30 Mar 2026. Only the abstract page was read (via a summarising fetch tool); the method details below are from that summary.

- 10 repositories and 124 pull requests, run with and without an AGENTS.md, with Codex and Claude Code as the agents.
- Reported: AGENTS.md present is associated with a lower median runtime (down 28.64%) and lower median output tokens (down 16.58%), "while maintaining comparable task completion rates."
- This points the opposite way from the cost result in [Gloaguen et al.](gloaguen-evaluating-agents-md.md) (cost up over 20%). The two differ in sample (10 repos, 124 PRs versus 138 plus SWE-bench instances), metric (wall-clock and output tokens versus dollar cost and steps) and setup. The reason for the disagreement was not investigated here.
- Not read: how tasks were chosen, how correctness was judged, what the files contained. Whether the result covers test instructions is unknown.
