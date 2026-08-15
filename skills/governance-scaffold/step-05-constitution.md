# Step 05 — Write the GOVERNANCE constitution & supporting stores

**Objective:** write the document that makes the four pillars **operable** — `{gov}/GOVERNANCE.md`, the
constitution that states the topology and the anti-drift laws for this project — and create the two
supporting stores (`_history/`, `_epics/`). After this step the layer is not just scaffolded, it is
**self-describing**: anyone (human or agent) opening the project can read GOVERNANCE.md and know the rules.

## RULES

- Writes `{gov}/GOVERNANCE.md` and creates `{gov}/_history/` and `{gov}/_epics/`.
- GOVERNANCE.md is **the rules**, tailored to this project's actual subsystems/milestones/paths — not a
  generic copy. It must reflect what steps 00–04 actually produced.

## 1 · Write GOVERNANCE.md

Author the constitution with these sections, filled with this project's specifics:

```markdown
# <Project> — Governance

> Loaded every session. The single source of the project's governance rules. If a helper script or a
> derived doc contradicts this file, THIS file wins.

## The four pillars (one truth, one place)
<the table: ROADMAP=WHAT+WHEN · PRD(s)=HOW-testable · DECISIONS=WHY-NOT · architecture=HOW-structural,
with this project's actual file paths under {gov}>

## The subsystems
<the confirmed subsystem set from step-01: name · the one question it owns · FR namespace>

## The anti-drift laws
1. If it is not in the registry (ROADMAP), it does not exist.
2. ROADMAP=WHEN · PRD=HOW-testable · architecture=HOW-structural · DECISIONS=WHY-NOT — never write the
   same fact in two of them.
3. New idea → a `state=idea` row in the Backlog → triage → assign a milestone or kill with a reason.
4. Killed things are not deleted or reopened → Graveyard with reason + the D-NN that closed them.
5. epics.md is PROJECTED from a milestone; regenerable, never a source of truth.

## Editing conventions
- DECISIONS.md is append-only; the only edits are additive forward-pointers (SUPERSEDED-BY / reframed by).
- `_history/` is archived evidence — never edited.
- Absolute dates; affirmative/timeless/additive durable knowledge; reference don't restate.
- One FR per layer; NFRs go to the PRD NFR section; anchored/movable tags live in architecture.md.
- <governance writes> may edit the four pillars; product code and the plan are separate — name here whatever
  process rules the project wants (who may change what, when a decision needs sign-off, etc.).

## The join key
A feature (Ref in ROADMAP) ⇄ its FRs (one per subsystem, in the PRDs) ⇄ the HOW (architecture) ⇄ the
WHY-NOT (D-NN in DECISIONS). `grep` a Ref across the PRDs to find every layer it touches.

## Process → command (the operating loop)
Every recurring governance action goes through a command; nothing is done by hand.
| Process | Command |
|---|---|
| Land a raw idea/opportunity/vendor (diagnose → verdict) | `decision-intake` |
| Register a shaped feature (Backlog → triage → FRs) | `feature-intake` |
| Record a closed decision (+ propagate) | `decision-record` |
| Scout/adopt a technology | `tech-scout` |
| Audit coherence (read-only gate) | `governance-check` |
| Project a milestone's epics (regenerable) | `epics-projection` |

## Pointers
<paths to ROADMAP.md, prd/, DECISIONS.md, architecture.md, _history/, _epics/, and the BMAD plan it was
scaffolded from>
```

- Keep it **tight and scannable** — it is read every session. State rules, don't argue them.
- If the host project has an agent-instructions file (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, etc.), add a
  short pointer there to `{gov}/GOVERNANCE.md` so the constitution is actually loaded — **ask before editing
  that file**; don't assume ownership of it.

## 2 · Create the supporting stores

- `{gov}/_history/` — with a one-line `README` stating it holds archived evidence (superseded docs, notes,
  audits), append/archive only, never edited. If step-04 pulled long rationale out of the brief, drop it
  here.
- `{gov}/_epics/` — with a one-line `README` stating it holds epics **projected** from a milestone
  (regenerable; not a source of truth). Leave it empty; projecting epics is the next tool's job, not this
  skill's.

## 3 · Note the epics-projection handoff

The scaffolded layer is the *input* to building. epics.md is **projected** from a milestone by
`epics-projection` (filter the milestone → expand each feature into its FRs/stories → order
anchored-first from the architecture tags). This skill does **not** project epics — it makes projection
possible. Record in GOVERNANCE.md's pointers that `_epics/` is filled by `epics-projection`.

## CHECKPOINT — Confirm the constitution

Show the user the GOVERNANCE.md draft (tight) and confirm the process rules under "Editing conventions"
match how they actually want the project governed (those are project-specific and you should not invent
them). Confirm whether to add the pointer to the host agent-instructions file.

**Stop and wait** for confirmation.

## Next step

Read it fully and follow: `./step-06-verify-handoff.md`.
