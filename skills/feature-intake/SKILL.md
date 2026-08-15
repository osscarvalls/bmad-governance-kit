---
name: feature-intake
description: Register a new feature/idea in a governance layer deterministically — Backlog (idea state) → triage gate → either kill-with-reason (Graveyard) or assign a milestone + create ONE FR per layer in the PRDs (namespaced <SUB>-FRn, each serving the new Ref) + update the Coverage Matrix. It never invents scope beyond what's agreed, never touches the spine (routes to decision-record if a spine change is needed), and never writes decisions by hand. Use when the user says "add a feature", "put X on the roadmap", "register this capability", or proposes a new product capability that already has shape. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# feature-intake

**Goal:** take a shaped capability and land it in the registry correctly — killed with a reason, or
registered with a stable `Ref` and one testable FR per layer it touches, with the Coverage Matrix kept
honest. This is the delta-incremental path; a whole product line gets `product-spec` first. Obeys the kit's
operating contract (`reference/operating-contract.md`).

## On activation

Read `GOVERNANCE.md` (pillar paths, subsystems + FR namespaces, anti-drift laws) and the ROADMAP (registry,
Coverage Matrix, Backlog, Graveyard) + the PRDs' current FR numbering per namespace.

## 1 · Land it in the Backlog FIRST (as `state=idea`)

Every new idea enters as a Backlog row *before* triage — even if it will obviously be committed. `bmad-agent-pm`
frames the job-to-be-done; the skill writes the row (provisional `Ref`, layers = "pending triage",
state = idea). Split multiple capabilities into multiple rows. Flag an **NFR-smell** early (an NFR → the PRD
NFR section, never a row/FR) and flag "this is really an implementation detail of an existing FR" (don't
create a duplicate).

## 2 · The triage gate (a 6-check ordered routine)

Substantive judgements delegate to `bmad-agent-architect`; the mechanics stay deterministic:

- **(a) which subsystem(s)** — the subsystem boundary table is the deterministic input; the *fine fit* (a
  feature straddling two) is the architect's call. Don't duplicate layers.
- **(a-bis) spine consult — the critical gate.** Read architecture read-only: fits-spine / fits-with-delta /
  *introduces a NEW spine element*. **If it introduces a new spine/anchored element, STOP and route through
  `decision-record`** (which assigns the id, edits architecture, propagates) *before* promoting the row as
  anchored. **feature-intake consults but never edits architecture.**
- **(b) small-team filter** — architect: can a couple of engineers build *and maintain* it? pass / fail /
  pass-with-trim.
- **(c) clash with a live decision** — *deterministic grep* of the decision log + graveyard. If it
  contradicts a live `D-NN` or reopens a graveyard item, don't override silently: either KILL (citing the
  decision) or supersede via `decision-record`.
- **(d) anchored/movable** — architect's call, anchored in (a-bis).
- **(e) milestone** — architect recommends; the skill enforces the closed status vocabulary.
- **(f) optional impact score** (frequency × intensity × fit) for a defensible priority.

Offer `bmad-advanced-elicitation` (pre-mortem), especially **before any KILL**.

## 3 · Route — exactly two outputs

- **KILL** → offer elicitation first; ensure/open a `D-NN` via `decision-record`; move the row Backlog →
  Graveyard with reason + id. ("Valid but no date" → icebox, not graveyard.)
- **PROMOTE** → assign a stable `Ref` — **if the numbering convention is unresolved, STOP and ask; never
  invent an id.** Handle double-milestone splits (two rows, same `Ref`). Move the row into the milestone
  table with the exact format + closed status vocabulary.

## 4 · Author the FRs — one per layer

`bmad-prd` writes the prose + acceptance criteria; **the skill enforces and never cedes** the header format,
the tag `[milestone · anchored|movable · serves <Ref>]`, placement in the correct subsystem PRD/section, the
namespace + `n+1` sequence, the one-FR-per-layer rule, and NFR→NFR-section routing. **Italic/no-code layers**
(reads, approval-queue, render-surface…) mean the layer is covered inside an existing FR — don't create a
duplicate. **REJECT non-testable acceptance criteria** (tasks masquerading as assertions) back to the
command. Depth is proportional to milestone (committed = complete; hypothesis/frozen = stated + tag only).

## 5 · Coverage Matrix

Add/extend the `Ref` row; verify the chain **both directions** (Ref → FRs lists exactly the created FRs;
each FR's `serves <Ref>` resolves to a real row). Fix here before advancing.

## 6 · Verify & report

No orphans; Ref⇄FR both ways; one-FR-per-layer count matches the non-italic/non-NFR layers; no silent clash;
naming OK (implementation names don't leak); and **only ROADMAP + PRD(s) were edited** (KILL: only ROADMAP)
— architecture and the decision log were **not** touched by hand. Report with `path:line`.
