---
source: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
source_date: undated
researched: 2026-09-26
---

# GitHub Copilot: repository custom instructions

First-party documentation. Re-read 2026-09-26 from the raw HTML (curl, html.parser, in full). The earlier version, from a summarising fetch, presented as the page's recommendations what is actually a prompt the page supplies for asking the Copilot cloud agent to generate a copilot-instructions.md.

- The page's opening line: repository custom instructions give Copilot "additional context on how to understand your project and how to build, test and validate its changes".
- The specific content and length guidance is inside the prompt the page tells you to paste into the Copilot cloud agent to generate `.github/copilot-instructions.md` (the Limitations block: "Instructions must be no longer than 2 pages." "Instructions must not be task specific."; the build block: "For each of bootstrap, build, test, run, lint, and any other scripted step, document the sequence of steps ...", "Run the tests and document the order of steps required to run the tests"; plus the main architectural elements with relative paths and steps to replicate CI checks). The section "Writing your own copilot-instructions.md file" has no such list. So these are generator-prompt instructions, not a stated rule for human authors.
- Copilot reads `AGENTS.md` files anywhere in the repo (nearest wins), or a single CLAUDE.md or GEMINI.md at the root. Path-specific instructions use `applyTo` globs in frontmatter.
- Skills: the only mention on this page is that Copilot code review reads repository instructions, agent instructions and agent skills from the head branch. It gives no guidance on choosing between instructions and skills.
- So the page's generator prompt asks for test steps in the always-loaded copilot-instructions.md; the page does not state a placement rule.
