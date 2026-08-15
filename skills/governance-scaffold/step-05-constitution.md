# Step 05 — Write the GOVERNANCE constitution, the todo indices & the supporting stores

**Objective:** write the document that makes the four pillars **operable** — `{gov}/GOVERNANCE.md`, the
constitution that states the topology and the anti-drift laws — plus the twin work indices and the artifact
taxonomy. After this step the layer is not just scaffolded, it is **self-describing and operable**: anyone
(human or agent) opening the project reads GOVERNANCE.md and knows the rules, and the operating commands have
the stores they need.

## RULES

- Writes `{gov}/GOVERNANCE.md`, `{gov}/HUMAN-TODO.md`, `{gov}/AGENT-TODO.md`, and creates the supporting
  store folders + their READMEs.
- Everything is **tailored to this project's actual subsystems/milestones/paths** — not a generic copy. It
  must reflect what steps 00–04 produced.

## 1 · Write GOVERNANCE.md from the bundled template

Start from `assets/GOVERNANCE.template.md` (bundled with this skill) and fill every `<placeholder>` from what
steps 00–04 produced: the pillar paths (§1), the confirmed subsystem set + FR namespaces (§2), and the
process→command catalog (§7 — already lists the `bmad-governance-kit` commands). The template already carries
the five anti-drift laws, the invariant patterns, the editing/communication conventions, and the supporting-
store map — **do not re-derive them, just localize the placeholders.**

- Keep it **tight and scannable** — it is read every session. State rules, don't argue them.
- Under §5, name whatever **process rules** the project actually wants (who may change what, when a decision
  needs sign-off, the merge/deploy discipline). These are project-specific — **confirm them, don't invent
  them.**
- If the host project has an agent-instructions file (`CLAUDE.md`, `AGENTS.md`, `.cursorrules`, …), add a
  short pointer there to `{gov}/GOVERNANCE.md` so the constitution is actually loaded — **ask before editing
  that file**; don't assume ownership of it.

## 2 · Create the twin work indices

Copy `assets/templates/HUMAN-TODO.template.md` → `{gov}/HUMAN-TODO.md` and
`assets/templates/AGENT-TODO.template.md` → `{gov}/AGENT-TODO.md`, emptied of the example items. These are the
two mirror-image queues (human-only vs agent-actionable) the operating commands write to; their entry rules
live in the templates' preambles. If step-01–04 surfaced any human-only follow-ups (a payment, an OAuth
action, an owner sign-off, legal work) or agreed agent follow-ups, seed them now with the correct fields.

## 3 · Create the supporting stores (the artifact taxonomy)

Create these folders under `{gov}`, each with a one-line README (the taxonomy is described in
`reference/governance-model.md` §8 and the GOVERNANCE template §8):

- **`history/`** — archived evidence (minutes, audits, superseded docs). *Append/archive only, never edited.*
  If step-04 pulled long rationale out of the brief, drop it here.
- **`implementation/`** — pipeline memory: projected epics (`epics-<milestone>.md`, regenerable), story files
  (the `Ref→story→commit` trace, archived on milestone close), the status projection (updated by whoever
  merges). Leave it empty; `epics-projection` fills it.
- **`deliverables/`** — client-facing outputs, derived from planning; never a source. Create only if the
  project produces them.
- **`intake/`** *(optional)* — the pre-governance workshop (`RADAR.md`, a granular `GRAVEYARD.md`, one dossier
  per idea). Create only if the project will run `decision-intake`. *Nothing here is governance.*

## 4 · Note the epics-projection handoff

The scaffolded layer is the *input* to building. `epics.md` is **projected** from a milestone by
`epics-projection` (filter the milestone → expand each feature into its FRs/stories → order anchored-first
from the architecture tags) into `implementation/`. This skill does **not** project epics — it makes
projection possible.

## CHECKPOINT — Confirm the constitution

Show the user the GOVERNANCE.md draft (tight) and confirm the **process rules** under §5 match how they
actually want the project governed (those are project-specific — you should not invent them). Confirm the
supporting stores to create (deliverables/ and intake/ are optional) and whether to add the pointer to the
host agent-instructions file.

**Stop and wait** for confirmation.

## Next step

Read it fully and follow: `./step-06-verify-handoff.md`.
