---
source: https://martinfowler.com/articles/sensors-for-coding-agents.html
source_date: 2026-05-27
researched: 2026-09-26
---

# Birgitta Böckeler, Maintainability sensors for coding agents (martinfowler.com)

Read in full via curl and html-to-text (raw page, 42,000 characters); the passages on hooks were read closely, the rest skimmed. This re-checks the earlier note [boeckeler-sensors-for-coding-agents](../../testing-feedback-loop/sources/boeckeler-sensors-for-coding-agents.md), whose quotes were from a summarised fetch. The page dates the piece "27 May 2026".

Speaker: Birgitta Böckeler, "a Distinguished Engineer and AI-assisted delivery expert at Thoughtworks" with "over 20 years of experience" (from the page). She wrote the harness-engineering article that gives this repo its vocabulary (guide, sensor, control). She counts as trusted through sustained, first-hand, published experiments with coding agents, and through that vocabulary being adopted here.

What the page says about git hooks (an experiment on one app, built with a custom "sensors" CLI that runs many checks and summarises them for the agent):

- List of sensors she runs in-session: type checker, ESLint, Semgrep, dependency-cruiser, test results with coverage, incremental mutation testing, and "GitLeaks runs as part of the pre-commit hook, I consider it to be a sensor as well, as it will give the agent feedback when it tries to commit (computational)".
- "After integration - pipeline: The same computational sensors run again in CI. The in-session sensors give the agent early feedback during development. The CI pipeline confirms the result on clean infrastructure and after integration."
- Section "Integration with the coding harness" asks "How to get the agent to check the sensor status regularly?" and lists four options:
  - "Via a guide - A skill, or a section in AGENTS.md ... This is the easiest way, and this is what I mostly did. But, it is also quite unreliable. I had to ask the agents many, many times why it had not run the sensors check a single time, or why it was running tests or linters directly instead of checking the sensors."
  - "Via hooks - I imagine there's a way to force this more regularly with hooks, but it needs some consideration which hooks to use. After every file edit is probably a good starting point, but it would have to be monitored if it's too much distraction for the agent." (agent hooks; she did not try it)
  - "Via git hooks - For users who like their agents to do frequent small commits, a pre-commit hook can be a good way to force a sensors check to take place before code even gets into a commit." (also not tried by her, as far as the page says)
  - A custom extension for the Pi harness, which "seems quite promising" but had not been used enough to tell if it ran more often than an instruction.
- She recommends a git hook only conditionally ("for users who like their agents to do frequent small commits"), so the fit depends on commit cadence. She does not report using a git hook to run the sensors CLI; the only git hook she reports running is the Gitleaks one.
- Not on the page: `--no-verify`, hook speed, or per-clone install.
