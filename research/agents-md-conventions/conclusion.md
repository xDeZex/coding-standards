# Draft: facts relevant to the AGENTS.md and adoption decisions

Carried over from the original single research file (issue #2) when it was split into per-source notes. Facts only, with no conclusions yet; a real position will replace this. Source notes are in [sources](sources/).

Note the difference in mechanism: agents.md describes "nearest file wins"; Codex concatenates with nearer files last.

## 7. Facts relevant to the two pending decisions (facts only)

Hand-written vs generated AGENTS.md template:
- agents.md sets no required fields or headings; nothing in the spec fixes a template.
- Claude Code documents generation of CLAUDE.md by `/init` (analyses the codebase; suggests improvements if a file exists) and calls the output "a starting" file to refine with instructions Claude "wouldn't discover on its own".
- Size guidance that constrains any template: under 200 lines (Claude Code CLAUDE.md), 32 KiB combined (Codex default).
- `@AGENTS.md` import and symlink are the documented ways to keep one shared file across tools.

How an AI adopts a kit into another repo:
- Documented install routes are tool-specific: plugin marketplaces (Claude Code, Cursor, Devin, Gemini, Kimi), copying a skill folder to `.claude/skills/` or `~/.claude/skills/`, symlinking rules into `.claude/rules/`. None of the pages read describe an "AI reads a source repo and proposes a selection for human confirmation" flow; that this exists as a convention is unverified.
- Skills are portable across tools via the Agent Skills spec; CLAUDE.md features (imports, rules `paths`) are Claude Code-specific, while AGENTS.md is plain Markdown.
- Claude Code asks for approval for external imports and out-of-tree symlinks; plugins run code as the user (docs' security note).
- Precedence differs in wording by source: nearest-wins (agents.md), concatenation with nearest last (Codex, Claude Code). Nothing read states that a nearer file can delete a farther file's rule.

## Not verified / gaps
- No dates on any fetched page; source dates are unknown. Version numbers appear only in the Claude Code memory page.
- No AGENTS.md size guidance found on agents.md itself.
- Cursor, Copilot, Gemini CLI, Aider docs on AGENTS.md not read; only agents.md's claim of support.
- agents.md governance charter, the Claude Code plugin components/manifest reference not read.
