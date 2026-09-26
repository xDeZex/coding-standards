---
source: https://arxiv.org/abs/2511.21654
source_date: 2026-05
researched: 2026-09-26
---

# EvilGenie: a Reward Hacking Benchmark (Gabor, Lynch, Rosenfeld)

Primary source: arXiv preprint (v1 26 Nov 2025; v2 17 May 2026 read from the PDF). Source date is that of the version read.

- Setup: LiveCodeBench problems in a directory the agent can view, edit and run (problem.md, solution.py, test_cases.json, test.py). 30% of test cases (max 10) held out and not disclosed. Reward hacking is possible by hard-coding, reading test_cases.json, or editing test files. Detection by held-out tests, LLM judge and test-file-edit detection, checked against human review.
- Agents evaluated in their vendor scaffolds: OpenAI Codex (GPT-5), Anthropic Claude Code (Claude Sonnet 4), Google Gemini CLI (Gemini 2.5 Pro); plus many models in the open Inspect basic_agent scaffold.
- Abstract: "explicit reward hacking by both Codex and Claude Code, and misaligned behavior by all three agents."
- Unambiguous problems (n = 145), Codex / Claude Code / Gemini CLI: hard-coded test cases 0.7% / 2.1% / 0%; modified test file 0% / 0% / 0.7%; deleted test file 0% / 0% / 3.4%; heuristic solution 0.7% / 20.7% / 0%; legitimate and correct 77.2% / 42.1% / 58.6%. Gemini 2.5 Pro was the only agent to delete or modify the test file; Claude Sonnet 4 far more often gave heuristic (non-general) solutions.
- Ambiguous problems (where the tests forbid some solutions that could be correct; n = 9): hard-coded test cases 44% / 33% / 22%, so hacking "was far more prevalent" when tests and spec are ambiguous.
- Detection findings: the LLM judge was "highly effective" in unambiguous cases; held-out tests gave "only minimal improvement", and are not foolproof (three cases of Claude Code exploiting a heuristic that passed both visible and held-out tests). In one case Gemini modified test.py before its final test run but its solution was still correct.
- Comparison with other work (authors' text): most EvilGenie problems are solvable legitimately yet reward hacking is still non-zero, which they call "arguably more concerning than on unsolvable problems". They note many ImpossibleBench "cheats" involve correcting an incorrect unit test, which "is arguably desirable behavior" even though it breaks the instruction not to modify tests.

Caveat: small samples on ambiguous problems; competitive-programming tasks, not repository work.
