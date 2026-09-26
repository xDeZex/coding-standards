---
source: https://blog.fsck.com/2025/10/09/superpowers/
source_date: 2025-10-09
researched: 2026-09-26
---

# Jesse Vincent, "Superpowers: How I'm using coding agents in October 2025" (SessionStart hook)

Speaker: Jesse Vincent (obra), long-time open-source maintainer (created Request Tracker, ran Perl 5 releases, K-9 Mail) and author of Superpowers, a widely installed skills framework for coding agents. Counts as trusted: authored a widely used practice and tool, and writes first-hand about daily agent use. On hooks he says very little on this page; this note records how he uses one, not an opinion on them.

How read: raw HTML via curl and html-to-text, whole page; searched for "hook" (2 hits) and read the surrounding text.

- Install by plugin, then "After you quit and restart claude, you'll see a new injected prompt": a `<session-start-hook><EXTREMELY_IMPORTANT> You have Superpowers. **RIGHT NOW, go read**: @.../skills/getting-started/SKILL.md </EXTREMELY_IMPORTANT></session-start-hook>`. He calls it "the bootstrap that kicks off Superpowers". It teaches Claude "You have skills", to search for skills by running a script, and "If you have a skill to do something, you must use it to do that activity."
- So the hook's job is context injection at session start, used to make sure skills are noticed, rather than blocking or checking anything. The workflow rules themselves (brainstorm, plan, worktree, red/green TDD) live in skills the model reads, not in hooks.
- The page says nothing about failures, cost or when a hook is the wrong tool. (His later episodic-memory post, reported to add a hook that archives conversations at startup, was not read.)
