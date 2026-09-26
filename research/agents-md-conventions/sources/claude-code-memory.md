---
source: https://code.claude.com/docs/en/memory
source_date: undated
researched: 2026-09-26
---

# How Claude Code reads CLAUDE.md

Source line as first recorded: https://code.claude.com/docs/en/memory ("How Claude remembers your project"). Source date: undated; the page mentions versions up to v2.1.281. Researched: 2026-09-26.

Read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere.

- Nature: CLAUDE.md is "context, not enforced configuration"; to block an action use a PreToolUse hook. Loaded at the start of every session and consumes context tokens.
- Size: "target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence." Auto memory (separate mechanism) loads first 200 lines or 25KB.
- Content guidance: keep to facts held every session (build commands, conventions, layout, "always do X"); multi-step procedures or single-area content go to a skill or path-scoped rule. Instructions should be concrete and verifiable; contradictory rules may be resolved arbitrarily.
- Locations (broad to specific, later = read later): managed policy, user `~/.claude/CLAUDE.md`, project `./CLAUDE.md` or `./.claude/CLAUDE.md`, local `./CLAUDE.local.md` (gitignored).
- Precedence/nesting: files from the working directory and every directory above are loaded at launch and "concatenated into context rather than overriding each other", root down, so closest is read last. Subdirectory CLAUDE.md files load on demand when Claude reads files there. `claudeMdExcludes` skips files by glob.
- Imports: `@path/to/file` syntax, relative to the importing file, recursive to a maximum depth of four hops; imported files still load into context at launch. External (outside working directory) imports trigger a one-time approval dialog.
- Block-level HTML comments are stripped before injection (maintainer notes cost no tokens).
- `.claude/rules/*.md`: topic files, recursive; without `paths` frontmatter they load at launch, with `paths` globs they load when matching files are read. Symlinks are supported to share rules across projects; a symlink target outside the working directory is treated as an external import (needs approval).
- `/init`: "generate a starting CLAUDE.md automatically" by analysing the codebase; if one exists it "suggests improvements rather than overwriting". With `CLAUDE_CODE_NEW_INIT=1` it is an interactive flow that can also set up skills and hooks.

AGENTS.md inside Claude Code (same page):
- Claude Code can read `AGENTS.md` directly (requires v2.1.277+). Default setting `claude-md-or-agents-md`: it reads AGENTS.md only if there is no `CLAUDE.md`, `.claude/CLAUDE.md` or `CLAUDE.local.md` in the working directory or above; otherwise CLAUDE.md files only. `claude-md-and-agents-md` loads both.
- Loaded at start: every `AGENTS.md` and `.claude/AGENTS.md` in the working directory and above; subdirectory ones on demand. Not read: `AGENTS.local.md`, `AGENTS.override.md`, anything under `.agents/`.
- Documented interop patterns: a `CLAUDE.md` containing `@AGENTS.md` followed by Claude-specific instructions; or `ln -s AGENTS.md CLAUDE.md`. The page says some sessions (before v2.1.281, e.g. Bedrock or telemetry disabled) read CLAUDE.md only, so the import is needed there.
