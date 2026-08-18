---
name: governance-scaffold
description: Scaffold a durable governance layer onto a project that has already been planned with BMAD. Reads the existing BMAD planning artifacts (product brief, PRD, architecture, epics/stories) and projects them into a four-pillar "one truth, one place" topology — a ROADMAP registry (a narrative ROADMAP.md for what+order plus release-calendar.yaml as the single structured feature⇄FR join, written via calendar-ops.py and schema-validated), namespaced PRDs (HOW-testable), an append-only DECISIONS log (WHY-NOT), and an architecture doc with a spine + anchored/movable tags (HOW-structural) — plus a GOVERNANCE constitution that states the anti-drift rules. Portable and project-agnostic; does not add product features, it organizes what planning already produced so the project can be operated without drift. Use when the user says "scaffold the governance layer", "set up governance for this project", "bring this BMAD plan under governance", "add a governance layer", or has a BMAD-planned project with no registry/decision-log/coverage discipline yet.
---

# governance-scaffold

**Goal:** take a project that has **already been planned with BMAD** (it has some subset of: a product
brief, one or more PRDs, an architecture/solution-design doc, an epics-and-stories breakdown, a sprint
plan) and **scaffold a governance layer** onto it — the durable structure that keeps a project from
drifting once many people and many sessions start touching it. This skill **does not invent product
scope**. It **reads** what planning produced and **projects** it into a small, opinionated topology with
explicit join keys, then writes the rules that keep that topology honest.

**CRITICAL:** if a step says "read it fully and follow step-XX", you read it fully and follow it. No
exceptions. Never load more than one step file at a time; never skip a step.

## What a governance layer is (the model this skill installs)

Four **co-equal pillars** — each owns exactly one question, and nothing is written in two of them:

| Pillar | Owns | Rule |
|---|---|---|
| **ROADMAP** (`ROADMAP.md` + `release-calendar.yaml`) | **WHAT + ORDER + the join** — a **narrative `ROADMAP.md`** (milestones → features in prose, order + why; no dates, no FR tables) + **`release-calendar.yaml`**, the single *structured* join (feature/enabler → milestone → FRs/NFRs → epics → stories, with status + `decisions[]`). | The single source of "what exists and in what order". Says neither *how* nor *why-not*. The narrative is human-edited; the yaml is written only via `calendar-ops.py`. |
| **PRD(s)** | **HOW — testable** — Functional Requirements, testable, **namespaced per subsystem/layer** (`<SUB>-FRn`); non-functional requirements live in **NFR sections**, never as FRs. | Each subsystem's requirements live in its own PRD. Every FR declares which `Ref` it `serves` — the FR-side of the join the validator checks. No coverage table in the PRD. |
| **DECISIONS.md** | **WHY-NOT** — an **append-only** log of closed decisions (`D-NN`), with forward supersede/reframe pointers. | Index of what was decided and killed. Never edited in place. Long rationale/evidence goes to `history/`. |
| **architecture.md** | **HOW — structural** — the invariant **spine** (§A), per-subsystem structure (§B), milestone deltas (§C); every decision tagged `[milestone · anchored\|movable · serves <Ref>]`. | Points at ROADMAP/DECISIONS/PRD, never restates them. A feature that touches the spine leaves its mark here. |

**This skill lays the substrate; the governance command family operates it.** Scaffolding the four documents is
half the system — a governance layer stays alive only through the commands that maintain it:
`decision-intake` (land a raw idea → verdict), `feature-intake` (register a feature → FRs),
`decision-record` (log a closed decision → propagate), `tech-scout` (adopt a technology),
`governance-check` (read-only coherence audit), and `epics-projection` (project a milestone's epics).
step-05 writes this process→command catalog into the project's GOVERNANCE.md.

Plus a **constitution** and two supporting stores:

- **GOVERNANCE.md** — the rules (the anti-drift laws + the topology map). Loaded every session; if a helper
  script and this document disagree, this document wins.
- **`history/`** — archived evidence (meeting notes, superseded docs). Append/archive only; never edited.
- **`implementation/`** (regenerable) — epics **projected** from a milestone. Not a source of truth.

Plus the two **calendar scripts**, copied next to `release-calendar.yaml` from this skill's
`assets/scripts/`: **`calendar-ops.py`** (the only sanctioned writer of the yaml) and
**`validate-release-calendar.py`** (the schema check of the join). They need Python 3 + PyYAML.

**The navigable chain:** a *feature* (a `<Ref>` entry in `release-calendar.yaml`, named in the narrative
ROADMAP) ⇄ its *FRs* (one per subsystem it touches, in the PRDs, each `serves <Ref>`) ⇄ the *how*
(architecture.md) ⇄ the *why-not* (`D-NN` in DECISIONS). The `Ref` is the join key; the join lives only in
the calendar.

## The anti-drift laws (this skill writes them into GOVERNANCE.md)

1. **If it is not in the registry, it does not exist.** Registry = narrative `ROADMAP.md` + `release-calendar.yaml`.
2. **ROADMAP=WHAT+ORDER · calendar=the JOIN · PRD=HOW-testable · architecture=HOW-structural ·
   DECISIONS=WHY-NOT.** If a change makes you write the *same fact* in two of them, stop — you are
   duplicating. (Propagating a *consequence* — a status in the calendar, a new FR in a PRD, a spine decision
   in architecture — is not duplication: those are different facts joined by the `Ref`/`D-NN`.)
   feature→milestone lives **only** in the calendar.
3. **New idea → the Backlog.** Then triage: which subsystem? does it fit the spine? anchored or movable? →
   register it in the calendar with a milestone **or kill it with a reason**.
4. **Killed things are not deleted or reopened.** The **Graveyard is a derived view**: `status: killed` in
   the calendar (with `decisions[]`) + the `D-NN` that closed them.
5. **`epics.md` is PROJECTED from a milestone** and is regenerable — never a source of truth; the projection
   writes `epics[]`/`stories[]` back to the calendar.

## Invariant patterns

- **`Ref` is the join key.** The feature's kebab-case handle = its calendar entry key; `grep` a `Ref` across
  the PRDs → every layer it touches. The join itself lives only in `release-calendar.yaml`.
- **One FR per layer.** A feature touching three subsystems → **three FRs** in three PRDs, all with the
  same `Ref` in their `serves`. An NFR (latency, security, residency, observability) → the **NFR section**,
  not an FR.
- **`anchored` vs `movable`.** *anchored* = backbone/irretrofittable (moving it costs a retrofit → a
  conscious decision). *movable* = reschedulable freely. architecture.md is the home of the tag.
- **Append-only decisions.** A decision that changes on the merits = a **new** entry (+ a `SUPERSEDED-BY`
  pointer on the old one). A decision that is only reframed = the old entry stays live + a reframe pointer.
- **Affirmative · timeless · additive.** Durable knowledge states what **is**, never what is not, and avoids
  claims that expire ("nascent", "there is no X yet"). When state changes, add or supersede.
- **Absolute dates** (`2026-08-15`), never relative ("last week").
- **Reference, don't restate.** Cite the `Ref`/`FR`/`D-NN` instead of copying its content.

## Delegation (BMAD does the thinking; this skill does the topology)

This skill's job is **topology + sequence + discipline**, not analysis. Where a judgement call is needed it
delegates to a BMAD command **if BMAD is available in the project**, and **degrades gracefully** (does the
call itself, and says so) if it is not:

- **`bmad-agent-architect` (Winston)** — classify each structural decision as `anchored`/`movable` and
  confirm the spine (step-04). Read-only consult for "does this fit the spine?".
- **`bmad-agent-pm` (John)** — frame each registry feature as a job-to-be-done and confirm subsystem
  boundaries (step-01, step-02).
- **`bmad-check-implementation-readiness`** — the final completeness/coherence gate over the scaffolded
  layer (step-06). If absent, this skill runs its own read-only coherence pass instead.
- **`bmad-review-adversarial-general` / `bmad-review-edge-case-hunter`** — optional adversarial lens on the
  scaffold before handoff.

> **Golden rule:** could a BMAD command do this step? Then it does. This skill contributes only what BMAD
> has no concept of: **which pillar** a fact belongs to, the **format**, the **sequence**, and the
> **discipline** (append-only, coverage, no-duplication, anchored/movable, registry-or-it-doesn't-exist).

## Conventions

- Bare paths (e.g. `step-00-inventory.md`) resolve from this skill's root.
- `{skill-root}` = this skill's install directory. `{project-root}` = the project being scaffolded.
- `{gov}` = the governance directory this skill writes (default `{project-root}/governance/`, confirmed with
  the user in step-00). `{plan}` = wherever the BMAD planning artifacts live (detected in step-00).
- **Language:** converse in the user's language. When **editing/creating** a governance document, match the
  language already used by the source planning docs; never translate a document on the fly.
- **This skill only writes under `{gov}`** and only reorganizes/annotates the PRD(s). It never rewrites
  product scope and never edits `{plan}` evidence in place — the plan is the input, the governance layer is
  the output.

## Workflow architecture

Step-file architecture for disciplined execution. Micro-files, just-in-time loading, forced sequence.

1. **READ THE WHOLE step file** before acting.
2. **FOLLOW THE SEQUENCE** — run sections in order.
3. **WAIT AT CHECKPOINTS** for the user's answer.
4. **LOAD THE NEXT** step only when the current one tells you to; read it fully.

### Critical rules (no exceptions)

- **Never** load several step files at once, and **never** skip a step.
- **Idempotent & non-destructive:** if a governance file already exists, you **merge/extend**, you never
  clobber. Scaffolding a partially-governed project is a valid mode — detect it in step-00.
- **No invented scope:** every registry `Ref` and every FR traces back to something the BMAD plan already
  says. If planning is silent on something the topology needs, you **flag a gap** and ask — you do not fill
  it with an assumption.
- **One fact, one place:** while projecting, if you are about to write the same sentence into two pillars,
  stop and pick the one that owns it; the others reference it.
- **Incremental consolidation:** each step writes its pillar when it closes. Nothing is "dumped at the end";
  step-06 only *verifies* and picks up anything left loose.

## First step

Read it fully and follow: `./step-00-inventory.md`.
