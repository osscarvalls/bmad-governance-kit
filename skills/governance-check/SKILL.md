---
name: governance-check
description: READ-ONLY anti-drift auditor of a governance layer's four-pillar graph — runs validate-release-calendar.py to prove every Ref⇄FR closes (both directions, no orphans), checks no duplicated facts across pillars, correct FR namespacing, an append-only/coherent DECISIONS log, present anchored/movable architecture tags, a coherent derived Graveyard, and an accurate constitution. It WRAPS bmad-check-implementation-readiness (spec completeness) plus bmad-review-adversarial-general / bmad-review-edge-case-hunter (adversarial lens) and adds only the governance invariants, composing them into ONE PASS/WARN/FAIL report. It NEVER auto-fixes. Use when the user says "check the governance", "audit coherence", "governance check", or before a checkpoint / before projecting epics. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# governance-check

**Goal:** prove the governance graph is coherent — or report exactly where it drifted — **without changing a
single character.** A projection or a build inherits the quality of this graph; audit it before you rely on
it. Obeys the kit's operating contract (`reference/operating-contract.md`).

## On activation

Read `GOVERNANCE.md` (pillar paths, subsystems + namespaces, anti-drift laws to audit against). **HARD
read-only invariant, no exceptions:** never edit/create/delete any pillar, `history/`, or the intake layer.
Every WARN/FAIL carries a *suggested fix that is NOT applied* — routed to the owning skill. The only writable
file is an optional report clearly marked "not a governance document, regenerable."

## It composes THREE sources into ONE report (it is not a hand-rolled validator)

1. **Backbone → `bmad-check-implementation-readiness`** — "are the PRD/UX/Architecture/Epics specs complete
   and ready?" Its verdict is *carried* to the report, not re-derived. Where a delta assertion overlaps it,
   **defer** (`↳ confirmed by bmad-check-implementation-readiness`).
2. **Adversarial → `bmad-review-adversarial-general` + `bmad-review-edge-case-hunter`** — run BOTH (cynical
   attitude vs exhaustive branch/boundary method; orthogonal).
3. **The governance delta** — the only thing no BMAD command knows (below).

## Scope

Default = the whole graph. Accept an argument to narrow to a `Ref` / milestone / subsystem / single
invariant (if narrowed to one invariant, readiness may be deferred — say so). Read all four pillars + the
intake layer **whole** — a half-read cross produces false FAILs.

## The delta invariants (PASS / WARN / FAIL each, with `path:line` + the owning skill for the fix)

1. **Coverage.** Run `validate-release-calendar.py` — it must be **PASS** (every calendar FR exists in its
   PRD; every `(Ref, FR)` pair confirmed by the PRD `serves`; every PRD `serves <Ref>` resolves to a calendar
   entry). Carry its verdict into the report. Then the checks the validator can't make: every calendar entry
   has ≥1 FR (empty `frs[]` = orphan feature = FAIL); a live FR serving a killed-only entry = FAIL;
   coverage-gap entries explicitly marked provisional/hypothesis; the narrative Backlog is pre-triage only
   (WARN if a committed feature lingers there instead of the calendar).
2. **Decisions + intake.** No two live decisions contradict without a supersede; every SUPERSEDED has a
   paired pointer to an existing target; **reclassify ≠ supersede** (reclassified-but-live is correct); no
   calendar entry is both `status: killed` and live elsewhere; every killed entry cites a `D-NN` in its
   `decisions[]`; append-only intact (contiguous numbering, no overwrite signals, ranges match the header
   `sources:`); every `decisions[]` id resolves to a real entry. **Plus intake coherence:** RADAR ⇄ dossiers
   aligned both ways, no zombie radar-dossiers, the intake-graveyard well-formed and not overlapping the
   derived Graveyard.
3. **Architecture.** Every spine-touching feature has a footprint (missing = governance bug); every decision
   carries the full three-field tag; `serves <FRs>` resolve; the milestone-delta section is consistent with
   the ROADMAP milestones and marks backbone transitions; **nothing anchored moved silently without a
   decision** (the schema-ON/enforcement-OFF invariant holds); the header points rather than restates.
4. **Naming + duplication.** Implementation names don't leak to the product surface; brand/domain terms used
   consistently; exact milestone names + correct hypothesis/frozen/gate framing; subsystem boundaries not
   double-claimed; **the duplication check** — heuristically scan for the *same fact/rationale* copied across
   two pillars (why-not outside the log, what/order restated in architecture/PRD, how-structural copied into a
   PRD, the feature⇄FR join kept anywhere but the calendar, feature→milestone restated outside the calendar).
   Operative test: *"if changing it means editing the same sentence in two places, it's duplication."* Plus
   `history/` immutability and the one-header-comment rule on the governance yaml.

## Compose the report

Header (scope + absolute date + read-only reminder + which commands ran) → **READINESS** block →
**DELTA** block (**including PASSes** — the auditor's value is also saying what's right) → **ADVERSARIAL**
findings with severity. Each WARN/FAIL ends in "NOT applied" + the owning skill (`feature-intake` for an
orphan Ref, `decision-record` for a missing `D-NN`, etc.). Close with a one-line verdict + counts
(COHERENT / COHERENT-WITH-WARNINGS / INCOHERENT). **Never fix anything.**
