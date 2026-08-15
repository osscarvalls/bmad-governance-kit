---
title: "<Project> — Product Roadmap (source of truth)"
status: <draft-vN | living>
created: <YYYY-MM-DD>
governance: |
  SINGLE SOURCE OF TRUTH for "what exists and when". Not how (→ PRDs), not why (→ DECISIONS).
  One fact, one place.
---

# <Project> — Product Roadmap

## How to read this (the model)
- **Feature** = a business capability, vertical. 1 row = 1 `Ref` = 1 milestone. The only thing with "one single place".
- **Layer** = the slice of a feature inside **one subsystem**. The *how* of each layer lives in that subsystem's PRD, tagged with the `Ref`.
- **Milestone** = a grouping of features with a goal — a column + heading, not a folder.
- **`Ref`** = the stable join key stitching a roadmap row to its layers in the PRDs.

### The subsystems (the possible layers)
| Subsystem | The question it owns | Boundary |
|---|---|---|
| **<SubA>** | <the one question> | <in scope / explicitly out> |
| **<SubB>** | <the one question> | <boundary> |
| **<SubC>** | <the one question> | <boundary> |
| **<SubD>** | <the one question> | <boundary> |

### Governance (the five anti-drift laws)
1. **If it's not in this registry, it doesn't exist.**
2. **ROADMAP says WHEN; PRDs say HOW; DECISIONS says WHY-NOT.** Edit two of three for one fact → duplicating.
3. **New idea** → row `state=idea`, `milestone=Backlog` → triage → assign a milestone or **kill with a reason**.
4. **Killed is not deleted or reopened** — Graveyard, with reason + `D-NN`.
5. **`epics.md` is PROJECTED from a milestone** — regenerated, not a source.

### States
`idea` · `committed` · `committed (schema/scaffold — enforcement OFF)` · `blocked` · `hypothesis` · `frozen` · `deferred (gate)` · `killed`

---

## Milestones
| Milestone | Objective | State |
|---|---|---|
| **<Milestone-0>** | <one-line goal> | **Active (building)** |
| **<Milestone-1>** | <one-line goal> | Next |
| **<Milestone-Hypothesis>** | **HYPOTHESIS not committed.** <one-line vision> | Hypothesis |

---

## <Milestone-0> · *Objective: <goal>*
| Ref | Feature (JTBD) | Layers | State | Decision |
|---|---|---|---|---|
| <Ref-1> | <one-line JTBD> | <SubA>, <SubD> | committed | <D-NN> |
| <ARCH-slug> | <one-line architectural capability> | <SubA> | committed | — |
<!-- ARCH-*/INT-*/OPS-*/UX-*/LEG-* slugs are PROVISIONAL until a PRD gives them their FR(s). -->

## <Milestone-1> · *Objective: <goal>*
| Ref | Feature (JTBD) | Layers | State | Decision |
|---|---|---|---|---|
| <Ref-N> | <one-line JTBD> | <SubA>, <SubB>, <SubD> | committed | <D-NN> |

---

## Coverage Matrix — feature → layers → FRs
<!-- The navigable chain both ways. One sub-table per milestone. Cell = the FR(s) that subsystem
     contributes; `·` = no layer; *(reads)*/*(intake)* = participates but no own FR. -->

### <Milestone-0>
| Ref | <SubA> | <SubB> | <SubC> | <SubD> |
|---|---|---|---|---|
| <Ref-1> | <SUBA-FR6,8> | · | · | <SUBD-FR1,2> |
| <ARCH-slug> | <SUBA-FR1> | · | · | · |

### <Milestone-1>
| Ref | <SubA> | <SubB> | <SubC> | <SubD> |
|---|---|---|---|---|
| <Ref-N> | <SUBA-FR27> | <SUBB-FR46> | <SUBC-FR6> | <SUBD-FR27> |

---

## 🪦 Graveyard (killed — not reopened)
| What | Why it died | Decision |
|---|---|---|
| <killed thing> | <one-line reason> | <D-NN> |

### Deferred (valid, undated — icebox)
<item> · <item>.

---

## Backlog (unassigned)
> <Dated intake note (`<YYYY-MM-DD>`): capture · verdict · routing — additive, never rewritten.>

_(empty — every new idea enters here before triage)_
