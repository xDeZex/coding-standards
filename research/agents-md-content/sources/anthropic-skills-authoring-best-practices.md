---
source: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices
source_date: undated
researched: 2026-09-26
---

# Skill authoring best practices (Anthropic)

First-party documentation. Re-read 2026-09-26 from the raw HTML (curl, html.parser); the quotes below were checked and match. Extends [the skills page](../../agents-md-conventions/sources/claude-code-skills.md).

- "The context window is a public good." Only skill name and description are preloaded; SKILL.md is read when relevant, other files only as needed. Once loaded, every token competes with conversation history.
- Keep SKILL.md body under 500 lines; split into files referenced one level deep (deeper nesting risks partial reads with `head`).
- The description drives selection: Claude picks among potentially 100+ skills from it, so it must say what the skill does and when to use it, in third person.
- Degrees of freedom: use exact scripts (low freedom) when "Operations are fragile and error-prone", "Consistency is critical" or "A specific sequence must be followed"; text guidance where several approaches work. Utility scripts are "more reliable than generated code" and save tokens.
- Feedback loops (run validator, fix, repeat) "greatly improve output quality" (assertion, no data).
- Evaluation-driven development: run the agent without the skill on representative tasks, note failures, build at least three evaluations, write minimal instructions, compare with baseline. It says there is no built-in way to run these evaluations and that "evaluations are your source of truth".
- Not stated: any comparison against putting the same content in an always-loaded file, or any figure for how often skills are invoked.
