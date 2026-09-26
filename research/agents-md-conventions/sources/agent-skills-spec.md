---
source: https://agentskills.io/specification
source_date: undated
researched: 2026-09-26
---

# Agent Skills specification

Source line as first recorded: https://agentskills.io/specification. Source date: undated. Researched: 2026-09-26.

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere.

- A skill is a directory with required `SKILL.md` (YAML frontmatter + Markdown) and optional `scripts/`, `references/`, `assets/`.
- Required frontmatter: `name` (1-64 chars, lowercase alphanumerics and hyphens, no leading/trailing/consecutive hyphens, must match directory name) and `description` (1-1024 chars, what it does and when to use it). Optional: `license`, `compatibility` (max 500), `metadata` (string map), `allowed-tools` (experimental).
- Progressive disclosure: metadata (~100 tokens) loaded at startup for all skills; body (<5000 tokens recommended) on activation; resources on demand. "Keep your main SKILL.md under 500 lines." References one level deep. Validator: `skills-ref validate`.
