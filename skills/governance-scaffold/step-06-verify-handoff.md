# Step 06 — Verify coherence & hand off

**Objective:** prove the scaffolded governance layer is internally coherent before declaring it done, then
hand off to the next stage (epics projection / building). Nothing new is authored here — this step
**verifies** and picks up anything left loose.

## RULES

- Read-only over the four pillars, except fixing loose ends the earlier checkpoints already agreed.
- The gate is **coherence**, not opinion: the join must close, with no orphans and no duplication.

## 1 · Run the coherence gate

Prefer the BMAD gate if present: **`bmad-check-implementation-readiness`** (are the specs complete and
ready?), optionally sharpened with **`bmad-review-adversarial-general`** / **`bmad-review-edge-case-hunter`**
for an adversarial lens. If BMAD is not available, run this read-only pass yourself:

Check each invariant and record PASS / WARN / FAIL with the specific offenders:

1. **Ref ⇄ FR (both directions).** Every registry `Ref` has ≥1 FR in the Coverage Matrix; every FR
   `serves` a real `Ref`. No orphans either way.
2. **One place per fact.** No sentence duplicated across two pillars (a feature described in both ROADMAP
   and a PRD statement; an FR's text copied into architecture). Consequences propagated by shared `Ref`/
   `D-NN` are fine; copied text is not.
3. **Namespacing.** Every FR is `<PREFIX>-FRn` for a real subsystem; no stray global `FR-n`; provisional
   slugs from step-01 all resolved (promoted, moved, or parked with a reason).
4. **DECISIONS integrity.** Append-only shape; every Graveyard row has a `D-NN`; every superseded entry has
   a forward pointer; no speculative decision the plan never made.
5. **Architecture tags.** Every structural decision carries `[milestone · anchored|movable · serves <Ref>]`;
   anchored items are actually backbone; architecture restates no FR text.
6. **Registry completeness.** Everything the plan scopes appears somewhere (a milestone table, the Backlog,
   or the Graveyard) — nothing planned is "loose".
7. **Constitution accuracy.** GOVERNANCE.md's pillar paths, subsystem list, and pointers match what's on
   disk.

## 2 · Resolve loose ends

For each WARN/FAIL, either fix it (if it's a mechanical loose end the earlier checkpoints already covered)
or, if it needs a real decision (an orphan feature the plan genuinely under-specified, an unclear
milestone), **surface it to the user** as an open question — do not close it with an assumption.

## 3 · Report & hand off

Give the user a compact close-out:

- **Coherence report:** PASS/WARN/FAIL per invariant, with offenders.
- **What was written:** the four pillars + GOVERNANCE.md + supporting stores, each with its path.
- **Traceability sample:** pick one `Ref` and show the full chain — `Ref` (ROADMAP) → its FRs (PRDs) → its
  architecture tag → its `D-NN` — as proof the join closes end to end.
- **Open gaps:** anything the plan under-specified that governance surfaced (orphans, un-phased features,
  decisions never written down). These are the real value of the scaffold — the plan's blind spots, now
  visible.
- **Handoff:** the layer is ready to be *operated* by the governance command family — `decision-intake`
  (land ideas), `feature-intake` (register features), `decision-record` (log decisions),
  `tech-scout` (adopt tech), `governance-check` (audit), and `epics-projection` (project a
  milestone's epics into `_epics/`, then build). Point at `epics-projection` as the immediate next step;
  this skill's job ends at a coherent, self-describing governance layer.

## Done

The project now has a governance layer: a registry that makes "loose features" impossible, a coverage matrix
that keeps requirements traceable, an append-only decision log that never loses why-not, an architecture doc
that knows its backbone, and a constitution that states the rules. Stop here.
