---
source: https://arxiv.org/abs/2509.01494
source_date: 2025-09
researched: 2026-09-26
---

# Zeng et al.: Benchmarking and Studying the LLM-based Code Review (SWR-Bench)

Preprint (submitted 1 Sep 2025, revised 5 Jun 2026). Read the abstract page through a summarising fetch tool; the precision figures below come from a search-result summary of the paper and are unverified against the PDF.

- Benchmark: 1,000 manually verified GitHub pull requests; per the search summary, balanced between 500 PRs with real issues and 500 clean PRs, so false-positive behaviour can be measured.
- Abstract: "current systems underperform, and ACR tools are more adept at detecting functional errors." A multi-review aggregation strategy raised F1 by up to 43.67%. The LLM-based scoring is said to agree with humans about 90%.
- Search-summary figures, unverified: precision often below 10%; best single combination (PR-Review with Gemini-2.5-Pro) F1 19.38%.
- Relevance: general evidence that LLM reviewers of ordinary PRs have low precision and recall. Not specific to test changes, and reviewers are older than the mid-2026 tools.
