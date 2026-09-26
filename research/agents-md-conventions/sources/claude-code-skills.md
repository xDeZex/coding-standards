---
source: https://code.claude.com/docs/en/skills
source_date: undated
researched: 2026-09-26
---

# Claude Code skills

Source line as first recorded: https://code.claude.com/docs/en/skills. Source date: undated. Researched: 2026-09-26.

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere.

- Follows the Agent Skills open standard, "which works across multiple AI tools", with Claude Code extensions (invocation control, `context: fork`, `paths`, dynamic context). Claude Code ignores unrecognised fields, but "if you include any field the spec doesn't allow, packaging or upload fails with a hard error."
- Locations: enterprise, personal `~/.claude/skills/`, project `.claude/skills/`, nested `<subdir>/.claude/skills/`, plugin, claude.ai. Name collisions: enterprise over personal over project. Skills are discovered from the start directory up to the repo root; nested ones load when Claude reads a file in that subdirectory. Changes are picked up live.
- Contrast stated by the docs: a skill body loads only when used, unlike CLAUDE.md content.
