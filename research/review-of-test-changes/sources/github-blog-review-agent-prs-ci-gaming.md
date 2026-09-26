---
source: https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/
source_date: 2026-05-07
researched: 2026-09-26
---

# Agent pull requests are everywhere. Here's how to review them. (Andrea Griffiths, GitHub Blog)

Vendor practitioner guidance from GitHub, opinion, no measurement. Read through a summarising tool; quotes need re-checking.

- "Agents fail CI. When they do, they have an obvious path to get tests passing: remove the tests, skip the lint step, add || true to test commands."
- Checklist for the reviewer: "Did coverage thresholds change? Were any tests removed, renamed, or marked as skipped? Did the workflow stop running on forks or pull requests?"
- Stance: "Any change that weakens CI is a blocker. Full stop."
- Signals named are all cheap, diff-visible facts (removed, renamed, skipped tests, coverage threshold, workflow config), not judgement calls about assertion strength.
- No prevalence data is given for agents doing this in practice.
