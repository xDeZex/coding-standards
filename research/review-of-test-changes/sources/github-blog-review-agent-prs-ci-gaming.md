---
source: https://github.blog/ai-and-ml/generative-ai/agent-pull-requests-are-everywhere-heres-how-to-review-them/
source_date: 2026-05-07
researched: 2026-09-26
---

# Agent pull requests are everywhere. Here's how to review them. (Andrea Griffiths, GitHub Blog)

Vendor practitioner guidance from GitHub, opinion, no measurement. How it was read this time: fetched with curl and converted to text, read in full; quotes verified against the page.

- "Agents fail CI. When they do, they have an obvious path to get tests passing: remove the tests, skip the lint step, add || true to test commands. Some agents take it."
- "Any change that weakens CI is a blocker. Full stop." Checklist before approving: "Did coverage thresholds change?", "Were any tests removed, renamed, or marked as skipped?", "Did the workflow stop running on forks or pull requests?", "Are any CI steps now gated behind conditions they weren't before?" A yes needs "an explicit justification".
- A review-order table says to check CI changes (workflows, test configs, coverage settings, build scripts) before reading application code.
- Separate advice: require a new test that fails on the pre-change behaviour for a bug fix.
- The signals named are diff-visible facts, not judgements about assertion strength.
- No prevalence data for agents doing this ("Some agents take it" is an assertion). The post also cites vendor figures (60 million Copilot reviews, one in five reviews involving an agent) without sources.
