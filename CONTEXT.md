# Coding Standards

A thinking space where a human and an AI research, discuss and document coding standards for software development with AI. Its outputs are meant to be carried into other repos by pointing an AI at this one.

## Language

**Kit**:
The portable set of artifacts this repo produces for use in other repos.
_Avoid_: Toolkit, package, bundle

**Catalogue**:
The source-of-truth collection of candidate instructions, each with its rationale and the conditions under which it applies, and each traceable to its sources through the position it comes from.
_Avoid_: Library, rulebook, database

**Catalogue entry**:
One candidate instruction in the catalogue, coming from a position.
_Avoid_: Rule, item, standard

**Countermeasure**:
A way of making a catalogue entry take effect in a repo, such as an AGENTS.md line, a skill, an agent hook or a deterministic tool. The term comes from lean.
_Avoid_: Control, enforcement

**Human guide**:
Writing about how a human should think with, operate and value working with AI.
_Avoid_: Manual, handbook

**Skills list**:
A curated list of pointers to skills that live elsewhere. This repo does not store skill content.
_Avoid_: Skill library

**Source note**:
A cited record of what a source (book, paper, talk, post) says, kept separate from our opinion of it.
_Avoid_: Research note, summary

**Position**:
Our conclusion on a topic, with its trade-offs, linking to the source notes it rests on.
_Avoid_: Verdict, opinion

**Source**:
A book, link or other origin of a claim, recorded with the date of the source and the date we researched it.
_Avoid_: Reference, citation

**Adoption**:
An AI, pointed at this repo from a target repo, inspecting that repo and proposing a selection from the catalogue for the human to confirm before anything is written.
_Avoid_: Installation, sync

**Blueprint**:
The decided shape of this repo and its kit, before any topic is researched.
_Avoid_: Spec, design

**Tactical**:
Code-level practice: how code is written, structured and checked. The level AI is good at, so increasingly delegated to it. A way of thinking, not a tag or folder.
_Avoid_: Low-level, implementation

**Strategic**:
Architecture, planning, process and the roles of humans and agents. The level humans increasingly focus on. A way of thinking, not a tag or folder.
_Avoid_: High-level, management
