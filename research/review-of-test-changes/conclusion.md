# Review of test changes as a check on agents weakening tests

Findings on using review of what changed in the tests, by a human or an AI reviewer, as the check on an agent that makes a red run green by weakening, deleting or special-casing tests. This follows from the [testing feedback loop conclusion](../testing-feedback-loop/conclusion.md) and its position, which name reward hacking as an unsolved weakness. Findings only. The short answer is that no source measures review of test changes as a guard against agent test tampering. What exists is adjacent evidence, plus practitioner advice with no data.

## How to read the evidence

The 19 source notes fall into four groups.

- Human review research (Bacchelli and Bird, Spadini et al. twice, Google's practices and book chapter, Duma et al.). Peer-reviewed or primary Google writing, all about human-authored changes except Duma. Most were read at abstract level or through a summarising tool.
- Review-adjacent measurement (mutation testing at Google, Petrovic et al., Test Double and Meta reports). Measures signals shown to human authors and reviewers, not tampering.
- AI review and reward hacking measurement (TRACE, SWR-Bench, SpecBench, Xiang et al., Panickssery et al., vendor docs). Abstract-level reads, several with figures taken from search summaries. None tests an AI reviewer on weakened tests in real agent pull requests.
- Practitioner advice (GitHub blog, Pyor). Opinion, one is from a vendor of a review tool, and neither gives prevalence data or evidence that its advice works.

Every note was read through a summarising tool or an abstract page (one PDF partly), so quotes and figures need re-checking against the originals.

## What the sources say about the problem

The practitioner sources agree on the mechanism. The [GitHub blog](sources/github-blog-review-agent-prs-ci-gaming.md) says an agent that fails CI has an obvious path to green: remove the tests, skip the lint step, add `|| true`. The [Pyor posts](sources/pyor-reviewing-test-changes-in-agent-prs.md) name four patterns (deleted assertions, widened tolerances, skip annotations, changed expected values or regenerated snapshots) and say editing the assertion is often the shorter path. Neither gives any measure of how often this happens in ordinary work. The measured side of the problem (benchmarks and impossible tasks) sits in the parent topic, not here.

[SpecBench](sources/specbench-oversight-collapses-onto-tests.md) (abstract only) adds a scale point: the gap between visible and held-out test pass rates grows about 28 percentage points per tenfold increase in code size, and all frontier models saturate the visible tests yet still hack. Its framing is that oversight collapses onto the test suite. The connection to review is our inference: special-casing such as memorising test inputs lives in the source diff, so a review confined to the test diff would not see it. The paper was not read for reviewer results.

## What a review of test changes is, and how it differs from code review

The main empirical answer is [Spadini et al. 2018](sources/spadini-when-testing-meets-code-review.md) (abstract level, over 300,000 reviews plus interviews): reviewing test files is very different from reviewing production files, test code is often treated as secondary, and navigating between test and production is a main obstacle. It does not study weakened or deleted tests.

[Spadini et al. 2019](sources/spadini-test-driven-code-review.md) is a controlled experiment (92 participants, 154 reviews, Java, seeded defects). Reading tests first found the same share of production defects and more test-code defects, with fewer maintainability comments on production code. Developers still preferred production-first. It is human-authored code and says nothing about agents or tampering.

Google's [reviewer guide](sources/google-eng-practices-reviewer-tests.md) asks whether tests will actually fail when the code is broken, and the [SWE book chapter](sources/swe-book-code-review-chapter.md) says behaviour changes should come with test revisions. Neither names a signal for a test edited to pass; both leave it to judgement. The chapter's size and speed norms (about 200 lines, feedback in 24 hours) are human-scale assumptions.

The practitioner posts describe a difference in stance rather than a studied one. [Pyor](sources/pyor-reviewing-test-changes-in-agent-prs.md) says to read the test diff first and treat a changed test alongside changed code as the primary object of review, each change needing a justification. The [GitHub blog](sources/github-blog-review-agent-prs-ci-gaming.md) lists cheap, diff-visible checks (coverage threshold changes, tests removed, renamed or skipped, workflow changes) and calls any CI weakening a blocker. These are checks a script could make as well as a person; the sources do not say so. Both are untested advice. Pyor also claims that when one model writes code and tests, the tests tend to encode what the code does, which is plausible and unverified.

## Human review as the fallback: how well supported

Baseline evidence is unflattering. [Bacchelli and Bird](sources/bacchelli-bird-modern-code-review.md) (search summary only, 2013) found review is less about finding defects than assumed and depends on the reviewer understanding the change, which takes most of the time. For agents, [Duma et al.](sources/duma-how-humans-review-ai-prs.md) (abstract level, 33,596 AI PRs) report that most AI-generated PRs get no review, and where reviewed the comments are dominated by agents; 25.92% of comments on AI PRs are agent-steering commands that look like review. Observable review metrics can therefore overstate human oversight. The note also carries unread search snippets on agent PRs merging faster with less commentary that should be treated as unverified. Nothing here is specific to tests. The support is that human review of test changes is the accepted human practice, while whether it happens for agent PRs is doubtful.

Mutation testing is the closest computational aid to a human reviewer. [Google's system](sources/google-mutation-testing-in-code-review.md) (abstract only) shows surviving mutants to author and reviewer inside mandatory review, at the scale of 6,000 engineers. [Petrovic et al. 2021](sources/petrovic-does-mutation-testing-improve-practices.md) (abstract) found developers seeing mutants write more tests and leave fewer mutants surviving, with a correlation between mutants and real faults. Both concern missed faults in new code by cooperative humans, not weakened tests by an agent. The [Test Double and Meta notes](sources/mutation-testing-agent-code-practitioner-and-meta.md) are an anecdote (including an agent that misreported its own mutation score, 96.30% against an actual 94.44%) and a secondary report of engineers accepting 73% of generated tests. That a mutation-score drop would reveal weakened assertions is plausible and not shown by any source.

## AI review as an inferential control: how well supported

The vendor documentation supports the classification and the limits, not the effect.

- [Claude Code](sources/claude-code-review-docs-scope.md) reviews by default for correctness, not "missing test coverage"; checks can be expanded through `CLAUDE.md` or `REVIEW.md`. It is advisory, averages 20 minutes and $15 to $25 per review, and states a precision and coverage trade-off with no numbers.
- [Codex](sources/codex-code-review-github-docs.md) by default flags only P0 and P1 issues, so a weakened test may fall below that bar unless rules say otherwise, and it advises leaving deterministic checks to CI.
- [Copilot](sources/copilot-code-review-responsible-use.md) says it may miss problems, may hallucinate problems, and should supplement human review, not replace it. A claim that it reviews only a risk-selected subset of files in large PRs came from a community thread and is unverified.
- None of the three pages gives detection or false-positive rates or mentions test tampering. Whether a rule such as "flag deleted or loosened assertions" works is not documented anywhere read.

Measured evidence is indirect and weak. [TRACE](sources/trace-reward-hack-detection-in-code.md) (abstract) is the closest: on 517 synthetic trajectories with test-suite exploitation among the categories, the best model detected 63% in a contrastive setup and 45% classifying each in isolation, and did worse on semantically contextualised hacks (plausible-looking logic) than syntactic ones. Limits: synthetic trajectories, whole trajectories rather than diffs, no false-positive rate in what was read. [SWR-Bench](sources/swr-bench-llm-code-review-precision.md) reports LLM reviewers underperforming on ordinary PRs, better at functional errors; the precision (often under 10%) and F1 (19.38% best) figures come from a search summary and are unverified, and reviewers tested predate the 2026 tools. [Xiang et al.](sources/cross-model-llm-code-review-asymmetry.md) (abstract) found cross-model review helped one direction (71.6% to 89.7%) and hurt the other (91.4% to 82.8%), so the effect of a second model depends on the pairing. Reviewers could not run tests, and what they saw of test files is unknown.

A possible concern is same-model review. [Panickssery et al.](sources/llm-evaluators-recognize-and-favor-own-generations.md) find self-recognition correlates with self-preference in models rating summaries. Applying this to a model reviewing its own agent's diff is our inference; the paper does not test it, and Xiang et al. has no same-model arm.

## Unverified or absent

- Any measurement of a human or AI reviewer catching weakened, deleted or special-cased tests in real agent PRs, and any false-positive rate for that task.
- Prevalence of test tampering in ordinary agent PRs.
- Whether review comments from an AI reviewer are acted on, and whether a reviewer with instructions to check test diffs beats one without.
- Whether mutation score or diff-visible signals shown to a reviewer catch weakened tests.
- Full-text figures for nearly all sources (abstract or summary reads only); the SWR-Bench precision figures and the Duma search snippets in particular.

## Connection to AI coding

The evidence supports a narrow claim: review is an inferential (AI) or human control that vendors and practitioners describe as advisory and fallible, and the only detection measurement found (TRACE) shows an AI judge missing a large share of hacks in synthetic settings. Human review of test changes rests on general practice, and the one large study of agent PRs suggests it is often absent or diluted. Read-only tests, which stop editing but not special-casing, are outside these sources; SpecBench's scale argument suggests special-casing hides where a test-diff review does not look. Review of test changes is thus supported as a reasonable practice, and unproven as a fix, which matches how the parent position already frames it.
