---
title: "<Project> — Architecture (by subsystem + milestone)"
status: <living>
source_of_truth: ROADMAP.md
decisions: DECISIONS.md
prds: [prd-<subA>, prd-<subB>, prd-<subC>, prd-<subD>]
---

# <Project> — Architecture

> **This document describes the HOW (structural).** Organized by **subsystem** (not phase); every decision
> carries `[milestone · anchored|movable · serves <FRs>]`.
> - **anchored** = backbone / irretrofittable. Moving it costs a retrofit → conscious decision only.
> - **movable** = reschedulable; the open roadmap may move it freely.
> The *what+when* lives in ROADMAP.md; the *why* in DECISIONS.md (`D-NN`); the *testable requirements* in the
> subsystem PRDs. This doc does not restate them — it points.
>
> **The system is ONE platform that deepens, not N products.** Proof: the *"schema ON / enforcement OFF"*
> pattern — milestones (§C), not separate codebases.

---

## A · Spine (invariant — true in every milestone)
<!-- The small kernel that does not change shape across milestones. Everything else mounts on it. -->

| Plane | Choice | Deploy target | Invariant |
|---|---|---|---|
| <Orchestration> | **<tech + pin>** | <host, region> | <the invariant this plane guarantees> |
| <Data> | **<tech>** | <region> | <invariant> |
| <Observability> | **<tech>** | <scope> | <invariant> |

**Spine invariants (all anchored, all milestones):**
- **<Invariant name>** — <one-line statement>. `[<D-NN>]`
- **<Invariant name>** — <one-line statement> (`serves <Ref> → <SUB>-FRn`).

---

## B · Subsystem architecture
> Each subsystem owns one question. FRs cited are that subsystem's PRD FRs; ROADMAP `Ref`s in parentheses.

### B.1 — <SubA> · *<the question it owns>* → prds/prd-<subA>.md
- <one-line architectural fact>. `[<milestone> · anchored · <SUB>-FRn]`
- **<Named decision>** — <one-line>. **The pattern is anchored; the mechanisms are movable.** `[<milestone> · anchored (pattern) / movable (mechanisms) · serves <SUB>-FRn · <D-NN>]`

### B.2 — <SubB> · *<the question it owns>* → prds/prd-<subB>.md
- **<component>** — <one-line>. `[<milestone> · anchored · <SUB>]` (<D-NN>)
- **<schema item>** — **<milestone> schema-ON, enforcement <state>**. `[<milestone> · anchored · serves <Ref> schema]` (<D-NN>)

### B.3 — <SubC> · *<the question it owns>* → prds/prd-<subC>.md
### B.4 — <SubD> · *<the question it owns>* → prds/prd-<subD>.md

---

## C · Milestone deltas
<!-- What each milestone ADDS/ACTIVATES on the spine. State explicit non-transitions
     ("<Milestone-1> introduces no new X backbone") so an absence isn't read as an oversight. -->

### <Milestone-0> → <Milestone-1>
- <what activates / what schema turns ON> — `[serves <Ref> · <D-NN>]`
- > <explicit note: a planned backbone transition that was REMOVED — state it so the absence isn't read as an oversight.>
