---
name: epics-projection
description: PROJECT epics.md from a milestone of the ROADMAP (the "epics are projected, never a source" law) — filter the milestone → resolve its features + FRs from release-calendar.yaml → DELEGATE the expansion into stories to bmad-create-epics-and-stories → order by dependencies using architecture.md (anchored first) → write a regenerable epics-<milestone>.md → generate the sprint plan via bmad-sprint-planning → write epics[]/stories[] back to the calendar (via calendar-ops.py) → hand off to the build loop. It invents nothing not in the registry. Use when the user says "project the epics for <milestone>", "generate epics.md", "prepare the stories for milestone X", or is about to start building a milestone. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# epics-projection

**Goal:** turn a milestone of the registry into an ordered, build-ready `epics.md` — a **regenerable
projection, never a source of truth** (source = the calendar + PRDs). It invents nothing; if the
calendar/PRDs change you **re-project**, never hand-patch. It writes `epics-<milestone>.md` by hand and writes
`epics[]`/`stories[]` back to the calendar via `calendar-ops.py`. Obeys the kit's operating contract
(`reference/operating-contract.md`).

## On activation

Read `GOVERNANCE.md` (pillar paths, the implementation/ location), the narrative `ROADMAP.md` +
`release-calendar.yaml` (the milestone's features + their `frs[]`), architecture (for ordering), and the PRDs
(for acceptance criteria).

## 1 · Pick the milestone & pre-flight

Ask which milestone (or accept it as an argument; accept narrowing to a single `Ref`). Load, **for that
milestone only**, its calendar entries + their `frs[]`/`nfrs[]` (`calendar-ops.py get`); **project only the
chosen entry of a double-milestone split, not the other**. Be honest about status — a hypothesis/frozen
milestone projects but the header inherits and states that; warn explicitly before projecting a frozen
milestone. Recommend (and offer to run) `governance-check` scoped to this milestone first — *a projection
inherits its source's drift* — plus optional `bmad-check-implementation-readiness`. Note it if skipped.

## 2 · Resolve + expand — the expansion IS `bmad-create-epics-and-stories`

The skill does **not** decompose, phrase stories, or write acceptance criteria. It builds the deterministic
**input** — the join `milestone → Ref → FR → ACs → tag → D-NN` from the calendar's `frs[]` + the PRDs — and
enforces two things the command doesn't know:

- the **traceability handle** `[Ref · <SUB>-FRn]` mandatory on every epic/story (without it a story isn't
  projectable), and
- the **scope frontier** (only this milestone's FRs, nothing invented).

Special cases, handled *without inventing FRs*: a feature whose slice is covered inside another FR = hang it
off the real FR; an `nfrs[]` entry = a cross-cutting constraint, not a story; a calendar entry with empty
`frs[]` = flagged as a coverage-gap risk, not projected with a fake FR. Validate the returned stories trace
back; return non-tracing ones to the command; trim out-of-frontier ones.

## 3 · Order by dependencies (anchored first — authority = architecture)

No BMAD command orders by the spine; this is in-skill. Apply deterministic rules: **anchored/backbone first,
movable after**; explicit cross-subsystem dependencies (schema before enforcement, base schemas before
consumers, spine before product capability, a base agent before concrete agents, a plane before its
consumer); phase-blockers push blocked stories behind their gate; NFRs are constraints, not ordering nodes.
**The skill does not reclassify anchored↔movable or invent dependencies** — a suspected missing spine
dependency is *reported* and routed (tech-scout → decision-record), not invented. Every non-trivial ordering
choice gets a one-line rationale citing `architecture.md:line`.

## 4 · Write the projection

`implementation/epics-<milestone>.md`, with a mandatory banner: **regenerable · projected from milestone
`<X>` on `<YYYY-MM-DD>` · source_of_truth = ROADMAP + PRDs (NOT this file) · ordering_authority =
architecture · do not hand-edit — re-project.** Group FRs into epics respecting the anchored-first order;
each story carries its handle + inherited state (blocked/hypothesis/frozen marked); reference-not-restate the
ACs. Confirm before overwriting a prior projection.

## 5 · Write back to the calendar & hand off

Write the projected epics/stories back into each feature's calendar entry — via the script, never by editing
the yaml: `python3 calendar-ops.py add-epics <ref> epic-... ` and `add-stories <ref> <M>-n.m ...`. The
calendar **references** the stories; `sprint-status.yaml` owns their list + state. Then delegate execution to
`bmad-create-story` → `bmad-dev-story` (attack order = projection order), and invoke `bmad-sprint-planning`
to generate the sprint tracker *from* this `epics.md` (delegation, not hand-written). Reaffirm law #5: a
capability discovered during build that isn't in the registry is **not** added to `epics.md` — it goes
through `feature-intake`, then re-project.

## 6 · Verify & report

Invented-nothing; round-trips both ways (calendar `frs[]` ⇄ PRDs); one-FR-per-layer; coverage-gap features
handled without invention (gaps listed as risks); anchored-first order; banner present; inherited state
correct; `epics[]`/`stories[]` written back to the calendar; naming OK. Only `epics.md` was written by hand
(the calendar write-back is via `calendar-ops.py`; the sprint tracker via the delegated command). List
prior-drift risks without fixing; recommend a final `governance-check`.
