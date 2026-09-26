---
source: https://claude.dev/blog/lessons-from-building-claude-code-how-we-use-skills/
source_date: 2026-06-03
researched: 2026-09-26
---

# Thariq Shihipar, "Lessons from building Claude Code: How we use skills" (hook passages only)

Speaker: Thariq Shihipar, member of technical staff on the Claude Code team at Anthropic (byline "Thariq Shihipar", published Jun 03, 2026). Counts as trusted: works on the tool, writes from hundreds of skills used internally. Vendor voice; hooks are a side topic of a post about skills.

How read: raw HTML fetched with curl, converted to text, whole page read; only the hook lines are recorded.

- On-demand hooks: "Skills can include hooks that are only activated when the skill is called, and that only last for the duration of the session. Use this for more opinionated hooks that you don't want to run all the time, but are extremely useful sometimes." (The page's example following this was not recorded in the text I extracted beyond the heading "Use on-demand hooks".)
- Measurement: "To understand how a skill is doing, we use a PreToolUse hook that lets us log skill usage within the company (example code here). This means we can find skills that are popular or are undertriggering compared to our expectations." So a hook is used for observability, not blocking.
- Code-quality skills: "These are skills that enforce code quality inside of your org and help review code. These can include deterministic scripts or tools for maximum robustness. You may want to run these skills automatically as part of hooks or inside of a GitHub Action." Hooks and a GitHub Action are named as alternatives for running the same check.
- The post lists a skill "signup-flow-driver" with "hooks for asserting state at each step".

Nothing on failures or when not to use a hook. It does place opinionated, situational hooks inside a skill so that they are scoped to a task, rather than always on.
