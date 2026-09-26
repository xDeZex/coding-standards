---
source: https://arxiv.org/abs/2604.04323
source_date: 2026-04
researched: 2026-09-26
---

# How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings

Preprint (Liu, Ji, An, Jaakkola, Zhang, Chang), arXiv 2604.04323, 6 Apr 2026. Abstract page only, via a summarising fetch tool.

- With a pool of 34,000 real-world skills, the gains from skills shrink as the setting becomes more realistic (agent must find and choose skills itself); in the hardest condition performance falls to about the level of no skills.
- Query-specific refinement of skills recovers much of the loss when the starting skills are reasonably relevant; one reported effect is Claude Opus 4.6 on Terminal-Bench 2.0 from 57.7% to 65.5%.
- Relevance: an independent finding that skill benefit depends on the agent selecting and loading the right skill, in line with the low invocation rate in [Vercel](vercel-agents-md-outperforms-skills.md). The pool size (34,000) is far from a single-repo setup with a few skills.
