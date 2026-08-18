---
name: product-spec
description: The SPECIFY phase between DIAGNOSE (decision-intake) and GOVERN (feature-intake) — take a whole product line / milestone from "diagnosed" (or "scattered and half-done") to a canonical, complete spec: brief → full journey set → deep PRDs (the WHAT) → UX → landed architecture (the HOW, in service of the WHAT). It wraps the BMAD authoring commands at their real depth and adds two deltas no command has — a carry-down contract (no intake insight is dropped) and a completeness gate (not just coherence) — foundation-up. Two modes: greenfield (from an approved intake verdict = product line) and reconcile (a scattered/half-done spec → reconcile first). feature-intake remains for the incremental delta. Use when the user says "specify the product/milestone X", "build the spec of <line>", "reconcile the spec of <milestone>", after a decision-intake product-line verdict, or before projecting epics of a from-zero line. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# product-spec

**Goal:** take a **product line / milestone** from diagnosed (or scattered and half-done) to a **canonical,
complete spec** — brief + full journey set + deep PRDs (the WHAT) + UX + landed architecture (the HOW, in
service of the WHAT) — wrapping the BMAD authoring commands *at their real depth*, with the discipline that
kills under-specification. It fills the hole between DIAGNOSE (`decision-intake`) and GOVERN
(`feature-intake`): a single feature *is* one-FR-per-layer, but a whole line shredded into N disconnected
features loses the brief, the journey set, the deep PRD, the architecture landing, and the completeness gate.
`feature-intake` stays for the *incremental delta*. Obeys the kit's operating contract
(`reference/operating-contract.md`).

## Two entry modes

- **Greenfield** — from an approved intake dossier (a `decision-intake` "product line" verdict).
- **Reconcile** — the spec already exists scattered/half-done (paused brief, PRDs founded on stale journeys,
  decisions not fully landed, bad premises) → **reconcile first, then build.**

## The three discipline deltas (no BMAD command has these — the heart of it)

1. **Carry-down contract** — no intake/reconciliation insight may disappear: it lands in brief/PRD/
   architecture, **or** is parked *with a reason* in a **carry-down ledger** that travels through every
   phase. The final gate FAILS if any ledger row is unresolved.
2. **Completeness gate (not just coherence)** — `governance-check` audits coherence (Ref⇄FR, orphans); this
   gate audits *completeness*: does the journey set cover the surface? does each subsystem have its FRs+NFRs?
   is architecture landed? is the Assumptions Index visible for sign-off? is the ledger resolved?
3. **Foundation-up** — no phase advances with the previous one half-done.

## The rule that is never crossed (QUÉ vs CÓMO)

**The PRD holds everything the product does (the WHAT), WITHOUT implementation.** Any library/service/engine/
hosting/gating is HOW → architecture, never the PRD; a concrete architecture never changes the PRD.

## Step sequence

| Step | Phase | Delegates to | Gate |
|---|---|---|---|
| 00 | Scope & assemble | — (in-skill topology) | CHECKPOINT |
| 01 | Reconcile *(brownfield)* | `bmad-agent-pm` + `bmad-agent-analyst`; `bmad-correct-course`; `bmad-advanced-elicitation`; architect read-only | KILL/FIX |
| 02 | Brief (to completeness) | `bmad-product-brief` | CHECKPOINT |
| 03 | Full journey set | `bmad-prd` (journeys) / `bmad-ux` | CHECKPOINT |
| 04 | PRD build (per subsystem) | `bmad-prd` + validate/readiness | CHECKPOINT per subsystem |
| 05 | UX/UI (first-class, BEFORE architecture) | `bmad-ux` / design pipeline | CHECKPOINT |
| 06 | Architecture (resolve HOW + land spine) | `tech-scout` (open questions) → `bmad-create-architecture` UPDATE | CHECKPOINT |
| 07 | Govern + completeness gate + handoff | `decision-record` · `governance-check` | FINAL GATE |

**Load-bearing nuances:**

- **00 · assemble.** Detect the mode (any prior brief / FRs-with-`serves` / decisions ⇒ Reconcile). Assemble
  **everything** — live + archived intake, the paused brief (incl. its decision-log), PRD FRs *and what
  journeys they're founded on*, decisions, ROADMAP + Coverage, architecture notes, the todo queues. Build a
  "spec-state map" surfacing gaps + suspect premises. In greenfield, load step-01 anyway, declare the
  exemption, and **open the carry-down ledger from the dossier.**
- **01 · reconcile.** Enumerate every live premise/decision/insight with its source; mark three pathologies
  (contradictions, stale/false premises, orphaned intake insights that never came down); **correct premises
  WITH the human** (open questions, take a position, anti-sycophancy); reclassify moved/killed items via
  `bmad-correct-course` (recorded later in step-07, never by hand). Produce a reconciled foundation. **Gate:
  nothing advances until the human signs the corrections.**
- **02 · brief.** Update a paused brief rather than tossing it; feed the reconciled foundation + corrected
  premises + ledger; reject a one-pager for a large line; close ledger rows destined for the brief; keep the
  topology (the brief points to FRs/architecture, doesn't restate).
- **03 · journeys.** **Enumerate the entire surface before writing any journey** — every real job, not
  headlines; one journey per job; globally numbered so FRs can reference them. **Exhaustiveness IS this
  step's gate** — ask the human explicitly "what real job has no journey?"
- **04 · PRD build.** Full template per subsystem the line touches; the same topology as `feature-intake` at
  product scale (one-FR-per-layer, tag, namespace `n+1`, NFR→NFR-section); **each FR references its
  journey(s)** (`realizes UJ-N`) — the journey→FR trace is the antidote to under-specification; stale-founded
  FRs get rewritten/retired. **Consolidate incrementally at close** (register features + wire `frs[]` in the
  calendar via `calendar-ops.py`, kill stale entries with their `D-NN`, register product decisions via
  `decision-record`, keep the validator PASS) — not deferred to step-07.
- **05 · UX (before architecture).** UX is a first-class spec, not deferred. If a design pipeline exists,
  enter it **at the design layer only, consuming the brief + journeys + PRDs** — never fire its own brief/
  research/PRD phases (that creates a satellite spec). If design reveals a missing WHAT, it goes back to the
  PRD; the interface HOW informs architecture, never leaks into the PRD.
- **06 · architecture.** (A) **resolve the HOW** by running `tech-scout` per open architecture question;
  (B) **land the spine** via `bmad-create-architecture` in **UPDATE mode** — **critical:** architecture is a
  canonical governance doc, not a workflow-generated one; a fresh run would overwrite it. Load the existing
  doc as current state and land new decisions as deltas. Architecture is the house of the anchored/movable
  tag; if an FR tag contradicts, reconcile *toward architecture* and fix the FR.
- **07 · govern + gate + handoff.** Consolidation is incremental (verify, don't do-first-time-here); run
  `governance-check` scoped to the line; **the completeness gate** asserts PASS/FAIL and does not hand off
  with any FAIL (journeys cover the surface, each subsystem PRD complete with FRs+NFRs, architecture landed
  with consistent tags, Assumptions Index visible for sign-off, carry-down ledger fully resolved) — a FAIL
  sends you *back to the owning phase* (foundation-up). Then **handoff to `epics-projection`** with the
  human's sign-off.

## Guardrails

An authoring skill (writes brief, journeys, PRDs, architecture) but **always through the BMAD command +
respecting topology**; never writes the decision log by hand (append-only, via `decision-record`); never
edits the intake workshop (reads it to recover insights). Routes **out** to `epics-projection`; routes **in**
from `decision-intake`'s "product-line" verdict.
