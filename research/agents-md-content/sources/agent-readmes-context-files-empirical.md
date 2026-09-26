---
source: https://arxiv.org/abs/2511.12884
source_date: 2025-11
researched: 2026-09-26
---

# Agent READMEs: An Empirical Study of Context Files for Agentic Coding

Re-read 2026-09-26: full paper PDF (arxiv.org/pdf/2511.12884, v2 dated 9 Aug 2026, pdftotext), not the abstract page. First version November 2025. Descriptive, not an effectiveness study.

- 2,303 context files from 1,925 repositories: 922 Claude Code files (CLAUDE.md), 694 Codex files (AGENTS.md) and 687 GitHub Copilot files (copilot-instructions.md), from repositories with at least 5 stars.
- Testing instructions appeared in 75.9% of files (the paper's own text: "the most prevalent category", "procedures and commands for executing automated tests"), implementation details 70.8%, architecture 68.1%; performance 14.5% and security 14.8%. The classification into 16 instruction types was done by an automatic classifier (reported F1 0.79 for concrete topics such as Testing and Architecture), so the percentages carry classifier error.
- Files behave like configuration code, changed in frequent small increments; the paper also finds them hard to read.
- Relevance: running-tests instructions are the most common content of real context files. It says nothing about whether that practice works better or worse than other placements.
