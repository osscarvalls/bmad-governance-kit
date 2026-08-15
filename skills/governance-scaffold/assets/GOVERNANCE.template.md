# <Project> — Governance

> **Loaded every session. The single source of this project's governance rules.** If a helper script, a
> derived doc, or a skill contradicts this file, **this file wins.** Language of this document: <language>.

<!--
  This is the constitution the governance layer installs. Fill every <placeholder> from the project's
  actual plan. Keep it tight — it is read every session. State rules; don't argue them.
-->

## 0 · What this governs

This project is governed by **four co-equal pillars** plus supporting stores. Durable knowledge lives in
exactly one of them; nothing is written twice. The pillars are stitched into a navigable graph by one join
key, the `Ref`.

## 1 · The four pillars (one truth, one place)

| Pillar | Path | Owns |
|---|---|---|
| **ROADMAP** | `<path/to/ROADMAP.md>` | **WHAT + WHEN** — the feature registry (`Ref`), milestones, the Coverage Matrix, the Backlog, the Graveyard. |
| **PRD(s)** | `<path/to/prds/>` | **HOW — testable** — FRs namespaced per subsystem (`<SUB>-FRn`), each serving a `Ref`; NFRs in their own section. |
| **DECISIONS** | `<path/to/DECISIONS.md>` | **WHY-NOT** — an append-only log of closed decisions (`D-NN`). |
| **architecture** | `<path/to/architecture.md>` | **HOW — structural** — the spine, per-subsystem structure, milestone deltas; every decision tagged `[milestone · anchored\|movable · serves <Ref>]`. |

**The join key.** A feature (`Ref` in ROADMAP) ⇄ its FRs (one per subsystem, in the PRDs) ⇄ the structural
*how* (architecture) ⇄ the *why-not* (`D-NN` in DECISIONS). `grep` a `Ref` across the PRDs → every layer it
touches. Mnemonic: **ROADMAP = WHEN · PRD = HOW-testable · architecture = HOW-structural · DECISIONS =
WHY-NOT.**

## 2 · The subsystems (the possible layers)

Each subsystem owns exactly one question; its FRs are namespaced with its prefix.

| Subsystem | The one question it owns | FR namespace |
|---|---|---|
| **<SubA>** | <the one question> | `<SUBA>-FR` |
| **<SubB>** | <the one question> | `<SUBB>-FR` |
| **<SubC>** | <the one question> | `<SUBC>-FR` |
| **<SubD>** | <the one question> | `<SUBD>-FR` |

> Editions/tiers/phases are **packagings** of these subsystems (milestones), **not** separate codebases or
> folders. One platform that deepens.

## 3 · The five anti-drift laws (they are law)

1. **If it isn't in the registry (ROADMAP), it doesn't exist.** A "loose" feature is a contradiction in terms.
2. **One truth, one place.** ROADMAP=WHEN · PRD=HOW-testable · architecture=HOW-structural · DECISIONS=WHY-NOT.
   Never write the same fact in two of them. (Propagating a *consequence* joined by a shared `Ref`/`D-NN` is
   not duplication; copying the same text is.)
3. **A new idea enters as `state=idea`, `milestone=Backlog`** — then triage (which subsystem? passes the
   small-team filter? clashes with a live `D-NN`? anchored or movable?) → assign a milestone **or kill it
   with a reason**.
4. **What is killed is never deleted or reopened** — it lives in the Graveyard with its reason + the `D-NN`
   that closed it.
5. **The epics list is PROJECTED from a milestone** and regenerable — never a source of truth.

## 4 · Invariant patterns

- **`schema ON / enforcement OFF`** — design a later milestone's schema while building an earlier one; it's
  the same platform at two moments.
- **`anchored` vs `movable`** — *anchored* = backbone/irretrofittable (moving it costs a retrofit → a
  conscious decision); *movable* = reschedulable. architecture.md is the home of the tag.
- **One FR per layer.** A feature touching N subsystems → N FRs, all with the same `Ref`. An NFR
  (latency/residency/security/observability) → the PRD's NFR section, never an FR.
- **Provisional slugs** (`ARCH-*`/`INT-*`/`OPS-*`/`UX-*`/`LEG-*`) are placeholders until the owning
  subsystem's PRD gives them a real FR.

## 5 · Editing conventions

- **DECISIONS.md is append-only.** The only permitted edits to a closed entry are additive forward-pointers:
  `· SUPERSEDED-BY D-NN` (replaced → the old one flips to `[SUPERSEDED]`) or `· reframed|narrowed|refined by
  D-NN` (stays IN-FORCE; only its scope changes). A change of substance = a new entry; a reframe = the old
  one stays alive + its pointer.
- **Record ≠ decide.** A decision is logged only via `decision-record`, and only when someone can name what
  closed it (an explicit human close, an intake "advance" verdict, or a dated session). Never invent a `D-NN`.
- **History/evidence is never edited** — append/archive only.
- **Absolute dates** (`YYYY-MM-DD`), never relative.
- **Affirmative · timeless · additive** durable knowledge — states what *is*, not what isn't; when state
  changes, add or supersede.
- **Reference, don't restate** — cite the `Ref`/`FR`/`D-NN`.
- **Graveyard = reason + `D-NN` only** — the killed is not re-argued.
- **FR namespacing per subsystem** — never a global `FR-1..N` sequence.
- **Naming discipline** — implementation names never leak into product-surface docs; brand/domain terms are
  named exactly, not paraphrased away.

## 6 · Communication conventions

- **Talk to humans in names, not codes.** Codes are join keys *between documents*, not the language for
  people. Name things in plain language; put a code in parentheses *after* the name if it adds traceability.
- **Tight, decision-first reports.** No walls of text.
- **Professional register** in any client-/stakeholder-facing deliverable.

## 7 · Process → command (the operating loop)

Every recurring action goes through a command; nothing is improvised. Extending this catalog is a conscious,
registered act — compose existing commands into a new skill, or add a new one; never a silent exception.

| Process | Command |
|---|---|
| Land a raw idea/opportunity/vendor (diagnose → verdict) | `decision-intake` |
| Specify a whole product line / milestone (from zero, or reconcile a scattered spec) | `product-spec` |
| Register a shaped feature (Backlog → triage → FRs) | `feature-intake` |
| Record a closed decision (+ propagate) | `decision-record` |
| Scout / adopt a technology | `tech-scout` |
| Audit coherence (read-only gate) | `governance-check` |
| Project a milestone's epics (regenerable) | `epics-projection` |
| Design a milestone's test strategy + gates | `test-strategy` |
| Fix a bug / non-feature change | `fix` |
| Build a story / an epic | BMAD story/epic pipelines |

## 8 · Supporting stores (see the artifact taxonomy)

- **`history/`** — archived evidence (minutes, audits, superseded docs). Append/archive only, never edited.
- **`implementation/`** — pipeline memory: projected epics (regenerable), story files (the
  `Ref→story→commit` trace, archived on milestone close), the status projection (updated by whoever merges).
- **`deliverables/`** — client-facing, derived from planning.
- **`intake/`** *(optional)* — the pre-governance workshop; nothing here is governance.
- **`HUMAN-TODO.md` / `AGENT-TODO.md`** — the twin work indices (human-only vs agent-actionable).

## 9 · Pointers

- The four pillars: see §1.
- The plan this layer was scaffolded from: `<path/to/bmad/plan>`.
- The governance model, controlled vocabularies, and skill contract: the `bmad-governance-kit` plugin.
