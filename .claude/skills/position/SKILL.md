---
name: position
description: Discuss a research topic's conclusion with the user and write their position. Use when the user wants to form, discuss or write a position for a research topic, or says "position" about a topic under research/.
---

Turn a research conclusion into the user's **position**. The position is the user's stance, not the agent's; the conclusion is only material to react to. Read `research/README.md` ("Who writes what") and `CONTEXT.md` first.

## 1. Pick the topic

Use the topic the user named, else the one `research/<topic>/` folder with a `conclusion.md` and no `position.md`. If several fit, ask which, one question.

## 2. Ask for their opinion first

Before discussing anything, ask the user for their own opinion on the topic, in their own words and how it connects to AI coding. Do **not** summarise, quote or hint at the conclusion first, and don't offer a recommended answer to this question: it would anchor them. You may read the conclusion and source notes yourself beforehand. Wait for the reply. Ask a follow-up only if the opinion is too vague to grill.

## 3. Grill

Once their opinion is on the table, call the Skill tool for `grilling` and `domain-modeling` and grill them against `research/<topic>/conclusion.md` and its source notes: where their opinion agrees, disagrees with, or goes beyond the sources, what is unverified, and how it applies to AI coding (tactical and strategic). Follow the repo's interview style in `CLAUDE.md`: one question at a time, with a recommended answer, waiting for the reply and naming any later question it affects. Sharpen terms into `CONTEXT.md` as they settle.

## 4. Write the position

When the user confirms shared understanding, write `research/<topic>/position.md` in their voice, per `research/README.md`: free prose, trade-offs and when it does not hold, links to source notes for specific claims, and one heading per conclusion that will yield a catalogue entry. Show it for approval, run the validator until it exits 0, then commit and push. Never delete or modify `conclusion.md`; it stays as the record of what the research found.
