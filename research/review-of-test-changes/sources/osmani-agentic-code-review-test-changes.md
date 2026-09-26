---
source: https://addyosmani.com/blog/agentic-code-review/
source_date: 2026-06-15
researched: 2026-09-26
---

# Addy Osmani: Agentic Code Review (test-change passage)

Practitioner blog post. How it was read this time (re-read pass, 2026-09-26): raw HTML fetched with curl, stripped to text with a python html.parser script, and every quote below checked against that text (all matched verbatim; the ellipsis in the CI quote elides "are the one part of the pipeline that"). Only the test and CI passages matter here. Opinion; the post cites third-party numbers (Faros, CodeRabbit, GitClear) that were not checked.

- "Read the test changes more carefully than the code. This is the agent failure mode to watch. The agent changes behavior, then 'fixes' the test by rewriting the assertion to match the new, broken behavior. A green check over 200 edited tests means nothing until you have confirmed the edits were correct. Treat any diff that rewrites many tests as a flag and read those first."
- "Mutation testing earns its place here: coverage tells you a line ran, mutation testing tells you whether the test would notice if that line were wrong."
- "Treat CI as the wall that does not move": watch for removed tests, skipped lint, lowered coverage thresholds (the page frames these as patterns "GitHub now warns reviewers about"); "Agents will also weaken CI to make themselves pass, not maliciously, just gradient descent finding the cheapest path to green. Deterministic gates ... cannot be talked out of their verdict".
- The post says "the agent failure mode to watch" about test rewriting but does not use the phrase "test-rewrite failure mode"; the Pyor post attributes that label to him. No prevalence data for test rewriting.
