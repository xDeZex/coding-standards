---
source: https://arxiv.org/abs/2605.02741
source_date: 2026-05-04
researched: 2026-09-26
---

# AI-Generated Smells: An Analysis of Code and Architecture in LLM- and Agent-Driven Development

Preprint by Yuecai Zhu, Nikolaos Tsantalis and Peter C. Rigby. Only the abstract page was read (via a summariser). Not peer-reviewed as far as known.

- Method: multi-scale audit from single-file algorithmic tasks to complex agent-generated systems.
- Claims: AI produces bloated, tightly coupled code that degrades architecturally as model capability increases; code volume strongly predicts structural degradation (a "Volume-Quality Inverse Law"); neither functional correctness nor detailed prompting prevents the decay.
- Conclusion quoted: "future progress depends on equipping agents with explicit architectural foresight to ensure the software they build is not just functional, but also maintainable."
- Bearing on the split: evidence that agents are weak at design-level qualities while passing functional checks, so human strategic attention is needed. It also suggests code-level output is not reliably good on structure. Sample sizes and models not recorded here.
