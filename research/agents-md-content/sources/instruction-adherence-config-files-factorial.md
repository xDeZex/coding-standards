---
source: https://arxiv.org/abs/2605.10039
source_date: 2026-05
researched: 2026-09-26
---

# Instruction Adherence in Coding Agent Configuration Files: A Factorial Study of Four File-Structure Variables

Re-read 2026-09-26: full paper PDF (arxiv.org/pdf/2605.10039, pdftotext), not the abstract page and not a summarising tool. The earlier version of this note said the range of file sizes and the instruction type were unknown; both are now known.

Preprint (Damon McMillan, HxAI Australia, single author), arXiv 2605.10039, submitted 11 May 2026. Not peer reviewed as far as shown.

- Design: 1,650 Claude Code CLI sessions (16,050 function-level observations) on two TypeScript codebases (a Next.js scaffold, ixartz, carries the 1,200-session primary Sonnet 4.6 pool; Umami 150), Sonnet 4.6 primary, Opus 4.6 as a cross-model check, Opus 4.7 reported only descriptively (CLI-version confound), five coding tasks, mixed-effects models with a Bayesian companion.
- The instruction tested is a single trivial one: emit a `// @tracked` annotation on generated functions, detected by AST parsing. Padding around it was authored to mimic topics common in real files, not taken from a repository. Baseline compliance was 60 to 68% depending on the cell; without any file, zero spontaneous emission.
- Variables and levels: file size 25, 100, 250, 500 lines (compliance 60.0%, 65.2%, 67.7%, 64.0%; GLMM p = 0.16); instruction position at line 2, 63, 128, 187, 250 of a 250-line file (67.7% down to 61.8%; p = 0.83; the largest contrast, first versus last position, was 5.9 points, raw p = 0.055, not significant after correction); architecture (single CLAUDE.md; plus AGENTS.md; plus two nested CLAUDE.md files; 67.7%, 68.2%, 61.7%; p = 0.19, the nested variant's 6-point dip did not survive correction); a contradicting instruction in an adjacent file (63.7% versus 64.1%). None of the four variables and none of three two-way interactions was detectable after correction. Only the size and conflict nulls have affirmative Bayes-factor support (BF10 0.05 to 0.10); position and architecture are failures to reject without such support, so they are weaker nulls.
- Within-session effect: about 5.6% lower odds of compliance per additional generated function (odds ratio 0.944, 95% Wald CI 0.937 to 0.951; log-odds slope -0.0578). The paper says this was identified during analysis rather than pre-specified, is non-monotonic rather than a constant per-step effect, differs by task, concentrates in the first three to four generated functions (median first omission at generation position 4), is detectable on two of three multi-function tasks, and reproduces in direction on the second codebase and on Opus 4.6. The unit is "per generated function within a session", not per instruction or per line.
- Task identity mattered more than any file variable (a 26.2-point gap between two specific tasks).
- Relevance: at 25 to 500 lines, for one trivial instruction, size and position did not measurably change compliance. It does not test realistic multi-instruction files, test-running instructions, or skills and hooks.
