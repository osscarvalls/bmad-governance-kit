# Step 04 — Architecture spine + tags, and seed the DECISIONS log

**Objective:** write the last two pillars together, because they cross-reference: the **architecture doc**
(HOW-structural — a spine, per-subsystem structure, milestone deltas, every decision tagged
`anchored`/`movable` and `serves <Ref>`) and the **append-only DECISIONS log** (WHY-NOT), seeded from the
decisions the plan already made.

## RULES

- Writes `{gov}/architecture.md` and `{gov}/DECISIONS.md`.
- **Reference, don't restate.** architecture.md points at ROADMAP/DECISIONS/PRD; it never re-enunciates a
  feature or an FR. If you're copying an FR's text into architecture, stop — tag and reference it instead.
- **DECISIONS is append-only from birth.** Even the seed entries follow the rule: affirmative, timeless,
  additive, with forward supersede/reframe pointers only.

## 1 · Structure architecture.md

Use the bundled templates `assets/templates/architecture.template.md` and
`assets/templates/DECISIONS.template.md` (they carry the spine/§B/§C structure, the tag grammar, and the
append-only decision format). Build (or, in merge mode, restructure the existing architecture doc into) three
sections:

```markdown
# <Project> — architecture (HOW — structural)   ·   source_of_truth: ROADMAP

## §A · Spine (invariant)
<the backbone that doesn't move: the core data model, the request/trust boundaries, the deploy seam,
the fundamental module split. Each item tagged and pointing at the Refs/FRs it serves.>

## §B · Per subsystem
### <Subsystem>
<its internal structure and key structural decisions — each tagged, each referencing FRs, no FR text copied>

## §C · Milestone deltas
### <Milestone>
<what this milestone adds/changes structurally vs the previous one>
```

## 2 · Tag every structural decision

Every decision in architecture.md carries a tag:

`[<milestone> · anchored|movable · serves <Ref(s)>]`

- **anchored** = backbone / irretrofittable — moving it later costs a retrofit, so scheduling it is a
  conscious decision. Put anchored decisions in §A or clearly marked in §B.
- **movable** = reschedulable freely.
- Delegate the anchored/movable call and the spine-fit judgement to **`bmad-agent-architect`** when
  available; otherwise make the call yourself and note the reasoning in one line.

> This tag is what lets a later epics projection **order work anchored-first**, and what tells a future
> change whether it's touching the backbone or just rescheduling.

## 3 · Seed DECISIONS.md

Create the append-only log. Mine the brief, any ADRs, and the architecture rationale for decisions **already
made** (technology picks, scope cuts, trade-offs, things deliberately *not* done) and record each as an
entry:

```markdown
# <Project> — DECISIONS (WHY-NOT, append-only)

> Append-only. Two allowed edits, both additive forward-pointers that never rewrite an entry:
> (a) `· SUPERSEDED-BY D-NN` when a later decision replaces this one (this one becomes [SUPERSEDED]);
> (b) `· reframed by D-NN` when a later one narrows/reframes it without replacing it (this stays VIGENTE).
> A decision that changes on the merits = a NEW entry. Long rationale/evidence lives in `history/`.

## D-01 · <title>   ·   <YYYY-MM-DD>
**Decision:** <what was decided — affirmative, timeless>.
**Why-not:** <the alternative(s) rejected and why>.
**Serves / affects:** <Ref(s) / FR(s) / spine>.
```

- Number them `D-01`, `D-02`, … in the order the plan made them (use the plan's dates where known; absolute
  dates only).
- For each Graveyard row from step-02, ensure there is a `D-NN` that closed it, and fill the Graveyard's
  `Decision` column with that id.
- Where a decision has a structural consequence, make sure its architecture tag references its `D-NN`, and
  where it scoped a feature, fill the registry row's `Decision` column. This is **propagation**, not
  duplication — the same `D-NN` joins the three pillars.

> **Do not manufacture decisions from your own reasoning.** Only record what the plan actually decided (or
> what the user explicitly confirms now). A speculative `D-NN` corrupts an append-only log and can only be
> superseded, never deleted.

## CHECKPOINT — Confirm architecture + decisions

Show: the architecture section skeleton with its tagged decisions (highlight what you marked **anchored**),
and the seeded `DECISIONS.md` list (D-NN · title · why-not, one line each). Ask the user to confirm the
anchored/movable calls and that no seeded decision misstates what was actually decided.

**Stop and wait** for confirmation.

## Next step

Read it fully and follow: `./step-05-constitution.md`.
