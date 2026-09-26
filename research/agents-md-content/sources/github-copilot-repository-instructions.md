---
source: https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions
source_date: undated
researched: 2026-09-26
---

# GitHub Copilot: repository custom instructions

First-party documentation, read via a summarising fetch tool, so wording is not verified verbatim.

- Recommended content: a summary of what the repo does and its languages and frameworks; for "bootstrap, build, test, run, lint, and any other scripted step" the sequence of steps; the main architectural elements with relative paths; steps to replicate CI checks.
- Length: instructions "no longer than 2 pages" and "not task specific".
- Copilot reads `AGENTS.md` files anywhere in the repo (nearest wins), or a single CLAUDE.md or GEMINI.md at the root. Path-specific instructions use `applyTo` globs in frontmatter.
- The summary returned no comparison of skills and instructions; whether the page discusses skills at all was not established.
- So this vendor places test commands in the always-loaded instructions.
