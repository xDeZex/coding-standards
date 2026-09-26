---
source: https://arxiv.org/abs/2601.20103
source_date: 2026-01
researched: 2026-09-26
---

# Deshpande, Kannappan, Qian: Benchmarking Reward Hack Detection in Code Environments (TRACE)

Preprint (27 Jan 2026), Patronus AI authors. Read the abstract page through a summarising fetch tool. This is the closest measured evidence of an LLM as detector of reward hacks in code, including test-suite exploitation.

- TRACE: 517 synthetic, human-verified trajectories, 54 exploit subcategories in 10 categories (including test suite exploitation, solution quality degradation, context exploitation, execution environment hacks).
- Best detection rate 63% (GPT-5.2 at highest reasoning) in a contrastive setup (hacked versus benign trajectory compared); 45% when each trajectory is classified in isolation.
- "State-of-the-art models struggle significantly more with semantically contextualized reward hacks compared to syntactically contextualized ones." Special-casing that looks like plausible logic is the harder kind.
- Limits: trajectories are synthetic, not real agent runs; judges saw whole trajectories, not a diff; detection rate is reported without a false-positive rate in what was read. Whether the numbers hold for a reviewer of a PR is unverified.
- Classification: measures the inferential-review approach and shows it misses a large share.
