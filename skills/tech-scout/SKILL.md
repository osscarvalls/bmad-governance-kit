---
name: tech-scout
description: Scout a technology/library/service/vendor for adoption into a governed project — research it (delegating to bmad-technical-research), evaluate it against the architecture spine (boring-tech, maintainable by a small team, fits the spine, honours the project's constraints like data residency/cost/licence) → if adopted, record the decision via decision-record and propagate its footprint to architecture/PRD/ROADMAP; if doubtful, open a spike / phase-blocker instead of adopting. Use when the user says "scout technology X", "should we add Z to the stack", "evaluate library Y for integration", or wants to assess a technology/service for the product. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# tech-scout

**Goal:** decide whether a technology earns a place in the stack, on evidence, judged against the spine —
and if yes, land the decision + its structural footprint through the governance pillars (not by hand).

## On activation

1. **Resolve the layer.** Read `{gov}/GOVERNANCE.md` for the pillar paths, the subsystem set, and any
   standing constraints (residency, cost ceiling, licence policy, "boring-tech" bias, team size). No layer →
   run `governance-scaffold` first.
2. **Read architecture.md §A (spine)** so you evaluate fit against the real backbone, not a guess.
3. Delegate the research to **`bmad-technical-research`** (the report) and the trade-off/spine-fit judgement
   to **`bmad-agent-architect`** (Winston), if available.

## Procedure

### 1 · Research
Produce (or have `bmad-technical-research` produce) an evidence-based report: what it is, maturity, the real
alternatives, operational cost, licence, security/residency posture, and the migration/lock-in risk.

### 2 · Evaluate against the spine (the boring-tech lens)
- **Fit:** does it slot into the spine, or force a retrofit of an `anchored` element?
- **Boring & maintainable:** could a small team own it in a year? Prefer boring, proven tech over novelty.
- **Constraints:** does it honour the project's standing constraints (residency, cost, licence, security)?
- **Clash:** does adopting it contradict a **live** `D-NN`?

### 3 · Verdict
- **Adopt** → invoke **`decision-record`** to log the decision (`D-NN`, why-not = the rejected
  alternatives), then propagate the footprint:
  - **architecture.md** — the structural decision, tagged `[milestone · anchored|movable · serves <Ref>]`.
  - **PRD** — only if adoption changes an FR's testable behaviour (usually it doesn't — a library is a HOW,
    which belongs in architecture, not the PRD).
  - **ROADMAP** — if it unblocks/schedules a feature, update that `Ref`'s row.
- **Doubtful** → don't adopt. Open a **spike / phase-blocker**: a time-boxed investigation registered as
  such (a Backlog row or an architecture open-question), with the specific question that must be answered
  before it can be adopted. Route to `decision-intake` if the doubt is really product/business, not tech.
- **Reject** → record the why-not via `decision-record` so it isn't re-scouted later.

## Report

Show: the evaluation against each lens (fit / boring / constraints / clash), the verdict, and — if adopted —
the `D-NN` recorded and the architecture/PRD/ROADMAP footprint propagated. A HOW-level pick lands in
architecture, never in the PRD.
