---
source: https://learn.chatgpt.com/docs/agent-configuration/agents-md
source_date: undated
researched: 2026-09-26
---

# How Codex reads AGENTS.md

Source line as first recorded: OpenAI Codex docs, https://learn.chatgpt.com/docs/agent-configuration/agents-md (redirected from developers.openai.com/codex/guides/agents-md, HTTP 308). Source date: undated. Researched: 2026-09-26.

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere.

- Global: reads `AGENTS.override.md` in Codex home if present, otherwise `AGENTS.md`; first non-empty file only.
- Project: walks from project root toward the working directory; per directory checks `AGENTS.override.md`, then `AGENTS.md`, then configured fallback filenames; at most one file per directory.
- Merge: "Codex concatenates files from the root down, joining them with blank lines"; files nearer the working directory come later so take precedence.
- Size: stops adding files once combined size reaches `project_doc_max_bytes` (32 KiB default).
- `project_doc_fallback_filenames` lets other names (e.g. `TEAM_GUIDE.md`) be read.
