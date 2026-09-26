---
source: https://blakecrosley.com/blog/claude-code-hooks
source_date: 2026-04
researched: 2026-09-26
---

# Blake Crosley, "Claude Code Hooks: Why Each of My 95 Hooks Exists"

Speaker: Blake Crosley, an independent developer who blogs at blakecrosley.com and describes 9 months of hook development on his own infrastructure. Counts as trusted only weakly: a named individual with a long first-hand account, but no authored tool or standard and no outside track record I could check. The page shows "February 08, 2026" as one date and "v2.1.116, April 2026" in the text, so `source_date` is approximate (2026-04).

How read: raw HTML via curl and html-to-text; the first ~9,000 characters read plus searches for the rest.

- Headline: "I built 95 hooks for Claude Code. Every one exists because something went wrong first." "the best hooks come from incidents, not planning."
- Incident hooks: git-safety-guardian (PreToolUse, Bash) exists because "the agent ran `git push --force origin main`" and overwrote three days of commits on a shared branch, with a 4-hour recovery; it pattern-matches the command string ("It doesn't try to understand intent. Simple, deterministic, impossible to bypass through clever prompting"). He counts "8 intercepted force-push attempts across 9 months". recursion-guard (PreToolUse on Task) exists because subagents "spawned infinite children" and burned tokens "at 10x the normal rate"; 23 blocks. blog-quality-gate (Stop) runs his own linter on a modified blog post because a post shipped with passive voice and a dangling footnote.
- Structure: four layers (prevention on PreToolUse, context on SessionStart and UserPromptSubmit, validation on PostToolUse, quality gate on Stop), "Each layer is independent. If a PreToolUse hook fails silently, the Stop hook still catches quality issues." So he plans for a hook failing silently.
- Config: thresholds moved into JSON files "so I could tune behavior without editing bash scripts".

Caveats: "impossible to bypass through clever prompting" is a claim about prompting only; text matching on `git push --force ... main` would not see other spellings, and the vendor guide calls such matching best-effort. His sample settings snippet does not match the documented Claude Code hooks JSON shape (a flat `command` next to `matcher`), which suggests it is illustrative; treat the code as not verified. Counts (8 and 23) are self-reported.
