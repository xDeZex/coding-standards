---
source: https://arxiv.org/abs/2604.04323
source_date: 2026-04
researched: 2026-09-26
---

# How Well Do Agentic Skills Work in the Wild: Benchmarking LLM Skill Usage in Realistic Settings

Re-read 2026-09-26: full paper PDF (arxiv.org/pdf/2604.04323, pdftotext), not the abstract page.

Preprint (Liu, Ji, An, Jaakkola, Zhang, Chang; UC Santa Barbara, MIT), arXiv 2604.04323v1, 6 Apr 2026, "Under review".

- Skill pool: 34,198 real skills from open-source repositories; 84 SkillsBench tasks, three runs each; models Claude Opus 4.6 (Claude Code), Kimi K2.5, Qwen3.5-397B.
- Progressive settings, Claude Opus 4.6 pass rates: force-loaded curated skills 55.4%; curated skills available and the agent decides 51.2%; curated plus distractor skills 43.5%; retrieval from the pool with curated skills in it 40.1%; retrieval from the pool without curated skills 38.4% (no-skills baseline 35.4%). Kimi and Qwen fell below their no-skills baselines in the last setting (19.8% versus 21.8%; 19.7% versus 20.5%).
- Loading behaviour (Claude): even with curated skills directly available, only 62.2% of trajectories loaded any skill and 49% loaded all curated skills, falling to 31% with distractors; the authors say agents struggle to recognise relevant skills from names and descriptions alone. Kimi loaded skills far more often (86%) without better results, so loading is harness dependent and is not the same as using the content well.
- Refinement: query-specific refinement recovered much of the loss when retrieved skills were reasonably relevant (Claude 40.1% to 48.2%). On Terminal-Bench 2.0, Claude Opus 4.6 went from 57.7% (no skills) to 61.4% (retrieved skills) to 65.5% (query-specific refinement); the abstract's "57.7% to 65.5%" therefore combines retrieval and refinement.
- Relevance: an independent measurement that a skill helps only if the agent loads it, in line with the low invocation rate in [Vercel](vercel-agents-md-outperforms-skills.md). The 34k pool is far from a single repository with a few skills, but the selection failure (51.2% versus 55.4%) also appears with the curated skills directly available.
