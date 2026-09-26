---
name: position
description: Discuss a research topic's conclusion with the user and write their position.
disable-model-invocation: true
---

The position is the user's stance; the conclusion is material for them to react to. Read `research/README.md` ("Who writes what") first.

## 1. Pick the topic

Take the topic named, else the one `research/<topic>/` with a `conclusion.md` and no `position.md`. Done when exactly one topic is chosen; if several fit, ask which.

## 2. Elicit their opinion

Read the conclusion and its source notes yourself, then ask for the user's own opinion on the topic and how it connects to AI coding. Keep the conclusion out of the question and give no recommended answer, so nothing _anchors_ them. Done when their opinion is in their own words and specific enough to grill; ask a follow-up until it is.

## 3. Grill

Call the Skill tool twice, for `grilling` and `domain-modeling`; `grill-with-docs` cannot be called by you. Grill their opinion against the conclusion and source notes: where it agrees, disagrees or goes beyond them, what is unverified, and how it applies to AI coding, tactical and strategic. Done when every branch of their opinion has been visited and they confirm shared understanding.

## 4. Write the position

Write `research/<topic>/position.md` in the user's voice, per `research/README.md`. Done when the user has approved it and the validator exits 0; then commit and push. Leave `conclusion.md` untouched: it stays as the record of what the research found.
