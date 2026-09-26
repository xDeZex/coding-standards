---
source: https://arxiv.org/abs/2602.12670
source_date: 2026-02
researched: 2026-09-26
---

# SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

Re-read 2026-09-26: full paper PDF (arxiv.org/pdf/2602.12670 v4, pdftotext), not the abstract page and not search snippets. The earlier version carried two search-snippet claims that the paper does not support; they are removed below.

Preprint (Xiangyi Li et al., large author list), arXiv 2602.12670, submitted 13 Feb 2026, v4 14 Jun 2026. Note that the numbers are from the latest version (v4).

- Design: 87 tasks in 8 domains, 18 model-harness configurations (Claude Code, Codex CLI, Gemini CLI, OpenHands and others), three trials per task, deterministic verifiers, matched no-skills and curated-skills conditions. Task instructions never name which skills to use; agents discover them through the normal loading mechanism.
- Curated skills raised the average pass rate from 33.9% to 50.5% (+16.6 points; configuration-level gains +4.1 to +25.7).
- Domain effect: Software Engineering was among the smallest gains (+11.6 points) and Mathematics among the smallest (+9.7); Natural Science (+28.8) the largest. The paper reads this as skills helping most where the model's pretraining lacks the procedure.
- Skill quantity: one skill +18.0 points, two to three skills +19.0, four or more +10.1. So focused bundles beat large ones, but two to three is barely better than one. Skill size: compact (+19.0) and standard (+21.5) beat detailed (+14.5) and comprehensive (+0.7).
- Self-generated skills (the agent writes its own first) landed 8.1 to 11.5 points below the no-skills baseline on the three dedicated-harness configurations.
- 13 of 87 tasks had negative skill deltas.
- Invocation: for task-shipped curated skills, the paper's Finding 4 is that skill discovery is usually not the bottleneck; recorded invocation rates were 84.7% to 99.2% on the configurations shown in its Table 14 (for example Codex + GPT-5.5 99.2%, Gemini CLI 90.4%, OpenHands + Sonnet 4.6 88.9%). The earlier snippet claim that human-authored skills are "rarely invoked" and that poor YAML descriptions make skills hard to trigger is not supported by this paper's text; the paper does say harness choice changes how the same model uses skills (for example Claude Opus 4.7 61.2% in Claude Code versus 53.1% in OpenHands).
- Limits: the paper says results may not transfer to GUI agents or multi-agent settings; skills here are supplied with the task, not selected from a large pool. Not about test-running instructions and not a comparison against AGENTS.md.
