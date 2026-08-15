---
name: decision-record
description: Record a CLOSED decision in the append-only DECISIONS log of a governance layer — assign the next D-NN, write the canonical entry (affirmative, timeless, additive), add forward SUPERSEDED-BY / reframed-by pointers to whatever it replaces or reframes, dump long rationale/evidence to _history/, and PROPAGATE the consequence to ROADMAP / PRD / architecture without duplicating. It is a SCRIBE, not a decider — it only writes when it can name what closed the decision (an explicit human close, a decision-intake verdict of "advance", or a dated meeting/session); otherwise it stops and routes to decision-intake. Use when the user says "record this decision", "we closed that…", "log this D-NN", "note this ADR", or reports a closed decision / change of course. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md to resolve pillar paths.
---

# decision-record

**Goal:** append **one** closed decision to `DECISIONS.md` and propagate its consequence across the other
pillars — never duplicating, never editing a closed entry. This is the only sanctioned way to touch the
why-not log.

## On activation

1. **Resolve the layer.** Read `{gov}/GOVERNANCE.md` to get the four pillar paths (ROADMAP, PRD(s),
   DECISIONS, architecture), the subsystem set, and the editing conventions. If there is no governance
   layer, stop: tell the user to run `governance-scaffold` first.
2. **Read `DECISIONS.md`** to find the highest `D-NN` and the append-only rules in force.
3. Talk to the user in their language; write each doc in the language that doc already uses.

## The gate: are you allowed to write? (SCRIBE, not decider)

Recording a decision **is not the same as making it.** The log is append-only — a spurious `D-NN` cannot be
deleted, only superseded, which corrupts the log permanently. So write **only** if you can **name what
closed the decision**, and only one of three sources counts:

- (a) an **explicit human close** ("we closed that…", a sign-off), or
- (b) an **"advance" verdict from `decision-intake`**, or
- (c) a **dated meeting/session** whose notes close it.

If none of these exists, **do not invent a `D-NN`.** Stop and route to `decision-intake` — you may
*propose* that something be closed, but a human or an intake verdict authorizes the close.

## Procedure

1. **Assign `D-NN`** = highest existing + 1.
2. **Write the canonical entry** (append-only, at the end of the log):
   - **Title · absolute date** (`YYYY-MM-DD`).
   - **Decision** — what was decided, affirmative and timeless (states what *is*, not what "isn't yet").
   - **Why-not** — the alternative(s) rejected and why. This is the log's whole reason to exist.
   - **Serves / affects** — the `Ref(s)` / `FR(s)` / spine element it touches.
3. **Add forward pointers** to prior entries, if any (never rewrite them):
   - `· SUPERSEDED-BY D-NN` on any entry this one **replaces** (that entry becomes `[SUPERSEDED]`).
   - `· reframed by D-NN` on any entry this one **narrows/reframes** without replacing (it stays live).
4. **Dump evidence** — long rationale, meeting notes, quotes, superseded docs → `{gov}/_history/`
   (append/archive; never edited). `DECISIONS.md` references it, doesn't inline it.
5. **Propagate the consequence** (this is not duplication — the same `D-NN` joins the pillars):
   - If it **scheduled/scoped/killed a feature** → update the `Ref`'s row in ROADMAP (status, milestone,
     `Decision` column) or move it to the Graveyard with this `D-NN`.
   - If it **changed a requirement** → the PRD FR is updated (delegate wording to `bmad-prd` if available).
   - If it **has a structural consequence** → architecture.md gets/updates the decision, tagged
     `[milestone · anchored|movable · serves <Ref>]` with this `D-NN` (delegate to `bmad-agent-architect`
     if available). Use `bmad-correct-course` if the decision reclassifies features.
   - **Never copy the decision's text into three docs** — each pillar carries its own fact, joined by `D-NN`.

## Report

Show: the new `D-NN` entry, every forward pointer added, what went to `_history/`, and the propagation
(which ROADMAP row / FR / architecture tag changed). Confirm nothing was duplicated across pillars.
