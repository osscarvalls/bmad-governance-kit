---
title: "<Project> — Product Roadmap (narrative: what + order)"
status: <draft-vN | living>
created: <YYYY-MM-DD>
governance: |
  The NARRATIVE half of the ROADMAP pillar: what exists and in what order, in prose.
  The structured JOIN (feature ⇄ FR/NFR ⇄ epic ⇄ story) lives in release-calendar.yaml, not here.
  Not how (→ PRDs), not why-not (→ DECISIONS). No dates, no FR tables, no coverage matrix.
  No skill mutates this file: a human edits it (or the agent proposes an edit the human approves).
---

# <Project> — Product Roadmap

## How to read this (the model)
- **Feature** = a business capability, vertical. Named by a **`Ref`** (kebab-case handle) that is also its
  entry key in `release-calendar.yaml`. That handle is the join key stitching the feature to its layers.
- **Layer** = the slice of a feature inside **one subsystem**. The *how* of each layer lives in that
  subsystem's PRD, in an FR tagged `serves <Ref>`.
- **Milestone** = a grouping of features with a goal — a heading here, not a folder.
- **The join** — which FRs/NFRs/epics/stories a feature is built from — lives **only** in
  `release-calendar.yaml`, written via `calendar-ops.py`, validated by `validate-release-calendar.py`. This
  document carries the **order and the why**, in prose; it does not restate the join.

### The subsystems (the possible layers)
| Subsystem | The question it owns | Boundary |
|---|---|---|
| **<SubA>** | <the one question> | <in scope / explicitly out> |
| **<SubB>** | <the one question> | <boundary> |
| **<SubC>** | <the one question> | <boundary> |
| **<SubD>** | <the one question> | <boundary> |

### Governance (the five anti-drift laws)
1. **If it's not in the registry, it doesn't exist.** Registry = this narrative + `release-calendar.yaml`.
2. **ROADMAP says WHAT+ORDER; the calendar is the JOIN; PRDs say HOW; DECISIONS says WHY-NOT.** Write one
   fact in two of them → duplicating. feature→milestone lives **only** in the calendar.
3. **New idea** → the Backlog → triage → register in the calendar with a milestone or **kill with a reason**.
4. **Killed is not deleted or reopened** — the Graveyard is a **derived view** (`status: killed` in the
   calendar + the `D-NN` in DECISIONS).
5. **`epics.md` is PROJECTED from a milestone** — regenerated, not a source; the projection writes
   `epics[]`/`stories[]` back to the calendar.

---

## Milestones (in order)

### <Milestone-0> · *Objective: <goal>*  — **Active (building)**
<One or two paragraphs, in prose: what this milestone delivers, the features it groups and why, and the
order they come in. Name features by their `Ref` handle (e.g. `billing`, `agenda-sync`). No FR lists, no
tables — those are in the calendar and the PRDs.>

### <Milestone-1> · *Objective: <goal>*  — Next
<Prose: the next milestone's intent and the features it introduces, in sequence.>

### <Milestone-Hypothesis> · *Objective: <vision>*  — **Hypothesis (not committed)**
<Prose: an alternative path that only builds if later data validates it. State clearly it is a hypothesis.>

---

## Backlog (pre-triage ideas)
<Prose or a short list of raw ideas awaiting triage. If the project runs `decision-intake`, this is the
intake RADAR; each idea is registered into the calendar or killed with a reason once triaged. Additive,
never rewritten in place.>

## Graveyard (derived — do not maintain by hand)
> The Graveyard is a **view**: every calendar entry at `status: killed` + the `D-NN` in DECISIONS that
> closed it. It is not a table kept here. Killed features are never reopened.
