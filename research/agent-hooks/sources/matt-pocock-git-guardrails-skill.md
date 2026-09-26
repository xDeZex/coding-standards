---
source: https://github.com/mattpocock/skills/blob/main/skills/misc/git-guardrails-claude-code/SKILL.md
source_date: 2026-08-19
researched: 2026-09-26
---

# Matt Pocock, git-guardrails-claude-code and setup-pre-commit skills

Speaker: Matt Pocock, TypeScript educator (Total TypeScript) who publishes an open-source set of agent skills (`mattpocock/skills`, 270,206 GitHub stars on 2026-09-26 per the GitHub API). Counts as trusted: author of a widely used set of agent skills, and other notes in this repo already treat him so. This note records what he ships, not commentary: he wrote no prose I found on hooks (a web search for his views on hooks returned only third-party listings of the skills). The date is the last commit touching the skill directory (GitHub API, 2026-08-19).

How read: `SKILL.md`, `scripts/block-dangerous-git.sh` and the `setup-pre-commit` SKILL.md fetched raw from raw.githubusercontent.com and read in full.

- The skill "Set up Claude Code hooks to block dangerous git commands (push, reset --hard, clean, branch -D, etc.) before they execute." It installs a PreToolUse hook on the Bash tool that blocks: "`git push` (all variants including `--force`)", "`git reset --hard`", "`git clean -f` / `git clean -fd`", "`git branch -D`", "`git checkout .` / `git restore .`".
- The script matches the command text against a list of substrings with `grep -qE` and, on a match, prints "BLOCKED: ... The user has prevented you from doing this." to stderr and `exit 2`. Matching is by text, so it is the best-effort kind of match the vendor guide warns about; the skill does not say so.
- Scope is asked, not assumed: "install for this project only (`.claude/settings.json`) or all projects (`~/.claude/settings.json`)". The skill's verify step pipes a fake `git push origin main` payload into the script and expects exit 2.
- Blocked message says Claude "does not have authority to access these commands", so the agent is told it lacks permission, not asked to work around.
- Alongside it, `setup-pre-commit` sets up a git hook (Husky) with lint-staged (Prettier), type checking and tests. So for commit-time checks he uses a git hook that binds every committer, and for destructive commands he uses an agent hook that binds only the agent. That is a pairing, not a stated rule.

Unverified: nothing here says how well it works; no incidents or failure reports from him. Uses of hooks that he does not ship (formatting, context injection) are not covered.
