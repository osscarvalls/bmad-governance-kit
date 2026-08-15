# The governance model (in one read)

A BMAD plan is excellent at *what to build*. But a plan drifts the moment many people and many sessions
touch it: features go "loose", requirements lose their trace, decisions get re-litigated, the architecture
forgets its own backbone. This kit installs the missing layer — a small, opinionated **governance topology**
— and the commands that keep it honest. It **governs and delegates the thinking to BMAD; it never forks it.**

## Four co-equal pillars — one truth, one place

| Pillar | Owns | Never |
|---|---|---|
| **ROADMAP** | **WHAT + WHEN** — a feature registry (each feature a stable `Ref`), milestones, the Coverage Matrix (`Ref`⇄FR), the Backlog, the Graveyard. | explains *how* or *why* |
| **PRD(s)** | **HOW — testable** — functional requirements, namespaced per subsystem (`<SUB>-FRn`), each serving a `Ref`; NFRs in their own section. | holds implementation (that's architecture) |
| **DECISIONS** | **WHY-NOT** — an append-only log of closed decisions (`D-NN`) with forward supersede/reframe pointers. | rewrites or deletes a closed entry |
| **architecture** | **HOW — structural** — the invariant spine, per-subsystem structure, milestone deltas; every decision tagged `[milestone · anchored\|movable · serves <Ref>]`. | restates the other pillars — it points |

**The join key is the `Ref`.** A feature (ROADMAP) ⇄ its requirements (one per subsystem, in the PRDs) ⇄
the structural *how* (architecture) ⇄ the *why-not* (a `D-NN` in DECISIONS). `grep` a `Ref` across the PRDs
and you reach every layer it touches. Mnemonic: **ROADMAP = WHEN · PRD = HOW-testable · architecture =
HOW-structural · DECISIONS = WHY-NOT.** If a change makes you write the *same fact* in two of the four, stop
— you are duplicating. (Propagating a *consequence* — a status change in ROADMAP, a new FR in a PRD, a spine
decision in architecture — is not duplication: those are distinct facts joined by the `Ref`/`D-NN`.)

## The five anti-drift laws (they are law)

1. **If it isn't in the registry, it doesn't exist.** A "loose" feature is a contradiction in terms.
2. **One truth, one place.** Never write the same fact into two pillars.
3. **A new idea enters as `state=idea`, `milestone=Backlog`** — then triage (which subsystem? passes the
   small-team filter? clashes with a live decision? anchored or movable?) → assign a milestone **or kill it
   with a reason**.
4. **What is killed is never deleted or reopened** — it lives in the Graveyard with its reason + the `D-NN`
   that closed it.
5. **The epics list is PROJECTED from a milestone** and regenerable — never a source of truth.

## Invariant patterns

- **`schema ON / enforcement OFF`** — you may design the *schema* of a later milestone while building an
  earlier one, because it's the same platform at two moments. Proof that phases are **milestones, not
  separate codebases**.
- **`anchored` vs `movable`** — *anchored* = backbone/irretrofittable (moving it costs a retrofit → a
  conscious decision); *movable* = reschedulable freely. architecture.md is the home of the tag.
- **One FR per layer.** A feature touching three subsystems → three FRs in three PRDs, all with the same
  `Ref`. An NFR (latency/residency/security/observability) → the PRD's NFR section, never an FR.
- **Provisional slugs** (`ARCH-*`/`INT-*`/`OPS-*`/`UX-*`/`LEG-*`) are placeholders until the owning
  subsystem's PRD gives them a real FR.
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
     feature-intake   (govern: Ref + one FR per layer + Coverage Matrix)
          │
          ▼
     governance-check   (read-only coherence gate)
          │
          ▼
     epics-projection   (project the milestone's stories — regenerable)
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
tag grammar, and the decision effect-verbs; see [`operating-contract.md`](operating-contract.md) for the
contract every skill in the kit obeys.
