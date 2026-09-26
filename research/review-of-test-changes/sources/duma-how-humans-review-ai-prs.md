---
source: https://arxiv.org/html/2605.02273v1
source_date: 2026-05
researched: 2026-09-26
---

# These Aren't the Reviews You're Looking For: How Humans Review AI-Generated Pull Requests (Duma et al., EASE 2026)

Primary source: empirical preprint on the AIDev dataset. Abstract-level summary via a fetch tool; figures need re-checking.

- Sample: 33,596 AI-generated PRs from GitHub repositories with at least 100 stars.
- "Most AI-generated PRs receive no review and, when reviewed, are largely dominated by AI agents rather than humans."
- Comment mix on AI PRs: 65.53% direct human review, 25.92% agent-steering commands, 8.55% automation messages; for human-authored PRs 93.56% direct human review and 1.63% agent-steering. A rule-based classifier reached 96.5% on 800 hand-checked comments.
- Implication stated: observable review metrics can overstate human oversight because steering commands look like review.
- Says nothing specific about tests. It is evidence that human review of agent PRs is often absent, which bears on human review as a fallback. Related search snippets (not read): agentic PRs merge faster with less human commentary; 45.1% of merged agentic PRs needed revisions (arXiv 2605.06464 and others); a claim that reviewer burden comes from PR size. Treat those as unverified.
