---
source: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
source_date: 2025-10-16
researched: 2026-09-26
---

# Equipping agents for the real world with Agent Skills (Anthropic engineering)

First-party post by Barry Zhang, Keith Lazuka and Mahesh Murag, 16 Oct 2025 (with an update note of 18 Dec 2025 that Agent Skills were published as an open standard). Re-read 2026-09-26 from the raw HTML (curl, html.parser); the quotes below were checked against the page text and match.

- Progressive disclosure in three levels: names and descriptions first, "without loading all of it into context"; the full SKILL.md when the agent judges the skill relevant; bundled files "only as needed". Analogy: "a well-organized manual that starts with a table of contents, then specific chapters, and finally a detailed appendix".
- "Pay special attention to the name and description of your skill", used to decide whether to trigger it.
- Suggests finding gaps by running agents on representative tasks and watching where they struggle or need extra context.
- Also: the name and description of every installed skill are pre-loaded into the system prompt at startup; skills can bundle scripts Claude runs without loading the script into context because "code is deterministic".
- No trigger-rate data anywhere on the page, and no comparison with CLAUDE.md placement or any statement about where test commands go.
