# Controlled vocabularies

The three controlled vocabularies the governance layer uses. They are small on purpose — a closed set is
what makes the graph machine-checkable. Genericize the placeholders (`<Milestone>`, `<SUB>`, `<Ref>`,
`<D-NN>`) to your project.

## 1 · Feature / milestone status (ROADMAP `State` column)

| Status | Meaning |
|---|---|
| `idea` | In the Backlog, pre-triage. |
| `committed` | Scheduled and owned. |
| `committed (schema/scaffold — enforcement OFF)` | The schema is designed now (schema-ON) but enforced in a later milestone. |
| `blocked` | A phase-blocker / spike is open against it. |
| `hypothesis` | Not committed — an alternative path that only builds if later data validates it. |
| `frozen` | Listed so it isn't lost; zero active hours. |
| `deferred (gate)` | Valid but held behind a named gate (e.g. legal/compliance). |
| `killed` | In the Graveyard; not reopened. |

## 2 · Decision lifecycle (per `D-NN` in DECISIONS)

- `IN-FORCE` — the live state of a decision.
- `SUPERSEDED` — replaced by a later decision; carries `· SUPERSEDED-BY D-NN`. The old text is **never
  rewritten**; it only gains the pointer and flips state.
- Reframe qualifiers — the entry **stays IN-FORCE**, only its scope/reading changes:
  `· reframed by D-NN` · `· narrowed by D-NN` · `· refined by D-NN`.

**The only two permitted edits to a closed entry are these additive forward-pointers.** A change of
substance = a *new* entry (+ `SUPERSEDED-BY`). A reframe = the old entry stays alive + its pointer. Never let
a superseded/reframed entry read as current.

## 3 · Decision effect verbs (the `→ *effect*` clause of a `D-NN`)

Every decision states its effect on features with one controlled verb + object. The verb drives which
pillars the consequence propagates to:

| Verb | Effect | Propagates to |
|---|---|---|
| `CREATES <x>` | a new feature/capability | ROADMAP row + PRD FR(s) (+ architecture if spine) |
| `CONSTRAINS <x>` | narrows an existing feature | PRD FR / architecture |
| `KILLS <x>` | removes a feature | ROADMAP → Graveyard |
| `MOVES <x>` | reschedules across milestones | ROADMAP row(s) |
| `PROMOTES <x>` | commits a hypothesis / advances state | ROADMAP status |
| `REWORKS <x>` | reshapes an existing feature | PRD + architecture |
| `REFRAMES <x>` | changes reading without replacing | a reframe pointer on the older `D-NN` |
| `governance.<x>` | pure process, no feature effect | none (log only) |

## 4 · The architecture tag grammar

Every architecture decision — and, echoed, every PRD FR — carries a tag:

```
[ <milestone> · <anchored|movable> · <serves-clause> · <D-NN> ]
```

- **`<milestone>`** — `<Milestone-0>` | `<Milestone-1>` | `<Milestone-Hypothesis>` | `all` | a compound
  like `<Milestone-0> seam / <Milestone-1> first line`.
- **`anchored | movable`** — backbone/irretrofittable vs reschedulable. Split form when a decision is partly
  each: `anchored (pattern) / movable (mechanisms)`.
- **`<serves-clause>`** — one of:
  - `<SUB>-FRn` — bare FR it directly serves.
  - `serves <SUB>-FRn/<SUB>-FRm` — multiple.
  - `serves <Ref> → <SUB>-FRn` — a ROADMAP Ref resolved to its FR.
  - `serves <Ref> (via intake)` — a hypothesis capability with no FR yet.
  - `serves <Ref> schema` — the schema-ON/enforcement-OFF case.
- **`<D-NN>`** — provenance; may chain qualifiers: `· D-NN (refines D-NN)`, `· D-NN (constrains D-NN)`.

## 5 · FR namespacing

Requirement numbering is **namespaced per subsystem** (`<SUB>-FRn`), never one global `FR-1..N` sequence.
`grep <SUB>-FR` returns exactly one subsystem's requirements. NFRs are named `NFR-<CODE>` so the Coverage
Matrix and tests can reference them.

## 6 · Coverage Matrix cell vocabulary

- `<SUB>-FRn` (or a comma list) — the FR(s) that subsystem contributes for that `Ref`.
- `·` — that subsystem has no layer for this `Ref`.
- `*(reads)*` / `*(approval queue)*` / `*(render surface)*` / `*(intake)*` — the subsystem participates but
  has no own FR (its slice is covered inside another FR, is an NFR, or awaits intake).
