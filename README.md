# BMAD Governance Kit

A Claude Code plugin that turns a **BMAD-planned project** into a **governed** one — and keeps it that way.

BMAD is great at *planning* (brief → PRD → architecture → epics). But a plan drifts the moment many people
and many sessions start touching it: features go "loose", requirements lose their trace, decisions get
re-litigated, the architecture forgets its own backbone. This kit installs the missing layer — a small,
opinionated **governance topology** — and the commands that operate it without drift. It **governs and
delegates the thinking to BMAD; it never forks it.**

## The model: four co-equal pillars, one truth in one place

| Pillar | Owns | |
|---|---|---|
| `ROADMAP.md` | **WHAT + WHEN** | a feature **registry** (each feature a stable `Ref`), milestones, a **Coverage Matrix** (`Ref` ⇄ FR), a **Backlog** and a **Graveyard** |
| PRD(s) | **HOW — testable** | FRs **namespaced per subsystem** (`<SUB>-FRn`), each serving a `Ref`; NFRs in their own section |
| `DECISIONS.md` | **WHY-NOT** | an **append-only** log of closed decisions (`D-NN`) with forward supersede/reframe pointers |
| `architecture.md` | **HOW — structural** | an invariant **spine**, per-subsystem structure, milestone deltas; every decision tagged `[milestone · anchored\|movable · serves <Ref>]` |

The join key is the `Ref`: a feature ⇄ its FRs (one per subsystem) ⇄ the architecture ⇄ the decision. A
`GOVERNANCE.md` constitution states the anti-drift laws and is loaded every session. Full model in
[`reference/governance-model.md`](reference/governance-model.md).

## The ten commands

**Scaffolder** — lays the substrate from an existing BMAD plan:

- **`governance-scaffold`** *(multi-step)* — reads the BMAD planning artifacts and projects them into the
  four pillars + the constitution + the twin todo indices + the artifact-taxonomy stores. Idempotent
  (greenfield or merge). Adds no product scope — it organizes what planning produced and surfaces its blind
  spots (orphan features, un-phased work, decisions never written down). Ships with faithful pillar templates
  under [`skills/governance-scaffold/assets/`](skills/governance-scaffold/assets/).

**Operators** — keep the layer alive (every recurring action is a command; nothing is improvised):

| Command | Does |
|---|---|
| `decision-intake` | Diagnose a raw idea/opportunity/vendor by phases with kill-gates → verdict routes onward |
| `product-spec` | Specify a whole product line: brief → journeys → deep PRDs → UX → architecture, with a carry-down contract + completeness gate |
| `feature-intake` | Register a shaped feature: Backlog → triage → kill-with-reason **or** one FR per layer + coverage |
| `decision-record` | Append a closed decision (`D-NN`), add supersede pointers, propagate — never duplicating |
| `tech-scout` | Evaluate a technology against the spine → adopt + record, or open a spike |
| `governance-check` | Read-only coherence audit → one PASS/WARN/FAIL report; never auto-fixes |
| `epics-projection` | Project a milestone's epics (regenerable) → hand off to the build loop |
| `test-strategy` | Design a milestone's test strategy + gates → write the test standards |
| `fix` | The short path for a bug / non-feature change (no new Ref/FR) |

Each operator reads the target project's `GOVERNANCE.md` to resolve the pillar paths, so the kit is
**portable** — nothing is hardcoded to any one project.

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

## What's in the box

```
bmad-governance-kit/
├── .claude-plugin/           # plugin.json + marketplace.json (repo is its own marketplace)
├── reference/                # the model, the controlled vocabularies, the operating contract
│   ├── governance-model.md
│   ├── controlled-vocabularies.md   # status vocab · tag grammar · effect verbs
│   └── operating-contract.md        # the contract every skill obeys
└── skills/
    ├── governance-scaffold/  # the scaffolder (7 steps) + assets/ (7 templates)
    ├── decision-intake/  product-spec/  feature-intake/  decision-record/
    ├── tech-scout/  governance-check/  epics-projection/  test-strategy/  fix/
```

## Relationship to BMAD

This kit contributes **topology + sequence + discipline** — which pillar a fact belongs to, the format, the
anti-drift rules. It does **not** re-implement analysis or design: wherever a judgement call is needed it
**delegates to a BMAD command if one is available** (`bmad-agent-architect` for anchored/movable, `bmad-prd`
for FR wording, `bmad-check-implementation-readiness` for the coherence gate, `bmad-create-epics-and-stories`
for expansion, the `bmad-testarch-*` suite for testing, …) and **degrades gracefully** — doing the call
itself, and saying so — when BMAD is not installed.

So: the kit is **usable standalone**, but reaches full quality on a project that also has BMAD installed.
BMAD is the recommended companion, not a hard dependency.

## License

MIT
