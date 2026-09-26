---
source: https://learn.chatgpt.com/guides/best-practices
source_date: undated
researched: 2026-09-26
---

# Codex best practices (OpenAI)

First-party documentation (redirected from developers.openai.com/codex/learn/best-practices, HTTP 308), Re-read 2026-09-26 from the raw HTML of the redirected page (curl, html.parser, in full); quotes below were checked and match. Complements [Codex AGENTS.md](../../agents-md-conventions/sources/codex-agents-md.md).

- A good AGENTS.md covers: repo layout and important directories; how to run the project; "Build, test, and lint commands"; conventions and PR expectations; constraints and do-not rules; "What done means and how to verify work".
- "A short, accurate AGENTS.md is more useful than a long file full of vague rules."
- Grow it from failures: "When Codex makes the same mistake twice, ask it for a retrospective and update AGENTS.md."
- Skills: they package instructions, context and supporting logic; "if you keep reusing the same prompt or correcting the same workflow, it should probably become a skill."
- "Improve reliability with testing and review" section: "That guidance can come from either the prompt or AGENTS.md" on what good testing looks like (tests, right test suites, lint, type checks); skills are not named there. Its list of common mistakes includes "Overloading the prompt with durable rules instead of moving them into AGENTS.md or a skill" and "Not letting the agent see its work by not giving details on how to best run build and test commands". Skills are listed for recurring jobs such as log triage, release notes, PR review against a checklist, migration planning, standard debugging flows.
- Also: "If AGENTS.md starts getting too large, keep the main file concise and reference task-specific markdown files".
- No data cited. This vendor lists build, test and lint commands under AGENTS.md and points skills at repeated workflows.
