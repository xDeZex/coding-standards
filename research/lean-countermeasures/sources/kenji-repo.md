---
source: ~/repos/kenji (local repo, commit 2169728; CONTEXT.md, docs/adr/0001, 0002, 0004, .agents/skills/improvement-kata/SKILL.md and KATA-FORMAT.md)
source_date: 2026-07-03
researched: 2026-09-26
---

# Kenji: a lean agent that reviews AI coding sessions

Secondary, practitioner source: one author's application of the Improvement Kata to AI coding. It is not a lean primary source. Read for how the term is used, not as authority on what lean means.

- **Countermeasure (CONTEXT.md)**: "A small, reversible change applied to address a specific waste pattern. May be a change to developer workflow, AI instruction files, documentation, or process conventions. The action taken in an Experiment." Avoid: Fix, solution, recommendation, rule.
- **Experiment**: "A single PDCA cycle within a Target Condition. Contains a hypothesis (what is expected to happen), a Countermeasure (the change applied), and an outcome (what was actually observed)."
- **Target Condition**: measurable picture of the next stage of the process, specific enough that a future Review can decide whether it was reached. Criterion must be checkable "without interpretation"; each has a check window so it does not stay open forever.
- **Harness**: the recorded AI engineering environment (instruction files, CI/hooks, skills, review flow). "Names the levers a Countermeasure can pull."
- **Status**: `active` -> `met` -> `standardized` ("the improvements that achieved the Target Condition have been written into standard work"), or `abandoned`.
- **Check**: evaluating whether a Target Condition has been reached, by examining session evidence against its measurable criteria.
- **ADR-0001 (superseded)**: countermeasures kept in a backlog, not written into tool instruction files, to stay tool-agnostic. ADR-0002: this left improvements unapplied, "a PDCA cycle with no 'Do' step". Kenji now proposes, gets approval, and applies countermeasures directly to instruction files (AGENTS.md, CLAUDE.md) in the same session. Tool-agnosticism is handled at Target Condition level.
- **ADR-0004**: splitting Target Condition (goal) from Experiment (attempt) lets one distinguish "the countermeasure failed" from "we haven't found the right countermeasure yet"; a failed experiment does not reset the improvement work.
- **improvement-kata skill**: 1 read session (genchi genbutsu); 2 read Workflow, Challenge, Harness (a Workflow step marked discretionary and skipped by judgment is not muda); 3 check open Target Conditions (verdict met/progressing/stalled with turn citations); 4 grasp current condition by hunting muda per turn (rework, waiting, motion, overprocessing, defect); 5 build proposal (verdicts, new Target Conditions, exact file changes); 6 get approval; 7 apply.
- **KATA-FORMAT**: experiments table (date, hypothesis, countermeasure, outcome) is append-only, "the record of what failed is part of the learning". Workflow steps are tagged Enforced (CI, hook, skill logic) or Discretionary.

Not addressed in the repo: poka-yoke, root-cause selection method (5 whys, criteria matrix), how a countermeasure is chosen among alternatives.
