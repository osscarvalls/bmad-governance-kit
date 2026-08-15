# Step 03 — Organize the PRD(s) & close the Coverage Matrix (HOW — testable)

**Objective:** turn the plan's requirements into the second pillar — **namespaced, testable FRs**, one per
subsystem per feature, each declaring the `Ref` it `serves` — and use them to **fill the Coverage Matrix**
so the `Ref`⇄FR join is complete and honest in both directions.

## RULES

- Writes the PRD(s) under `{gov}` (or annotates the existing PRD in place if the user chose to keep it
  where it is) **and** fills the Coverage Matrix rows left open in step-02.
- **The PRD is the WHAT, testable — never the HOW.** No library names, hosting choices, or engines in a PRD;
  those belong to architecture (step-04). If a "requirement" is really an implementation decision, route it
  to architecture, not here.
- **One FR per layer.** A feature touching three subsystems → three FRs (one in each subsystem's PRD), all
  carrying the same `Ref` in `serves`.

## 1 · Decide the PRD file layout

- **One PRD per subsystem** (`{gov}/prd/prd-<subsystem>.md`) is the default for anything beyond a couple of
  subsystems — it keeps "one FR per layer" physically separated and greppable.
- A **single PRD with a section per subsystem** is fine for small projects. Either way, each subsystem
  declares its **`fr_namespace`** (`<PREFIX>-FR`) at its head.

## 2 · Migrate / author the FRs

Use the bundled template `assets/templates/prd-subsystem.template.md` for each subsystem PRD (it carries the
reading-key, the FR + tag format, the NFR section, and the local coverage table). For each feature (`Ref`)
and each subsystem it touches, write one FR in that subsystem's PRD:

- **Id:** `<PREFIX>-FRn` (namespaced; apply the old→new mapping from step-01 in merge mode, keeping the old
  id as an alias on first migration).
- **`serves <Ref>`** — the join back to the registry.
- **Statement:** testable — an observable behaviour, not an implementation. Reuse the plan's requirement
  wording; sharpen it to be testable, don't rewrite its meaning.
- **Acceptance criteria** where the plan provides them (from stories/epics).

Delegate the testability/completeness pass to **`bmad-prd`** (validate intent) if available.

## 3 · Split out the NFRs

Everything cross-cutting and non-functional (latency/p95, security, data residency, cost, reliability,
observability, accessibility, compliance) goes into an **NFR section** of the relevant PRD — **never** as an
FR, and never as a registry feature. Give each NFR a stable id (`NFR-<domain>`) so architecture and tests
can reference it.

## 4 · Resolve the provisional slugs

For each provisional slug from step-01 (`INT-*`/`OPS-*`/`UX-*`/`LEG-*`): either it earns a real FR here
(promote it, update its `Ref` row and the matrix), or it is genuinely an NFR/architecture concern (move it),
or it is not yet real (leave it in the Backlog). No provisional slug survives this step unresolved without a
noted reason.

## 5 · Close the Coverage Matrix

Now fill the matrix rows in `ROADMAP.md`: for each `Ref`, list its FR id in each subsystem column (`·` where
that subsystem has no layer for it). Then verify **both directions**:

- **Every `Ref` has at least one FR.** A registry row with an empty matrix line is an **orphan feature** —
  flag it (the plan under-specified it) rather than papering over it.
- **Every FR serves a `Ref`.** An FR with no `Ref` is an **orphan requirement** — either it belongs to an
  unregistered feature (register it in the Backlog) or it is dead (note it).

## CHECKPOINT — Confirm coverage

Report: FR counts per subsystem, the completed Coverage Matrix, and **every orphan** in either direction
with its likely cause. Orphans are the whole point of this step — surface them, don't hide them.

**Stop and wait** for the user to resolve or accept each orphan before moving to architecture.

## Next step

Read it fully and follow: `./step-04-architecture-decisions.md`.
