---
source: https://arxiv.org/abs/2605.10039
source_date: 2026-05
researched: 2026-09-26
---

# Instruction Adherence in Coding Agent Configuration Files: A Factorial Study of Four File-Structure Variables

Preprint, arXiv 2605.10039, submitted 11 May 2026. Abstract page only, via a summarising fetch tool (the full HTML returned 404).

- 1,650 Claude Code CLI sessions (16,050 function-level observations), two TypeScript codebases, Sonnet 4.6 and Opus models.
- Four file-structure variables tested: file size, instruction position, file architecture, and contradictions between adjacent files. After multiple-testing correction none of the four, and none of three two-way interactions, gave a detectable effect on compliance.
- Within a session, compliance fell by about 5.6% in odds per additional function generated (odds ratio 0.944), and it varied by task.
- Relevance: contradicts, for the sizes tested, the vendor claim that longer files reduce adherence ([Claude Code docs](claude-code-best-practices-claude-md.md)); the range of file sizes was not read. It also suggests adherence to a standing instruction decays over a long session, which bears on "a reminder before the agent acts". Which instruction types were tested is not known from the abstract.
