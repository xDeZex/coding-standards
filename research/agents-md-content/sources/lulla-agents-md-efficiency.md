---
source: https://arxiv.org/abs/2601.20404
source_date: 2026-01
researched: 2026-09-26
---

# On the Impact of AGENTS.md Files on the Efficiency of AI Coding Agents

Re-read 2026-09-26: full paper PDF (arxiv.org/pdf/2601.20404, pdftotext, 7 pages), not the abstract page and not a summarising tool. An earlier version of this note, written from a summarising fetch of the abstract page, wrongly said both Codex and Claude Code were run.

Preprint (Lulla, Mohsenimofidi, Galster, Zhang, Baltes, Treude), arXiv 2601.20404, submitted 28 Jan 2026, v2 30 Mar 2026. The paper is a 5-page workshop paper (ICSE JAWs 2026).

- Agent: only OpenAI Codex, model gpt-5.2-codex, through the Codex CLI. The abstract and introduction mention Claude Code as an example of such agents, but it was not run; testing other agents is listed as future work.
- Design: 10 repositories randomly sampled from 26 that have a single root AGENTS.md whose content was classified (by gpt-oss-120b, then manually checked) as covering conventions and best practices, architecture and structure, or project description. Up to 15 merged PRs per repository, 124 in total, each at most 100 changed lines, at most 5 files, code files only, created after the AGENTS.md was introduced. The agent recreated each PR from a pre-merge snapshot, with and without the AGENTS.md, from an issue-style task statement that a local LLM generated from the PR diff. Paired within-task design, isolated Docker containers.
- Results (Table 1, Wilcoxon signed-rank, significant at p < 0.05): median wall-clock time 98.57 s to 70.34 s (down 28.23 s, 28.64%); mean 162.94 s to 129.91 s (20.27%). Median output tokens 2,925 to 2,440 (16.58%); mean output tokens 5,744.81 to 4,591.46 (20.08%). Time and output tokens are the two metrics marked significant. Mean input tokens fell 9.73% and mean total tokens 9.93%, but median input tokens rose 3.41% and median total tokens fell only 1.29%; these were not marked significant. The authors read the larger drop in mean output tokens as AGENTS.md mainly cutting a few very costly runs.
- "Comparable task completion" rests only on a manual sanity check: 50 randomly sampled tasks were inspected to confirm the outputs were non-empty, non-trivial changes consistent with the task. The paper says this is not a correctness evaluation and that output-quality evaluation is future work. So this study does not show that task success was unchanged.
- The filter kept files with conventions, architecture or project description content; testing instructions were not a selection criterion, and the paper does not say what share of the files had them.
- Stated scope: initial step, one agent, small tasks, efficiency only; no analysis of why the files help (traces are future work).
- Differs from [Gloaguen et al.](gloaguen-evaluating-agents-md.md) (cost up over 20%) in agent and model, task construction (issue text generated from the PR diff), filtered file content, metric (time and tokens versus dollar cost and steps) and the fact that this study did not measure success. The reason for the disagreement was not investigated by either paper.
