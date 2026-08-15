---
name: tech-scout
description: Scout a technology/library/service/vendor for adoption into a governed project — research it (delegating to bmad-technical-research), evaluate it against the architecture spine (boring-tech, small-team-maintainable, fits the spine, honours the project's constraints like data residency/cost/licence) → if adopted, record the decision via decision-record and propagate its footprint to architecture/PRD/ROADMAP; if the doubt is empirical, open a spike/phase-blocker instead of adopting. Use when the user says "scout technology X", "should we add Z to the stack", "evaluate library Y for integration", or wants to assess a technology/service. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# tech-scout

**Goal:** decide whether a technology earns a place in the stack, on evidence, judged against the spine — and
if yes, land the decision + its structural footprint through the pillars (not by hand). Obeys the kit's
operating contract (`reference/operating-contract.md`).

## On activation

Read `GOVERNANCE.md` + **architecture §A (the spine)** so you evaluate fit against the real backbone.
Open/resume a tech dossier + RADAR row before launching research (intake discipline). If the *capability
itself* is new (not in the registry), the correct entry point may be `feature-intake` first.

## 1 · Frame the integration question

Turn "I want X" into a well-formed question, then enumerate the **hard spine constraints** any candidate
must satisfy — as a **checklist the report must answer, not a verdict**: data residency; managed-vs-self-
operated + version-pinnability; small-team maintainability; fit with existing spine components vs introducing
a new plane; latency budget if on the hot path; whether it touches an already-marked backbone transition.

## 2 · Research — delegate ENTIRELY to `bmad-technical-research`

The skill's job is to *delegate well*: pass the frame + spine constraints as **explicit research goals**
(residency, managed, maintainability, spine-fit, **serious alternatives + why-yes/why-no each**, maturity /
licence / lock-in / security) so the report addresses them head-on. Record the exact report path — it is the
evidence the decision will cite. No checkpoint here (research is input); do not pre-empt the verdict.

## 3 · Evaluate — delegate the verdict to `bmad-agent-architect`

The architect renders one of three verdicts with the boring-tech bias, the small-team filter, explicit
trade-offs, and **alternatives-and-why-not** (this why-not is the material the decision needs):

- **ADOPT** — fits, cleared, acceptable trade-offs.
- **REJECT** — it closes → Graveyard via a decision.
- **SPIKE-FIRST** — it does **not** close. A hard *empirical* unknown, parked with a phase-blocker: **owner +
  absolute deadline + the binary question to answer.** Adoption is blocked until answered. ("Doubt from lack
  of empirical evidence, not from analysis" = spike, not reject.)

Leave the intake trail: the verdict to the dossier, discarded vendors/alternatives to the intake-graveyard
granularly.

## 4 · Route by verdict

- **ADOPT** → invoke `decision-record` with the five fields pre-drafted + the propagation context (subsystem,
  Refs/FRs served, anchored/movable + milestone, "touches the spine → architecture edit"). Dossier →
  promoted + archived to `history/`.
- **REJECT** → `decision-record` with verb KILLS (Graveyard with reason + id). **Ends here** — skip the
  propagation-verify step (no structural footprint).
- **SPIKE-FIRST** → the *only* branch where this skill edits docs by hand: a ROADMAP row set to `blocked`
  (citing the spike) + a **phase-blocker** in architecture's open-questions section with the three mandatory
  fields. **Adopt nothing.** Re-run from step 3 when the spike answers. Route to `decision-intake` if the
  doubt is really product/business, not tech.

## 5 · Verify propagation (ADOPT only)

The *material* propagation was done by `decision-record`; **verify** the three distinct footprints landed
(architecture HOW-structural in the right section with the tag, authored by the architect; PRD HOW-testable
FRs with the id; ROADMAP handle + Coverage cell), stitched by the id, **no duplication.** A missing footprint
is completed *through `decision-record`* (the owner of propagation), not patched here.

## 6 · Report

Branch-specific: ADOPT = id + three footprints; REJECT = id KILLS + Graveyard, no adoption footprint;
SPIKE = blocked row + phase-blocker + nothing adopted. Confirm the intake trail is complete and only the docs
the branch permits were touched. Recommend `governance-check`.
