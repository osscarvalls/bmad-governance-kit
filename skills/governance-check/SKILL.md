---
name: governance-check
description: READ-ONLY anti-drift auditor of a governance layer's four-pillar graph — verifies every Ref⇄FR (both directions, no orphans), no duplicated facts across pillars (one truth one place), correct FR namespacing, an append-only/coherent DECISIONS log, present anchored/movable architecture tags, a coherent Graveyard, and an accurate constitution. It WRAPS bmad-check-implementation-readiness (spec completeness) plus bmad-review-adversarial-general / bmad-review-edge-case-hunter (adversarial lens) and adds only the governance invariants, composing them into ONE PASS/WARN/FAIL report. It NEVER auto-fixes. Use when the user says "check the governance", "audit coherence", "governance check", or before a checkpoint / before projecting epics. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# governance-check

**Goal:** prove the governance graph is coherent — or report exactly where it drifted — without changing a
single character. A projection or a build inherits the quality of this graph; audit it before you rely on it.

## On activation

1. **Resolve the layer.** Read `{gov}/GOVERNANCE.md` for the pillar paths, subsystem set + FR namespaces,
   and the anti-drift laws to audit against. No layer → tell the user to run `governance-scaffold`.
2. **Read-only.** This command **never** edits. It reports; the write-commands (`feature-intake`,
   `decision-record`, …) fix what it finds.
3. Wrap the BMAD gate where available: **`bmad-check-implementation-readiness`** (are specs complete/ready?),
   sharpened by **`bmad-review-adversarial-general`** / **`bmad-review-edge-case-hunter`** (orthogonal
   adversarial lens). Add only the governance-invariant delta below.

## The invariants (PASS / WARN / FAIL each, with offenders named)

1. **Ref ⇄ FR, both directions.** Every registry `Ref` has ≥1 FR in the Coverage Matrix; every FR `serves`
   a real `Ref`. No orphan features, no orphan requirements.
2. **One truth, one place.** No fact written into two pillars (a feature narrated in both ROADMAP and a PRD
   statement; an FR's text copied into architecture). Consequences joined by shared `Ref`/`D-NN` are fine;
   copied text is a FAIL.
3. **Namespacing.** Every FR is `<PREFIX>-FRn` for a real subsystem; no stray global `FR-n`; every
   provisional slug resolved or parked with a reason.
4. **DECISIONS integrity.** Append-only shape intact; no edited/deleted closed entries; every supersede/
   reframe is a forward pointer; every Graveyard row has a `D-NN`; no live contradiction between two VIGENTE
   decisions.
5. **Architecture tags.** Every structural decision carries `[milestone · anchored|movable · serves <Ref>]`;
   anchored items are genuinely backbone; architecture restates no FR text; `source_of_truth: ROADMAP` holds.
6. **Graveyard & Backlog coherence.** Killed items aren't reopened elsewhere; Backlog items are `state=idea`
   with no FRs yet; nothing planned is "loose" (everything is in a milestone table, Backlog, or Graveyard).
7. **Naming.** Project vocabulary used consistently; implementation names not leaking into product-surface
   docs if the constitution forbids it.
8. **Constitution accuracy.** GOVERNANCE.md's pillar paths, subsystem list, and pointers match disk.
9. **(If an intake workshop exists)** RADAR ⇄ dossiers coherent, no zombie ideas, intake graveyard
   well-formed — and the boundary held: nothing in the four pillars that never got a verdict.

## Report

One consolidated **PASS / WARN / FAIL** report: per invariant, the verdict + the specific offenders
(`path:line`). End with the top fixes and **which write-command owns each** (`feature-intake` for an
orphan Ref, `decision-record` for a missing `D-NN`, etc.). Never fix anything here.
