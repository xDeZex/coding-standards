---
source: https://arxiv.org/abs/2511.04824
source_date: 2025-11-06
researched: 2026-09-26
---

# Agentic Refactoring: An Empirical Study of AI Coding Agents

Preprint by Horikawa, Li, Kashiwa, Adams, Iida and Hassan. Abstract page read through a summariser.

- Data: 15,451 refactoring instances in 12,256 pull requests and 14,988 commits from real open-source Java projects (AIDev dataset).
- Agents mostly do low-level, consistency-oriented refactorings: Change Variable Type 11.8%, Rename Parameter 10.4%, Rename Variable 8.5%.
- Abstract: "Agentic efforts are dominated by low-level, consistency-oriented edits...reflecting a preference for localized improvements over the high-level design changes common in human refactoring."
- Motivations mostly maintainability (52.5%) and readability (28.1%); modest but statistically significant improvements in structural metrics.
- Bearing on the split: directly supports the observation that agents operate at the tactical level and humans do the high-level design changes, though it describes what agents do in the sampled PRs, not what they are capable of.
