---
name: feature-intake
description: Register a new feature/idea in a governance layer deterministically — Backlog (pre-triage) → triage gate → either kill-with-reason (derived Graveyard) or register it in release-calendar.yaml (via calendar-ops.py) with a milestone + create ONE FR per layer in the PRDs (namespaced <SUB>-FRn, each serving the new Ref) + wire the join and validate it by schema (validate-release-calendar.py). It never invents scope beyond what's agreed, never touches the spine (routes to decision-record if a spine change is needed), and never writes decisions by hand. Use when the user says "add a feature", "put X on the roadmap", "register this capability", or proposes a new product capability that already has shape. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# feature-intake

**Goal:** take a shaped capability and land it in the registry correctly — killed with a reason, or
registered as a `release-calendar.yaml` entry (a stable `Ref` handle) with one testable FR per layer it
touches, the join validated by schema. This is the delta-incremental path; a whole product line gets
`product-spec` first. Obeys the kit's operating contract (`reference/operating-contract.md`).

## On activation

Read `GOVERNANCE.md` (pillar paths, subsystems + FR namespaces, anti-drift laws), the narrative `ROADMAP.md`
+ `release-calendar.yaml` (the registry + the join), and the PRDs' current FR numbering per namespace. The
calendar is written **only** via `calendar-ops.py` (next to the yaml); never hand-edit it.

## 1 · Land it in the Backlog FIRST (pre-triage)

Every new idea enters the narrative Backlog *before* triage — even if it will obviously be committed.
`bmad-agent-pm` frames the job-to-be-done; the skill notes it as a pre-triage idea (provisional `Ref`
handle, layers = "pending triage"). Split multiple capabilities into multiple ideas. Flag an **NFR-smell**
early (an NFR → the PRD NFR section, never a calendar entry/FR) and flag "this is really an implementation
detail of an existing FR" (don't create a duplicate). Nothing is written to the calendar yet.

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
- **(c) clash with a live decision** — *deterministic grep* of the decision log + the killed calendar
  entries. If it contradicts a live `D-NN` or reopens a killed feature, don't override silently: either KILL
  (citing the decision) or supersede via `decision-record`.
- **(d) anchored/movable** — architect's call, anchored in (a-bis).
- **(e) milestone** — architect recommends; the skill enforces the closed status vocabulary.
- **(f) optional impact score** (frequency × intensity × fit) for a defensible priority.

Offer `bmad-advanced-elicitation` (pre-mortem), especially **before any KILL**.

## 3 · Route — exactly two outputs

- **KILL** → offer elicitation first; ensure/open a `D-NN` via `decision-record`. If the idea was never
  registered, it just stays out of the calendar (note the kill in the narrative Backlog). If a calendar entry
  already existed, `python3 calendar-ops.py set-status <ref> killed` + `add-decision <ref> <D-NN>` — the
  Graveyard is derived. ("Valid but no date" → narrative icebox, not killed.)
- **PROMOTE** → choose a stable `Ref` handle — **if the naming convention is unresolved, STOP and ask; never
  invent one.** Register it: `python3 calendar-ops.py add features|enablers <ref> --milestone <M>
  [--release <r>]`. A double-milestone split is two calendar entries sharing the handle stem.

## 4 · Author the FRs — one per layer

`bmad-prd` writes the prose + acceptance criteria; **the skill enforces and never cedes** the header format,
the tag `[milestone · anchored|movable · serves <Ref>]`, placement in the correct subsystem PRD/section, the
namespace + `n+1` sequence, the one-FR-per-layer rule, and NFR→NFR-section routing. **Italic/no-code layers**
(reads, approval-queue, render-surface…) mean the layer is covered inside an existing FR — don't create a
duplicate. **REJECT non-testable acceptance criteria** (tasks masquerading as assertions) back to the
command. Depth is proportional to milestone (committed = complete; hypothesis/frozen = stated + tag only).

## 5 · Wire the join in the calendar & validate

Record the FRs the feature is built from — via the script, never by editing the yaml:
`python3 calendar-ops.py add-frs <ref> <SUB>-FRn ...` (and `add-nfrs <ref> NFR-<CODE> ...`). Then run
`python3 validate-release-calendar.py` and drive it to **PASS** — it verifies both directions (every calendar
FR exists in its PRD; every `(Ref, FR)` pair confirmed by the PRD `serves <Ref>`; no orphan `serves`). Fix
here before advancing.

## 6 · Verify & report

Validator PASS; one-FR-per-layer count matches the non-italic/non-NFR layers; no silent clash; naming OK
(implementation names don't leak); and **only the calendar (via `calendar-ops.py`) + PRD(s) were edited**
(KILL: only the calendar) — the narrative `ROADMAP.md`, architecture, and the decision log were **not**
touched by hand. Report with `path:line`.
