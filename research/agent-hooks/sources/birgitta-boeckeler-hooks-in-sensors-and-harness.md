---
source: https://martinfowler.com/articles/sensors-for-coding-agents.html
source_date: 2026-05-27
researched: 2026-09-26
---

# Birgitta Böckeler on hooks, in "Sensors for coding agents" and "Harness engineering for coding agent users"

Speaker: Birgitta Böckeler, Distinguished Engineer at Thoughtworks who writes on martinfowler.com about AI-assisted delivery. Counts as trusted: her guides-and-sensors vocabulary is the one this repo uses, and she publishes sustained first-hand experiments. Hooks are a small part of both articles.

How read: both pages raw via curl and html-to-text, whole page, hook passages read. This replaces the earlier summary-read notes in `research/testing-feedback-loop/sources/` for the hook lines; the quotes below match the raw text. Sensors article dated "27 May 2026"; the harness article "02 April 2026".

- Getting sensors run, in her experiment: "Via a guide - A skill, or a section in AGENTS.md that asks the agent to check the sensors regularly. This is the easiest way, and this is what I mostly did. But, it is also quite unreliable. I had to ask the agents many, many times why it had not run the sensors check a single time, or why it was running tests or linters directly instead of checking the sensors."
- "Via hooks - I imagine there's a way to force this more regularly with hooks, but it needs some consideration which hooks to use. After every file edit is probably a good starting point, but it would have to be monitored if it's too much distraction for the agent." She had not tried it: "I imagine". Her worry is distraction of the agent, the same cost Ronacher and Shrivu describe.
- "Via git hooks - For users who like their agents to do frequent small commits, a pre-commit hook can be a good way to force a sensors check to take place before code even gets into a commit." Elsewhere: "GitLeaks runs as part of the pre-commit hook, I consider it to be a sensor as well, as it will give the agent feedback when it tries to commit (computational)".
- She also tried a custom extension for the Pi harness that asks at startup whether to start a sensors session: "It seems quite promising ... But at the time of writing this, I haven't used the extension enough to tell if it's running more frequently than it would with an instruction in some markdown file."
- Harness article: a table row lists structural tests as "A pre-commit (or coding agent) hook running ArchUnit tests that check for violations of module boundaries" (feedback, computational), and cites Stripe's minions write-up as "pre-push hooks that run relevant linters based on a heuristic".

She reports no hook-specific failures or results; her finding is that an instruction was unreliable, and her hook options are untested suggestions plus git hooks.
