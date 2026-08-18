# The governance model (in one read)

A BMAD plan is excellent at *what to build*. But a plan drifts the moment many people and many sessions
touch it: features go "loose", requirements lose their trace, decisions get re-litigated, the architecture
forgets its own backbone. This kit installs the missing layer — a small, opinionated **governance topology**
— and the commands that keep it honest. It **governs and delegates the thinking to BMAD; it never forks it.**

## Four co-equal pillars — one truth, one place

| Pillar | Owns | Never |
|---|---|---|
| **ROADMAP** | **WHAT + ORDER + the join.** Two artifacts: a **narrative `ROADMAP.md`** (milestones → features in prose: the what/why and the sequence; no dates, no FR tables) and **`release-calendar.yaml`** — the single *structured* source of the join (release → feature/enabler + milestone → FRs/NFRs → epics → stories, with status + `decisions[]` per entry). | explains *how* or *why-not*; stores dates (they are estimated from the stories) |
| **PRD(s)** | **HOW — testable** — functional requirements, namespaced per subsystem (`<SUB>-FRn`), each declaring the feature it `serves`; NFRs in their own section. | holds implementation (that's architecture); keeps its own coverage table |
| **DECISIONS** | **WHY-NOT** — an append-only log of closed decisions (`D-NN`) with forward supersede/reframe pointers. | rewrites or deletes a closed entry |
| **architecture** | **HOW — structural** — the invariant spine, per-subsystem structure, milestone deltas; every decision tagged `[milestone · anchored\|movable · serves <Ref>]`. | restates the other pillars — it points |

**The join key is the `Ref`** — the feature handle: its kebab-case business name, which is *also* its entry
key in `release-calendar.yaml`. A feature (a calendar entry, named in the narrative ROADMAP) ⇄ its
requirements (one FR per subsystem, in the PRDs, each `serves <Ref>`) ⇄ the structural *how* (architecture) ⇄
the *why-not* (a `D-NN` in DECISIONS). The join lives in **exactly one place** — `release-calendar.yaml` —
and the PRD's `serves <Ref>` is the FR-side declaration that a **schema validator** cross-checks. Mnemonic:
**ROADMAP = WHAT+ORDER · calendar = the JOIN · PRD = HOW-testable · architecture = HOW-structural · DECISIONS
= WHY-NOT.** If a change makes you write the *same fact* in two pillars, stop — you are duplicating.
(Propagating a *consequence* — a status in the calendar, a new FR in a PRD, a spine decision in architecture
— is not duplication: those are distinct facts joined by the `Ref` / `D-NN`.)

## Why a YAML and not a Markdown table (the determinism win)

The old model kept the `feature ⇄ FR` join as a **Coverage Matrix table**, replicated across the ROADMAP and
every PRD, maintained by hand via fragile string-match, with no declared owner. This model removes that
whole failure class:

- The join lives **only** in `release-calendar.yaml`. The Coverage Matrix disappears from the ROADMAP and
  the PRDs.
- The calendar is **written only through `calendar-ops.py`** (a structured operation), never by editing the
  yaml by hand or by string-match.
- The join is **validated by schema** with `validate-release-calendar.py`: every FR in the calendar exists
  in its PRD, every `(Ref, FR)` pair is confirmed by the PRD's `serves`, and every PRD `serves <Ref>` resolves
  to a real calendar entry. One source, one validation — not two hand-kept tables.
- The **narrative `ROADMAP.md`** carries order and rationale for humans; **no skill mutates it** (a human
  edits it, or the agent with the human's OK). Machines read the yaml; humans read the prose.

## The five anti-drift laws (they are law)

1. **If it isn't in the registry, it doesn't exist.** A "loose" feature is a contradiction in terms. The
   registry = the narrative `ROADMAP.md` (order/why) + `release-calendar.yaml` (the join).
2. **One truth, one place.** ROADMAP=WHAT+ORDER · calendar=the JOIN · PRD=HOW-testable ·
   architecture=HOW-structural · DECISIONS=WHY-NOT. Never write the same fact into two pillars.
   feature→milestone lives **only** in the calendar.
3. **A new idea enters the Backlog** — then triage (which subsystem? passes the small-team filter? clashes
   with a live decision? anchored or movable?) → register it in the calendar with a milestone **or kill it
   with a reason**.
4. **What is killed is never deleted or reopened.** The **Graveyard is a derived view**: the `D-NN` that
   kills it in DECISIONS + the entry set to `status: killed` (with `decisions[]`) in the calendar.
5. **The epics list is PROJECTED from a milestone** and regenerable — never a source of truth. The
   projection writes `epics[]`/`stories[]` back into the calendar.

## Invariant patterns

- **`schema ON / enforcement OFF`** — you may design the *schema* of a later milestone while building an
  earlier one, because it's the same platform at two moments. Proof that phases are **milestones, not
  separate codebases**.
- **`anchored` vs `movable`** — *anchored* = backbone/irretrofittable (moving it costs a retrofit → a
  conscious decision); *movable* = reschedulable freely. architecture.md is the home of the tag.
- **One FR per layer.** A feature touching three subsystems → three FRs in three PRDs, all serving the same
  `Ref`. An NFR (latency/residency/security/observability) → the PRD's NFR section, never an FR.
- **Readable handles.** A feature's `Ref` is its **kebab-case business name** — the calendar entry key
  (`billing`, `agenda-sync`). Legacy short slugs (`ARCH-*`/`INT-*`/`LEG-*`) stay valid `Ref`s in the `serves`
  clauses that already use them.
- **Milestones, not folders.** Editions/tiers/phases are *packagings* of the same subsystems — one platform
  that deepens.

## The delegation principle (BMAD is the brain; the kit is the discipline)

The governance skills are, in essence, **BMAD commands run in series with a shared context plus governance
discipline.** They do not reimplement analysis, design, or validation. **Rule of thumb: could a BMAD command
do this step? Then it does.** The skill adds only what BMAD lacks: the **topology** (which pillar a fact
belongs to), the **format**, the **sequence**, and the **discipline** (append-only, coverage,
no-duplication, anchored/movable). Every skill names, step by step, the exact command it delegates to — a
step without its command cited is a bug in the skill. When BMAD is not installed, the skills **degrade
gracefully** (they do the call themselves and say so), so the kit is usable standalone but reaches full
quality with BMAD present.

## The operating loop

```
                    decision-intake     (diagnose a raw idea → verdict)
                          │
     product-spec  ◄──────┼──────►  tech-scout        (from-zero product line / new technology)
          │               │
          ▼               ▼
     feature-intake   (govern: calendar entry + one FR per layer, join validated by schema)
          │
          ▼
     governance-check   (read-only coherence gate; runs validate-release-calendar.py)
          │
          ▼
     epics-projection   (project the milestone's stories; write epics[]/stories[] back to the calendar)
          │
          ▼
     test-strategy   (ONCE per milestone: suite + gates → test standards)
          │
          ▼
     build (BMAD story/epic pipelines)  ──►  fix   (bug / non-feature change)
```

**The only order that matters: check → (fix) → project → build.** Never project or build on an unverified
roadmap. Architecture is present throughout: intake **consults** it (does it fit the spine?), tech-scout
**updates** it, epics-projection **uses it to order** (anchored first). A spine change with no footprint in
architecture is a governance bug.

## The autonomy dial

- **Gated & conversational** (`decision-intake`, `decision-record`, `tech-scout`) — they ask, you decide; a
  BMAD persona provides the judgement. `feature-intake` **cannot touch the spine** — if a feature needs a
  spine change it stops and routes to `decision-record`.
- **Run-and-report** (`governance-check`, `epics-projection`) — they transform or audit, they don't ask. The
  check **detects but never fixes** — it hands you the fix and the skill that owns it. Projection is
  deterministic, not creative — change the roadmap, re-project.
- **Execution** (build pipelines, `fix`) — the sharp end. `fix` never edits planning artifacts; if a "fix"
  turns out to be new capability or a wrong spec, it stops and routes back through governance.

See [`controlled-vocabularies.md`](controlled-vocabularies.md) for the status vocabulary, the architecture
tag grammar, the calendar entry shape, and the decision effect-verbs; see
[`operating-contract.md`](operating-contract.md) for the contract every skill in the kit obeys.
