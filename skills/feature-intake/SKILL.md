---
name: feature-intake
description: Register a new feature/idea in a governance layer deterministically — Backlog (idea state) → triage gate → either kill-with-reason (Graveyard) or assign a milestone + create ONE FR per layer in the PRDs (namespaced <SUB>-FRn, each serving the new Ref) + update the Coverage Matrix. It never invents scope beyond what's agreed and never writes decisions by hand (those go to decision-record). Use when the user says "add a feature", "put X on the roadmap", "register this capability", or proposes a new product capability that already has shape. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md to resolve pillar paths and the subsystem namespaces.
---

# feature-intake

**Goal:** take a shaped capability and land it in the registry correctly — either killed with a reason, or
registered with a stable `Ref` and one testable FR per layer it touches, with the Coverage Matrix kept
honest. This is the delta-incremental path; a whole new product line gets specified first (with BMAD
planning + `governance-scaffold`), not here.

## On activation

1. **Resolve the layer.** Read `{gov}/GOVERNANCE.md` for the pillar paths, the subsystem set + their FR
   namespaces (`<SUB>-FR`), and the anti-drift laws. No layer → tell the user to run `governance-scaffold`.
2. **Read ROADMAP.md** (registry, milestones, Coverage Matrix, Backlog, Graveyard) and skim the PRD(s) for
   the current FR numbering per namespace.
3. Talk to the user in their language; write docs in each doc's language.

## Procedure

### 1 · Land it in the Backlog (idea state)
Every new idea enters as a `state=idea` row in the **Backlog** first — even if it will obviously be
committed. Give it a candidate `Ref` (permanent join key — choose to last) and candidate subsystems.
Frame the job-to-be-done in one line (delegate to `bmad-agent-pm` if available).

### 2 · The triage gate
Answer, out loud, before committing anything:
- **Which subsystem(s)** does it touch? (→ how many FRs it will have.)
- **Does it fit the spine, anchored or movable?** (Consult `bmad-agent-architect` read-only.)
- **Does it clash with a live `D-NN`?** If it contradicts a VIGENTE decision, it can't be committed as-is —
  route the conflict to `decision-intake` / `decision-record`.
- **Does it pass the small-team test** — could a couple of engineers own it? If it's too big, split it into
  smaller Refs or send it back to `decision-intake`.

### 3a · Kill-with-reason
If triage rejects it → move the row to the **Graveyard** with a one-line reason + the `D-NN` that closed it
(if the kill is a real decision, get that `D-NN` via `decision-record`). Killed features are never
reopened. Stop.

### 3b · Commit
If triage passes:
1. **Assign the milestone** (move the row from Backlog into that milestone's registry table; set status).
2. **Create one FR per layer** — in each touched subsystem's PRD, add a testable `<SUB>-FRn` (next in that
   namespace) with `serves <Ref>` and acceptance criteria. Delegate FR wording to `bmad-prd` if available.
   An NFR (latency/security/residency/…) goes to the PRD's **NFR section**, not as an FR, not as a Ref.
3. **Update the Coverage Matrix** — add the `Ref`'s row with its FR id in each subsystem column (`·` where
   no layer). Verify: the new `Ref` has ≥1 FR, and every new FR serves this `Ref`.
4. **Architecture** — only if it touches the spine: leave its mark in architecture.md, tagged
   `[milestone · anchored|movable · serves <Ref>]` (delegate to `bmad-agent-architect`). If it doesn't
   touch the spine, don't manufacture an architecture entry.

## Report

Show the outcome: killed (with reason + `D-NN`) or committed (the `Ref`, its milestone, the FRs created per
layer, the Coverage Matrix row, and any architecture tag). Confirm no fact was duplicated across pillars and
no decision was written by hand here.
