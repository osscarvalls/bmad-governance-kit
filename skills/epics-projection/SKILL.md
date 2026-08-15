---
name: epics-projection
description: PROJECT epics.md from a milestone of a governance layer's ROADMAP (the "epics are projected, never a source of truth" law) — filter the milestone → resolve its FRs per subsystem via the Coverage Matrix → DELEGATE the expansion into stories to bmad-create-epics-and-stories → order by dependencies using architecture.md (anchored first) → write _epics/epics-<milestone>.md as a regenerable projection → optionally generate the sprint plan via bmad-sprint-planning → hand off to the build loop (bmad-create-story → bmad-dev-story). It invents nothing: it projects only what the registry already declares. Use when the user says "project the epics for <milestone>", "generate epics.md", "prepare the stories for milestone X", or is about to start building a milestone. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# epics-projection

**Goal:** turn a milestone of the registry into an ordered, build-ready `epics.md` — a **regenerable
projection**, never a new source of truth. This command projects only what ROADMAP + the Coverage Matrix
already declare; it does not invent features or FRs.

## On activation

1. **Resolve the layer.** Read `{gov}/GOVERNANCE.md` for the pillar paths and the `_epics/` location. No
   layer → tell the user to run `governance-scaffold`.
2. **Read ROADMAP.md** (the milestone tables + Coverage Matrix) and **architecture.md** (for anchored/movable
   ordering). Read the PRD(s) for the FRs' acceptance criteria.
3. Talk to the user in their language.

## Procedure

### 1 · Pick the milestone & load its scope
Ask which milestone (or accept it as an argument; accept narrowing to a single `Ref`). Load, **for that
milestone only**: its registry table (`Ref`s + status) and its Coverage Matrix rows (each `Ref`'s FRs per
subsystem). Be honest about status — if the milestone is `hypothesis`/`frozen`, the projection inherits that
label; don't launder it into `committed`.

### 2 · Pre-flight (recommended)
A projection inherits its source's quality. Offer to run **`governance-check`** scoped to this milestone
first (orphan `Ref`, empty matrix cell, live contradiction). If the user skips it, note that the coherence
gate didn't run.

### 3 · Expand into stories
**Delegate the expansion to `bmad-create-epics-and-stories`**: each `Ref` → an epic; each FR → the stories
that satisfy it, carrying acceptance criteria from the PRD. This skill supplies the *topology* (which Refs/
FRs are in scope, from the matrix); BMAD supplies the *expansion*.

### 4 · Order by dependencies (anchored first)
Use architecture.md's tags: `anchored` structural work comes before what depends on it; `movable` work is
free to reschedule. Produce a dependency-ordered sequence of epics/stories.

### 5 · Write the projection
Write `{gov}/_epics/epics-<milestone>.md`: a header stating it's a **regenerable projection** of milestone
`<X>` as of `<absolute date>` (+ inherited status), then the ordered epics → stories, each tracing
`story → FR → Ref`. It is not a source of truth; regenerating it must be safe.

### 6 · Sprint plan & handoff
Optionally invoke **`bmad-sprint-planning`** to generate the sprint status from this `epics.md`. Then hand
off to the build loop: **`bmad-create-story` → `bmad-dev-story`** (→ review). Name that as the next step.

## Report

Show: the milestone + its `Ref`s/FRs in scope, the pre-flight result, the ordered epic list (with anchored-
first rationale), the path written, and the handoff. Confirm the projection added no scope beyond the
registry.
