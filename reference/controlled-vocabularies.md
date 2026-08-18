# Controlled vocabularies

The controlled vocabularies the governance layer uses. They are small on purpose — a closed set is what
makes the graph machine-checkable. Genericize the placeholders (`<Milestone>`, `<SUB>`, `<Ref>`,
`<D-NN>`) to your project.

## 1 · Calendar entry status (`status` in `release-calendar.yaml`)

The machine vocabulary — a closed set enforced by `calendar-ops.py`:

| Status | Meaning |
|---|---|
| `backlog` | Registered, not yet started. |
| `in-progress` | Being built now. |
| `done` | Shipped. |
| `unscheduled` | Registered but not assigned to an active release. |
| `blocked` | A phase-blocker / spike is open against it. |
| `killed` | In the Graveyard (derived view); carries `decisions[]` with its `D-NN`; not reopened. |

**Milestone-level qualifiers are narrative, not per-entry status.** "Hypothesis" (a milestone that only
builds if later data validates it), "frozen" (listed so it isn't lost; zero active hours), and the
`schema-ON / enforcement-OFF` case are stated in the **narrative `ROADMAP.md`** and carried by the
**architecture tag**, not encoded as a calendar `status`.

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
pillars the consequence propagates to — and the calendar mutation is always a `calendar-ops.py` operation:

| Verb | Effect | Propagates to |
|---|---|---|
| `CREATES <x>` | a new feature/capability | calendar `add` + PRD FR(s) (+ architecture if spine) |
| `CONSTRAINS <x>` | narrows an existing feature | PRD FR / architecture |
| `KILLS <x>` | removes a feature | calendar `set-status killed` + `add-decision` (Graveyard is derived) |
| `MOVES <x>` | reschedules across milestones | calendar `set-milestone` |
| `PROMOTES <x>` | commits a hypothesis / advances state | calendar `set-status` + narrative ROADMAP |
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
  - `serves <Ref>` — the feature handle (calendar entry key) it serves.
  - `serves <Ref>/<Ref2>` — multiple.
  - `serves <Ref> → <SUB>-FRn` — a handle resolved to its FR.
  - `serves <Ref> (via intake)` — a hypothesis capability with no FR yet.
  - `serves <Ref> schema` — the schema-ON/enforcement-OFF case.
- **`<D-NN>`** — provenance; may chain qualifiers: `· D-NN (refines D-NN)`, `· D-NN (constrains D-NN)`.

**The `serves <Ref>` clause is the FR-side declaration of the join** — `validate-release-calendar.py`
cross-checks it against the calendar, so it is not optional decoration.

## 5 · FR namespacing

Requirement numbering is **namespaced per subsystem** (`<SUB>-FRn`), never one global `FR-1..N` sequence.
`grep <SUB>-FR` returns exactly one subsystem's requirements. NFRs are named `NFR-<CODE>` so the calendar and
tests can reference them. The subsystem prefixes are declared in `release-calendar.yaml`'s `config.subsystems`
(mapping each prefix to its PRD file), which is how the validator resolves them.

## 6 · The calendar entry shape (`release-calendar.yaml`)

```yaml
config:
  prd_dir: prds                       # PRD folder, relative to the calendar file
  subsystems: { <SUB>: prd-<sub>.md } # FR namespace → PRD file (drives the validator)
  milestones: [<Milestone-0>, ...]    # the closed milestone vocabulary
releases:
  <release>:
    status: <in-progress|backlog|...>
    features:                         # readable business capabilities
      <Ref>:                          # the entry key = the feature handle = the join key
        milestone: <Milestone>
        frs: [<SUB>-FRn, ...]         # the FRs this feature is built from (the join)
        nfrs: [NFR-<CODE>, ...]
        epics: [epic-...]             # written back by epics-projection
        stories: [<M>-n.m]            # written back by epics-projection; sprint-status owns their state
        status: <status>              # optional; defaults to the release's
        decisions: [D-NN]             # required once killed
    enablers:                         # technical work with no user-facing story (same shape)
      <enabler>: { ... }
```

- **`features` vs `enablers`** — a feature is a readable business capability; an enabler is technical work
  with no user-facing story. Same shape; both carry FRs.
- **Business granularity, not FRs** — one entry is a capability, not a requirement. The FRs live in `frs[]`.
- **No dates** — they are estimated from the stories, never stored.
- **`epics[]` / `stories[]`** — written back by `epics-projection`; the calendar *references* stories,
  `sprint-status.yaml` owns their list + state.
