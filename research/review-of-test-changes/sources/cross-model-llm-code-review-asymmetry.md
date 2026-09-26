---
source: https://arxiv.org/abs/2607.21656
source_date: 2026-07-22
researched: 2026-09-26
---

# Xiang et al.: Cross-Model LLM Code Review (Claude and Codex)

Preprint, accepted to the Agentic SE workshop at KDD'26 (per the abstract page). Read through a summarising fetch tool (abstract page only, not the PDF). Weak evidence for our question: small task set, two model families, and it measures task pass rate, not test tampering.

- Setup: Claude and Codex paired as drafter and reviewer on 116 challenging coding tasks; reviewers could read code but not execute tests.
- Result: Claude reviewing Codex drafts raised the pass rate from 71.6% to 89.7% (reported significant); Codex reviewing Claude drafts lowered it from 91.4% to 82.8%. Authors conclude the useful pairing is asymmetric.
- Relevance: shows review by a second model can hurt as well as help, and that results depend on the pairing. It does not isolate same-model versus cross-model review as a controlled contrast of self-preference; the summary gives no same-model arm.
- Unverified: exact protocol, what "pass rate" means, number of runs, and whether reviewers saw test files.
