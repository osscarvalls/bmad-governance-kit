# Step 03 — Organize the PRD(s) & wire the join in the calendar (HOW — testable)

**Objective:** turn the plan's requirements into the second pillar — **namespaced, testable FRs**, one per
subsystem per feature, each declaring the `Ref` it `serves` — and record which FRs each feature is built from
by writing `frs[]`/`nfrs[]` into `release-calendar.yaml` (via `calendar-ops.py`). The `serves <Ref>` tag is
the FR-side of the join; the calendar's `frs[]` is the feature-side; `validate-release-calendar.py` proves
they agree, in both directions. **There is no Coverage Matrix** — the join lives only in the calendar.

## RULES

- Writes the PRD(s) under `{gov}` (or annotates the existing PRD in place if the user chose to keep it
  where it is) **and** fills each calendar entry's `frs[]`/`nfrs[]` via `calendar-ops.py`.
- **The PRD is the WHAT, testable — never the HOW.** No library names, hosting choices, or engines in a PRD;
  those belong to architecture (step-04). If a "requirement" is really an implementation decision, route it
  to architecture, not here.
- **One FR per layer.** A feature touching three subsystems → three FRs (one in each subsystem's PRD), all
  carrying the same `Ref` in `serves`.

## 1 · Decide the PRD file layout

- **One PRD per subsystem** (`{gov}/prds/prd-<subsystem>.md`) is the default for anything beyond a couple of
  subsystems — it keeps "one FR per layer" physically separated and greppable. The filenames **must match**
  the `config.subsystems` map seeded in step-02 (that is how the validator finds them).
- A **single PRD with a section per subsystem** is fine for small projects. Either way, each subsystem
  declares its **`fr_namespace`** (`<PREFIX>-FR`) at its head.

## 2 · Migrate / author the FRs

Use the bundled template `assets/templates/prd-subsystem.template.md` for each subsystem PRD (it carries the
reading-key, the FR + tag format, and the NFR section — **no coverage table**). For each feature (`Ref`) and
each subsystem it touches, write one FR in that subsystem's PRD:

- **Id:** `<PREFIX>-FRn` (namespaced; apply the old→new mapping from step-01 in merge mode, keeping the old
  id as an alias on first migration).
- **`serves <Ref>`** — in the FR's tag line `` `[<milestone> · anchored|movable · serves <Ref>]` `` — the
  join back to the calendar. This exact tag is what the validator parses; keep it on the line directly under
  the `#### <FR> — Title` header.
- **Statement:** testable — an observable behaviour, not an implementation. Reuse the plan's requirement
  wording; sharpen it to be testable, don't rewrite its meaning.
- **Acceptance criteria** where the plan provides them (from stories/epics).

Delegate the testability/completeness pass to **`bmad-prd`** (validate intent) if available.

## 3 · Split out the NFRs

Everything cross-cutting and non-functional (latency/p95, security, data residency, cost, reliability,
observability, accessibility, compliance) goes into an **NFR section** of the relevant PRD — **never** as an
FR, and never as a calendar feature. Give each NFR a stable id (`NFR-<domain>`) so architecture, tests, and
the calendar's `nfrs[]` can reference it.

## 4 · Resolve the provisional slugs

For each provisional slug from step-01 (`INT-*`/`OPS-*`/`UX-*`/`LEG-*`): either it earns a real FR here
(promote it, wire its `frs[]` in the calendar), or it is genuinely an NFR/architecture concern (move it), or
it is not yet real (leave it in the narrative Backlog). No provisional slug survives this step unresolved
without a noted reason.

## 5 · Wire the join in the calendar & validate

For each feature/enabler, record the FRs it is built from — via the script, never by editing the yaml:

```
python3 {gov}/calendar-ops.py add-frs  <ref> <SUB>-FRn <SUB>-FRm ...
python3 {gov}/calendar-ops.py add-nfrs <ref> NFR-<CODE> ...
```

Then run `python3 {gov}/validate-release-calendar.py` and drive it to **PASS**. The validator checks both
directions for you:

- **ERROR — an FR in the calendar doesn't exist in its PRD** → the `frs[]` entry is wrong or the FR wasn't
  written. Fix.
- **WARN — an FR doesn't declare `serves <ref>`** → the tag is missing/mismatched. Fix the tag.
- **WARN — a PRD `serves <ref>` has no calendar feature** → an **orphan requirement**: either register the
  feature (step-02) or the FR is dead. Resolve.
- **A feature with empty `frs[]`** is an **orphan feature** (the plan under-specified it) — flag it, don't
  paper over it.

## CHECKPOINT — Confirm coverage

Report: FR counts per subsystem, the validator's PASS/WARN/FAIL summary, and **every orphan** in either
direction with its likely cause. Orphans are the whole point of this step — surface them, don't hide them.

**Stop and wait** for the user to resolve or accept each orphan before moving to architecture.

## Next step

Read it fully and follow: `./step-04-architecture-decisions.md`.
