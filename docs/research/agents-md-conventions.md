# Research: conventions for AGENTS.md, CLAUDE.md and shared instruction kits

Issue: xDeZex/coding-standards#2. Researched: 2026-09-26. Vocabulary follows `CONTEXT.md`.

Source-date note: the fetched documentation pages carry no publication date. Where a page states a version, it is recorded; otherwise the source date is "undated (live docs, read 2026-09-26)". Content was read through a fetch tool that summarises pages, so quotes are as returned by that tool; re-check exact wording before quoting elsewhere.

## 1. AGENTS.md (agents.md)

Source: https://agents.md (site). Source date: undated. Researched: 2026-09-26.

- Format: "a simple, open format for guiding coding agents"; standard Markdown, no required fields; "use any headings you like; the agent simply parses the text you provide." Common sections listed: project overview, build/test commands, code style, security.
- Purpose: "a dedicated, predictable place to provide the context and instructions"; README is "for humans", AGENTS.md is for agents.
- Nesting/precedence: for monorepos, "place another AGENTS.md inside each package. Agents automatically read the nearest file in the directory tree, so the closest one takes precedence." Also: explicit user chat prompts override everything.
- Size: the site gives no size limit or recommendation (as fetched). Unverified whether one exists elsewhere on the site.
- Adoption claims: "over 25 agents" support it (Codex, Jules, Cursor, Copilot, VS Code, Devin, Aider, Zed, Warp) and "over 60k open-source projects" use it. These are the site's own claims, not independently verified.
- FAQ: agents will try to run test commands listed; file is "living documentation"; legacy migration via symbolic links; example config for Aider and Gemini CLI.

Source: https://github.com/agentsmd/agents.md (repo README). Source date: undated; commit dates not visible in fetch. Researched: 2026-09-26.
- MIT licence; references a `Technical_Charter.pdf` (governance details not read; unverified). Repo shows 38 commits, 24.6k stars at fetch time. The repo's own `AGENTS.md` is the example, with sections "Dev environment tips", "Testing instructions", "PR instructions".

## 2. How Codex reads AGENTS.md

Source: OpenAI Codex docs, https://learn.chatgpt.com/docs/agent-configuration/agents-md (redirected from developers.openai.com/codex/guides/agents-md, HTTP 308). Source date: undated. Researched: 2026-09-26.

- Global: reads `AGENTS.override.md` in Codex home if present, otherwise `AGENTS.md`; first non-empty file only.
- Project: walks from project root toward the working directory; per directory checks `AGENTS.override.md`, then `AGENTS.md`, then configured fallback filenames; at most one file per directory.
- Merge: "Codex concatenates files from the root down, joining them with blank lines"; files nearer the working directory come later so take precedence.
- Size: stops adding files once combined size reaches `project_doc_max_bytes` (32 KiB default).
- `project_doc_fallback_filenames` lets other names (e.g. `TEAM_GUIDE.md`) be read.

Note the difference in mechanism: agents.md describes "nearest file wins"; Codex concatenates with nearer files last.

## 3. How Claude Code reads CLAUDE.md

Source: https://code.claude.com/docs/en/memory ("How Claude remembers your project"). Source date: undated; the page mentions versions up to v2.1.281. Researched: 2026-09-26.

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

## 4. Skills (Agent Skills standard and Claude Code)

Source: https://agentskills.io/specification. Source date: undated. Researched: 2026-09-26.
- A skill is a directory with required `SKILL.md` (YAML frontmatter + Markdown) and optional `scripts/`, `references/`, `assets/`.
- Required frontmatter: `name` (1-64 chars, lowercase alphanumerics and hyphens, no leading/trailing/consecutive hyphens, must match directory name) and `description` (1-1024 chars, what it does and when to use it). Optional: `license`, `compatibility` (max 500), `metadata` (string map), `allowed-tools` (experimental).
- Progressive disclosure: metadata (~100 tokens) loaded at startup for all skills; body (<5000 tokens recommended) on activation; resources on demand. "Keep your main SKILL.md under 500 lines." References one level deep. Validator: `skills-ref validate`.

Source: https://code.claude.com/docs/en/skills. Source date: undated. Researched: 2026-09-26.
- Follows the Agent Skills open standard, "which works across multiple AI tools", with Claude Code extensions (invocation control, `context: fork`, `paths`, dynamic context). Claude Code ignores unrecognised fields, but "if you include any field the spec doesn't allow, packaging or upload fails with a hard error."
- Locations: enterprise, personal `~/.claude/skills/`, project `.claude/skills/`, nested `<subdir>/.claude/skills/`, plugin, claude.ai. Name collisions: enterprise over personal over project. Skills are discovered from the start directory up to the repo root; nested ones load when Claude reads a file in that subdirectory. Changes are picked up live.
- Contrast stated by the docs: a skill body loads only when used, unlike CLAUDE.md content.

## 5. Subagents

Source: https://code.claude.com/docs/en/sub-agents. Source date: undated. Researched: 2026-09-26.
- Markdown file with YAML frontmatter; only `name` and `description` required; body is the system prompt. Locations by priority: managed settings, `--agents` flag, `.claude/agents/`, `~/.claude/agents/`, plugin `agents/`.
- Non-fork subagents load the CLAUDE.md hierarchy (including AGENTS.md loaded as project instructions) unless `omitClaudeMd: true`; built-in Explore and Plan skip it.
- Plugin subagents ignore `hooks`, `mcpServers`, `permissionMode`.

## 6. How published kits package themselves

Source: https://code.claude.com/docs/en/plugins (plugin overview). Source date: undated. Researched: 2026-09-26.
- A plugin is "a directory of skills, agents, hooks, MCP servers, or other components that Claude Code installs and loads as one unit"; manifest at `.claude-plugin/plugin.json`. Distributed via a marketplace: a repo with `.claude-plugin/marketplace.json` listing plugins; installed by name (`plugin@marketplace`) at user, project or local scope.
- Stated trade-offs: an enabled plugin's skill/agent names and descriptions sit in context every turn (token cost); MCP servers and hooks run in every session; "what the plugin runs, it runs as you". Skills, subagents, hooks and MCP servers also work standalone without a plugin; the docs say to use a plugin when you want several packaged as one unit with versioned updates.
- The overview lists no component type for CLAUDE.md or AGENTS.md content (unverified beyond the page read; the components page was not fetched).

Source: https://github.com/anthropics/skills (README). Source date: undated. Researched: 2026-09-26.
- Layout: `skills/` (examples), `spec/` (Agent Skills specification), `template/` (skill template). A skill is "a folder with a SKILL.md file". Installed as a Claude Code plugin marketplace (`/plugin marketplace add anthropics/skills`, then `/plugin install document-skills@anthropic-agent-skills`), or on claude.ai and the API. Licence: many Apache 2.0; document skills source-available; "for demonstration and educational purposes only".

Source: https://github.com/obra/superpowers (README; third-party collection). Source date: undated. Researched: 2026-09-26.
- Layout: `skills/` plus per-harness plugin directories (`.claude-plugin`, `.codex-plugin`, `.cursor-plugin`, `.agents/plugins`), `docs/`, `scripts/`. Install is per tool: Claude Code marketplace, Cursor `/add-plugin`, Devin `devin plugins install obra/superpowers`, Gemini `gemini extensions install <url>`, Kimi `/plugins install`. Self-described as skills that "trigger automatically".

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
