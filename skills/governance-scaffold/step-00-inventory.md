# Step 00 — Inventory the BMAD plan & fix the scope

**Objective:** discover what planning already produced, decide where the governance layer will live, detect
whether any governance already exists (merge vs greenfield), and confirm the plan with the user before
writing anything.

## RULES

- This step **reads and agrees scope** — it writes nothing yet.
- Talk to the user in their language. Cite files as `path:line` so references are clickable.

## 1 · Detect the planning artifacts

Search `{project-root}` for BMAD planning output. It may sit under `docs/`, `_bmad-output/`, `output/`,
`planning/`, project root, or a configured path. Look for, and record the path of, each that exists:

- **Product brief** — `*brief*.md` (the problem, users, goals).
- **PRD(s)** — `*prd*.md` (functional requirements — usually `FR`/`NFR` numbered).
- **Architecture / solution design** — `*architecture*.md`, `*solution*.md`, `*tech-spec*.md`.
- **Epics & stories** — `*epic*.md`, `stories/`, `*sprint*status*`.
- **Any decisions/ADRs** already recorded — `*decision*.md`, `adr/`, `*ADR*`.

If a BMAD config exists (`_bmad/bmm/config.*`, `bmad.config.*`), read it to resolve the artifact
directory and the project/user names and languages; otherwise infer from what you found.

> If **no** BMAD planning artifacts are found, stop and tell the user: this skill scaffolds governance
> **from** a plan — it needs the plan first. Point them at BMAD planning (`bmad-product-brief` → `bmad-prd`
> → `bmad-create-architecture` → `bmad-create-epics-and-stories`) and offer to resume afterwards.

Set `{plan}` = the directory (or set) where these live.

## 2 · Detect existing governance (merge vs greenfield)

Check whether a governance layer (or fragments of one) already exists: a `ROADMAP.md`/registry, a
`release-calendar.yaml` (or any feature⇄FR join, even an old-style coverage matrix), a `DECISIONS.md`, an
architecture doc with `anchored`/`movable` tags, a `GOVERNANCE.md`/constitution. Decide the **mode**:

- **greenfield** — no governance yet. Scaffold all four pillars from the plan.
- **merge** — some governance exists. **Extend, never clobber.** Map what's present to the four pillars,
  find the gaps (a registry with no structured join; a hand-kept coverage matrix to migrate into
  `release-calendar.yaml`; a PRD with un-namespaced FRs; decisions kept as prose in the brief with no
  append-only log), and scaffold **only the missing structure**, folding existing content in.

## 3 · Decide where governance lives

Default `{gov}` = `{project-root}/governance/`. Confirm with the user, or accept a different target (some
teams keep it at repo root, or alongside the plan). Whatever they choose, all four pillars + `history/` +
`implementation/` live under `{gov}`.

## 4 · Read the plan for shape (not detail yet)

Skim — do not deep-read — the brief, PRD(s) and architecture to answer three shaping questions the later
steps depend on:

1. **Subsystems / layers.** Does the plan already decompose the product into subsystems (from the
   architecture's module boundaries, or PRD sections)? List the candidate subsystems — they become the
   **FR namespaces** (`<SUB>-FRn`) in step-01.
2. **Milestones / phasing.** Does planning imply phases (MVP → v1 → later; or epic groupings)? List the
   candidate milestones — the registry is organized by them in step-02.
3. **Existing decisions.** Are there decisions/trade-offs already written down (in the brief, ADRs, or
   architecture rationale) that should seed the append-only `DECISIONS.md` in step-04?

Note gaps: if the plan has no clear subsystem decomposition or no phasing, say so — step-01 will propose a
minimal one and confirm it, rather than invent silently.

## CHECKPOINT — Confirm the scope

Present a compact scope card:

- **Mode:** greenfield or merge (and, if merge, what already exists and what's missing).
- **Plan inventory:** each artifact found, with its path (`path:line` clickable), and anything expected but
  missing (e.g. "no architecture doc → the HOW-structural pillar will be thin, flag it").
- **`{gov}` target:** where the layer will be written.
- **Candidate subsystems** (→ FR namespaces), **candidate milestones**, and **decisions to seed** — each as
  a short list, marked where the plan is silent and you'll need to confirm.

**Stop and wait for the user.** Is the mode right, is `{gov}` right, do the subsystems/milestones match
their intent? Do not write anything until they confirm.

## Next step

Once scope is confirmed, read it fully and follow: `./step-01-subsystems.md`.
