# BMAD Governance Kit

A Claude Code plugin that turns a **BMAD-planned project** into a **governed** one — and keeps it that way.

BMAD is great at *planning* (brief → PRD → architecture → epics). But a plan drifts the moment many people
and many sessions start touching it: features go "loose", requirements lose their trace, decisions get
re-litigated, the architecture forgets its own backbone. This kit installs the missing layer — a small,
opinionated **governance topology** — and the commands that operate it without drift.

## The model: four co-equal pillars, one truth in one place

| Pillar | Owns | |
|---|---|---|
| `ROADMAP.md` | **WHAT + WHEN** | a feature **registry** (each feature a stable `Ref`), milestones, a **Coverage Matrix** (`Ref` ⇄ FR), a **Backlog** and a **Graveyard** |
| PRD(s) | **HOW — testable** | FRs **namespaced per subsystem** (`<SUB>-FRn`), each serving a `Ref`; NFRs in their own section |
| `DECISIONS.md` | **WHY-NOT** | an **append-only** log of closed decisions (`D-NN`) with forward supersede/reframe pointers |
| `architecture.md` | **HOW — structural** | an invariant **spine**, per-subsystem structure, milestone deltas; every decision tagged `[milestone · anchored\|movable · serves <Ref>]` |

The join key is the `Ref`: a feature ⇄ its FRs (one per subsystem) ⇄ the architecture ⇄ the decision. A
`GOVERNANCE.md` constitution states the anti-drift laws and is loaded every session.

## What's in the kit

**One scaffolder** — lays the substrate from an existing BMAD plan:

- **`governance-scaffold`** — reads the BMAD planning artifacts and projects them into the four pillars +
  the constitution. Idempotent (greenfield or merge). Adds no product scope — it organizes what planning
  already produced and surfaces its blind spots (orphan features, un-phased work, decisions never written
  down).

**Six operators** — keep the layer alive (nothing is done by hand; every recurring action has a command):

| Command | Does |
|---|---|
| `decision-intake` | Diagnose a raw idea/opportunity/vendor by phases with kill-gates → verdict routes onward |
| `feature-intake` | Register a shaped feature: Backlog → triage → kill-with-reason **or** one FR per layer + coverage |
| `decision-record` | Append a closed decision (`D-NN`), add supersede pointers, propagate the consequence — never duplicating |
| `tech-scout` | Evaluate a technology against the spine → adopt + record, or open a spike |
| `governance-check` | Read-only coherence audit (`Ref`⇄FR, no orphans, no duplication, append-only intact) → PASS/WARN/FAIL |
| `epics-projection` | Project a milestone's epics (regenerable) → hand off to the build loop |

Each operator reads `GOVERNANCE.md` to resolve the pillar paths, so the kit is **portable** — nothing is
hardcoded to any one project.

## Install

```
/plugin marketplace add osscarvalls/bmad-governance-kit
/plugin install bmad-governance-kit@bmad-governance-kit
```

Then, in a BMAD-planned project:

```
/bmad-governance-kit:governance-scaffold
```

Skills are namespaced by the plugin: invoke any command as `/bmad-governance-kit:<command>`.

## Relationship to BMAD

This kit contributes **topology + sequence + discipline** — which pillar a fact belongs to, the format, and
the anti-drift rules. It does **not** re-implement analysis or design: wherever a judgement call is needed it
**delegates to a BMAD command if one is available** (`bmad-agent-architect` for anchored/movable,
`bmad-prd` for FR wording, `bmad-check-implementation-readiness` for the coherence gate,
`bmad-create-epics-and-stories` for expansion, …) and **degrades gracefully** — doing the call itself, and
saying so — when BMAD is not installed.

So: the kit is **usable standalone**, but reaches full quality on a project that also has BMAD installed.
BMAD is the recommended companion, not a hard dependency.

## Layout

```
bmad-governance-kit/
├── .claude-plugin/
│   ├── plugin.json          # plugin manifest
│   └── marketplace.json     # this repo is its own marketplace
└── skills/
    ├── governance-scaffold/ # the scaffolder (multi-step)
    ├── feature-intake/
    ├── decision-intake/
    ├── decision-record/
    ├── tech-scout/
    ├── governance-check/
    └── epics-projection/
```

## License

MIT
