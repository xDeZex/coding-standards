---
source: https://arxiv.org/abs/2511.04824
source_date: 2025-11-06
researched: 2026-09-26
---

# Agentic Refactoring: An Empirical Study of AI Coding Agents

How read this time: PDF fetched from arxiv.org/pdf/2511.04824 and converted with pdftotext; read the abstract, introduction, RQ2 and RQ3 sections, the implications section, the threats to validity and the conclusion. Other sections (RQ1 details, RQ4 metrics, related work) were only checked with keyword search. Earlier note was based on the abstract page via a summariser.

Preprint (v1, 6 Nov 2025) by Horikawa, Li, Kashiwa, Adams, Iida and Hassan. Not peer-reviewed as far as the PDF shows.

- Data: 15,451 refactoring instances across 12,256 pull requests and 14,998 commits (the earlier note said 14,988, which was wrong) from open-source Java projects in the AIDev dataset. Refactoring appears in 26.1% of agentic Java commits; 53.9% of refactoring instances occur in commits with no explicit refactoring intent.
- Most common agent refactorings: Change Variable Type 11.8%, Rename Parameter 10.4%, Rename Variable 8.5%. Abstract: "agentic efforts are dominated by low-level, consistency-oriented edits ... reflecting a preference for localized improvements over the high-level design changes common in human refactoring."
- The comparison is relative, not absolute. By abstraction level (Table 4): agents 43.0% high-level refactorings versus 54.9% for humans; low-level 35.8% versus 24.4%; medium-level about equal (21.2% versus 20.7%). So agents still perform many high-level (signature-level) refactorings. The human baseline comes from human refactoring patterns reported in prior work (reference [22] in the paper), not from the same dataset.
- Motivations: maintainability 52.5%, readability 28.1% (classified from PR titles, commit messages; the human comparison there uses data from Kim et al.).
- Quality effects: small but statistically significant improvements in structural metrics (for example Class LOC median delta -15.25), but the paper states it "does not consistently reduce design and implementation smells"; Finding #8 says the reductions in smell counts are "statistically significant but not practically significant (i.e., negligible effect size)".
- Caveats in the paper: agentic commits are identified by keywords and author information, and it is hard to tell how much human intervention occurred, so the authors frame the study as human-AI collaborative refactoring. Data are open-source only and Java only.
- The paper's own implication for developers: "Developers can delegate routine cleanup to agents and focus human effort on design-level restructuring that requires domain knowledge and architectural intent." This is the authors' recommendation, not a measurement.
- Bearing on the split: consistent with agents leaning toward localised edits more than humans do; it describes what agents did in sampled PRs, not what they are capable of.
