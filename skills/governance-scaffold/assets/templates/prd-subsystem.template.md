---
title: "PRD — <Subsystem>"
subsystem: <Subsystem>
status: draft-vN
created: <YYYY-MM-DD>
updated: <YYYY-MM-DD>
source_of_truth: ../ROADMAP.md
decisions: ../DECISIONS.md
fr_namespace: <SUB>-FR
---

# PRD — <Subsystem>

## 0. Purpose
<!-- What this PRD is canonical for; who reads it downstream (epics-projection / build / test-strategy).
     Every FR keeps its [milestone · anchored|movable · serves <Ref>] tag + its · D-NN provenance;
     the Coverage Matrix stitches each FR back to its ROADMAP Ref. Points to decisions, never restates. -->

> **Reading key.** Each FR carries `[milestone · anchored|movable · serves <ROADMAP Ref>]`.
> *anchored* = backbone/irretrofittable; *movable* = product capability, reschedule freely.
> Depth is proportional to milestone: committed FRs are full; hypothesis/frozen FRs are stated + tagged.

## 1. Vision
<!-- What this subsystem IS; the boundary as a decision rule (what belongs here vs other subsystems).
     Names capabilities and boundaries, not vendors (concrete stack → architecture.md). -->

## 2. Target user & jobs-to-be-done
- **<archetype>** (<milestone>) needs <…>. Realizes UJ-1..UJ-N.

## 3. Glossary
- **<Term>** — <definition; point to architecture.md for concrete stack>.

## 4. Features

### 4.A <Feature group name>
**Description:** <one paragraph; concrete stack → architecture.md.>

**Functional requirements:**

#### <SUB>-FR1 — <requirement title>
`[<milestone> · anchored · serves <Ref>]` · realizes UJ-1 · <D-NN>

<The requirement, one or two sentences. Point to architecture.md for impl.>

**Consequences (testable):**
- <testable consequence>.
- <testable consequence> *(impl: architecture.md §…)*.

#### <SUB>-FR2 — <title>
`[<milestone> · movable · serves <Ref>]` · <D-NN>

<statement.>

**Consequences (testable):**
- <testable consequence>.

## 5. Non-functional requirements
<!-- Cross-cutting NFRs go HERE as a section, NOT as FRs. Named NFR-<CODE> so the Coverage Matrix and
     tests can reference them. -->
- **NFR-<CODE> — <name>.** <the constraint, testable>.

## 6. Coverage (this subsystem's FRs → ROADMAP Ref)
| <SUB>-FR | serves Ref | milestone |
|---|---|---|
| <SUB>-FR1 | <Ref> | <milestone> |
