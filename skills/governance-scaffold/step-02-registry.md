# Step 02 — Scaffold the ROADMAP registry (narrative + release-calendar.yaml)

**Objective:** write the first pillar — the **ROADMAP registry** — in its two halves: a **narrative
`{gov}/ROADMAP.md`** (what exists and in what order, in prose) and **`{gov}/release-calendar.yaml`**, the
single *structured* source of the join (each feature → its milestone, and later its FRs/NFRs/epics/stories).
This is where "if it is not in the registry, it does not exist" becomes true. The **join** (feature ⇄ FR)
is filled in step-03; here we lay the two files and register every feature with its milestone.

## RULES

- **First write of the skill.** Create `{gov}/ROADMAP.md` + `{gov}/release-calendar.yaml` (greenfield) or
  extend them (merge). Never clobber existing entries — fold them in.
- **No invented features.** Every feature traces to something the plan already contains (an epic, a PRD
  feature, an architecture capability). If the plan implies a feature but never names it, register it and
  mark it (a note in the narrative, `provenance: inferred`) so the user can confirm.
- **The yaml is written only via `calendar-ops.py`** — never hand-author or string-edit it. The narrative
  `ROADMAP.md` is prose, human-owned.
- Match the source docs' language for the narrative; the yaml keys/values stay in the kit's neutral vocab.

## 1 · Copy the calendar tooling into `{gov}`

Copy from this skill's `assets/scripts/` into `{gov}/` (next to where the yaml will live):
`calendar-ops.py` and `validate-release-calendar.py`. They are **project-agnostic** — they read everything
project-specific from the yaml's own `config:` block. Note the Python 3 + PyYAML requirement for the handoff.

## 2 · Extract the features

Walk the epics/stories and the PRD. Each **coherent user-facing capability** becomes one **feature**; purely
technical work with no user-facing story becomes an **enabler**. An epic usually maps to one feature
(sometimes a few); a lone story usually does not — group stories into the capability they serve. For each
capture:

- **`Ref`** — a stable, short, meaningful kebab-case handle (e.g. `billing`, `agenda-sync`, or `F-01` if the
  project prefers numbers). This becomes the **entry key** in the calendar and the join key — pick it to
  last. Never reuse a retired handle.
- **Feature (JTBD)** — one line for the narrative, framed as the job it does for the user (delegate framing
  to **`bmad-agent-pm`** if the plan's wording is implementation-flavoured).
- **Milestone** — from the phasing agreed in step-00 (or leave for the Backlog if not yet scheduled).
- **Kind** — feature vs enabler.

## 3 · Seed `release-calendar.yaml` (config by hand, entries via the script)

Start from the bundled `assets/templates/release-calendar.template.yaml`. Fill only the **`config:`** block by
hand (it is not entry data): `prd_dir`, the `subsystems:` map (each FR-namespace prefix → its PRD filename,
from step-01), and the `milestones:` list (the closed milestone vocabulary from step-00). Create at least one
`releases:` entry (e.g. the active release) with empty `features: {}` / `enablers: {}`.

Then register **every** feature/enabler with a **`calendar-ops.py` operation** — never by editing the yaml:

```
python3 {gov}/calendar-ops.py add features <ref> --milestone <M> --release <release>
python3 {gov}/calendar-ops.py add enablers  <ref> --milestone <M> --release <release>
```

Leave `frs[]`/`nfrs[]` empty for now (step-03 fills them). Anything the plan lists as "later / maybe / out of
scope" → leave it out of the calendar and note it in the narrative **Backlog** section. Anything the plan
explicitly rejected → register it and immediately `set-status <ref> killed` + `add-decision <ref> <D-NN>`
(step-04 assigns the real `D-NN`); the Graveyard is a **derived view**, never a hand table.

## 4 · Write the narrative `ROADMAP.md`

Use `assets/templates/ROADMAP.template.md`. Write, in prose: the subsystem table, the five anti-drift laws
(the template carries them), and one section per milestone **in order**, naming features by their `Ref`
handle and explaining the what/why/sequence. **No FR tables, no coverage matrix, no dates** — those are the
calendar's and the PRDs'. Add the Backlog (pre-triage ideas) and the derived-Graveyard note. In the
front-matter, state that this is the **narrative** half and the yaml is the **structured** half (written via
`calendar-ops.py` only) — the join has exactly one owner, so there is no "which of five files is the source"
ambiguity to declare.

## 5 · Validate the seed

Run `python3 {gov}/validate-release-calendar.py`. With no FRs yet it should report `0 errors` (features with
empty `frs[]` are fine until step-03; the validator only flags FRs that don't resolve). Fix any config/path
error now — step-03 depends on the PRD paths in `config.subsystems` being correct.

## CHECKPOINT — Confirm the registry

Show the user: the milestone sections of the narrative (Ref · JTBD · order), the calendar's feature/enabler
entries per milestone (`calendar-ops.py get`), the Backlog, anything marked `inferred` or seeded-killed, and
the validator's PASS. Ask them to confirm the `Ref` handles (they are permanent join keys) and the
milestone of anything ambiguous.

**Stop and wait** for confirmation before touching the PRDs.

## Next step

Read it fully and follow: `./step-03-prd-coverage.md`.
