---
source: https://arxiv.org/html/2605.02273v1
source_date: 2026-05
researched: 2026-09-26
---

# These Aren't the Reviews You're Looking For: How Humans Review AI-Generated Pull Requests (Duma et al., EASE 2026)

Primary source: empirical preprint on the AIDev dataset. How it was read this time: PDF of arXiv 2605.02273 via pdftotext (full text). The earlier note mixed up two table rows; corrected below.

- Data: AIDev dataset. Popular-repository subset (R_pop, at least 100 stars): 33,596 agent-authored PRs. Same-repository comparison subset (R_intersect): 9,616 agent-authored and 5,574 human-authored PRs.
- R_pop PR level: 61.38% (20,621) of the 33,596 agent PRs have no recorded review; 12,975 (38.62%) have at least one review. Of those reviewed, 58.77% agent-only, 10.14% human-only, 31.09% human plus agent (the text says 40.34% for the last, table and arithmetic give 31.09%). 84.0% of agent PRs have no recorded review or agent-only review; 15.9% show human participation. Authors stress absence of recorded review is not absence of oversight (maintainers may inspect without commenting).
- R_pop comment level (Table 2): 39,122 review comments, 71.58% by agents, 28.42% by humans; of the human comments 64.53% direct human review, 28.37% agent-steering, 7.10% automation.
- R_intersect (the source of the 65.53% / 25.92% / 8.55% split, not the 33,596 set): agent PRs 65.53% direct review, 25.92% steering, 8.55% automation; human PRs 93.56% direct review, 1.63% steering. The percentages are shares of human-authored comments, not of all comments.
- Within the same repositories agent PRs were reviewed slightly more often than human PRs (71.08% vs 65.48%, small effect, V = 0.06), and observable human participation was nearly identical (30.12% vs 30.83%). The difference is in composition: human-only review 8.08% for agent PRs vs 25.21% for human PRs; mixed human-agent 34.29% vs 21.86%.
- Classifier: rule-based, 96.5% accuracy (772 of 800 hand-checked comments). Abstract: metrics can be hard to read as human oversight because steering commands look like review.
- Says nothing specific about tests. "Most AI-generated PRs receive no review" holds for the R_pop set as recorded review activity; it does not hold as a difference from human PRs in the same repositories.
- Earlier snippet claims: "45.1% of merged agentic PRs needed revisions" is not in this paper and not in arXiv 2605.06464 (which was read and does not contain it); it comes from Watanabe et al., arXiv 2509.14745 (567 Claude Code PRs, 157 projects; of 475 merged PRs, 214 (45.1%) were modified between submission and merge; human PRs 58.5% unmodified vs 54.9% for agent PRs, no significant difference; test changes were in 16.4% of the revised agent PRs). That paper was read via pdftotext for these numbers only. The "9.9% of generated methods deleted in review" claim could not be found in any source read and is dropped. The claims about agentic PRs merging faster with less commentary and reviewer burden tied to PR size were not found in this paper and are unverified.
