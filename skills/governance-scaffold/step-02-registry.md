# Step 02 — Scaffold the ROADMAP registry (WHAT + WHEN)

**Objective:** write the first pillar — `{gov}/ROADMAP.md` — the single source of "what exists and when".
It holds the **feature registry** (every feature with a stable `Ref`), the **milestones**, an empty-but-
structured **Coverage Matrix**, and the **Backlog** and **Graveyard** sections. This is where "if it is not
in the registry, it does not exist" becomes true.

## RULES

- **First write of the skill.** Create `{gov}/ROADMAP.md` (greenfield) or extend the existing registry
  (merge). Never clobber existing rows — fold them in.
- **No invented features.** Every `Ref` traces to something the plan already contains (an epic, a PRD
  feature, an architecture capability). If the plan implies a feature but never names it, register it and
  mark it `provenance: inferred` so the user can confirm.
- Match the source docs' language.

## 1 · Extract the features

Walk the epics/stories and the PRD. Each **coherent user-facing capability** becomes one **feature row**.
An epic usually maps to one feature (sometimes a few); a lone story usually does not — group stories into
the capability they serve. For each feature capture:

- **`Ref`** — a stable, short, meaningful id (e.g. `AUTH`, `SEARCH`, `BILLING`, or `F-01` if the project
  prefers numbers). This is the join key — pick it to last. Never reuse a retired `Ref`.
- **Feature (JTBD)** — one line, framed as the job it does for the user (delegate framing to
  **`bmad-agent-pm`** if the plan's wording is implementation-flavoured).
- **Subsystem(s)** — which of the step-01 subsystems it touches (this predicts how many FRs it will have).
- **Milestone** — from the phasing agreed in step-00 (or `Backlog` if not yet scheduled).
- **Status** — see the status vocabulary below.
- **Decision** — the `D-NN` that scheduled/scoped it, if any (usually empty at scaffold time; filled as
  decisions get logged).

## 2 · Write ROADMAP.md

Start from the bundled template `assets/templates/ROADMAP.template.md` (it already carries the model
explainer, the five laws, the status vocabulary, and the Coverage-Matrix/Graveyard/Backlog structure) and
fill it from the features above. The section outline it produces:

```markdown
# <Project> — ROADMAP (registry: WHAT + WHEN)

> Single source of "what exists and when". Says neither HOW (→ PRDs / architecture) nor WHY-NOT (→ DECISIONS).
> A feature not in this registry does not exist. Killed features live in the Graveyard, never deleted.

## Status vocabulary
`idea` (Backlog, pre-triage) · `committed` · `committed (schema/scaffold — enforcement OFF)` · `blocked`
· `hypothesis` (not committed) · `frozen` · `killed`

## Milestones
<one subsection per milestone, in order; each with a one-line intent + status>

### <Milestone> · <intent>
| Ref | Feature (JTBD) | Subsystems | Status | Decision |
|-----|----------------|------------|--------|----------|
| ... | ...            | ...        | ...    | ...      |

## Coverage Matrix   <!-- Ref ⇄ FRs; filled/kept honest by step-03 -->
### <Milestone>
| Ref | <SUB1>-FR | <SUB2>-FR | ... |
|-----|-----------|-----------|-----|
| ... | ...       | ·         | ... |   <!-- "·" = this subsystem has no layer for this Ref -->

## Backlog   <!-- idea-state features, pre-triage: each is a `state=idea` row awaiting a milestone or a kill -->
| Ref | Idea | Candidate subsystems | Notes |
|-----|------|----------------------|-------|

## Graveyard   <!-- killed features: reason + the D-NN that closed them; never reopened -->
| Ref | Feature | Reason | Decision |
|-----|---------|--------|----------|
```

- Put each feature under its milestone table.
- Anything the plan lists as "later / maybe / out of scope for now" → **Backlog** (as `idea`), not a
  milestone table. Anything the plan explicitly rejected → **Graveyard** with its reason (and a seed `D-NN`
  placeholder that step-04 will assign a real number to).
- Leave the **Coverage Matrix** rows present (one per `Ref`) but with cells to be filled in step-03 — the
  matrix is the registry's half of the `Ref`⇄FR join; the PRD side is written next.

## 3 · Governance metadata

At the top of `ROADMAP.md`, declare the **coverage matrix as the source of truth** for the `Ref`⇄FR join
(the PRD tables are the regenerable projection). This one line prevents the classic divergence where the
same matrix is maintained in five files with no declared owner.

## CHECKPOINT — Confirm the registry

Show the user: the milestone tables (Ref · JTBD · subsystems · status), the Backlog, the Graveyard, and any
row marked `inferred`. Ask them to confirm the `Ref` ids (they are permanent join keys) and the
milestone/status of anything ambiguous.

**Stop and wait** for confirmation before touching the PRDs.

## Next step

Read it fully and follow: `./step-03-prd-coverage.md`.
