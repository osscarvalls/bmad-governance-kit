---
name: decision-record
description: Record a CLOSED decision in the append-only DECISIONS log — assign the next D-NN, write the canonical entry (affirmative, timeless), add forward SUPERSEDED-BY / reframe pointers, dump long rationale/evidence to history/, and PROPAGATE the consequence to ROADMAP / PRD / architecture without duplicating. It is a SCRIBE, not a decider — it only writes when it can name what closed the decision (an explicit human close, a decision-intake "advance" verdict, or a dated session); otherwise it stops and routes to decision-intake. Use when the user says "record this decision", "we closed that…", "log this D-NN", "note this ADR", or reports a closed decision / change of course. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# decision-record

**Goal:** append **one** closed decision to the log and propagate its consequence across the other pillars —
never duplicating, never editing a closed entry. The only sanctioned way to touch the why-not log. Obeys the
kit's operating contract (`reference/operating-contract.md`).

## On activation

Read `GOVERNANCE.md` (pillar paths, subsystems, editing conventions) and the decision log itself (to find
the highest `D-NN` and the rules in force).

## STEP 0 — the authorization gate (a SCRIBE, not a decider)

Recording a decision **is not making it.** The log is append-only — a spurious `D-NN` can't be deleted, only
superseded, which corrupts it permanently. So before capturing anything, **name aloud** which of three
close-sources applies:

- (a) an **explicit human close**, or
- (b) an **"advance" verdict from `decision-intake`** (backed by a dossier), or
- (c) a **dated meeting/session**.

**If none → STOP. Don't assign an id. Route to `decision-intake`.** Never self-invoke from your own
reasoning. You may *propose* a close; the human (or the intake verdict) authorizes it.

## 1 · Draft the five canonical fields

- a short **title** (3–6 words) · the **decision in one line** (no long rationale) · **the effect on
  features via a controlled verb** — CREATES / CONSTRAINS / KILLS / MOVES / PROMOTES / REWORKS / REFRAMES (or
  `governance.` for a pure-process, no-feature-effect decision) · **source + absolute date** · **which
  `D-NN` it supersedes** (if any). Optional `bmad-advanced-elicitation` pass to red-team the draft *before*
  it becomes immutable.

## 2 · Assign the id

Re-read the log; the highest id is the **last entry of the file** (append-only) — never trust a number
remembered from another session. Decide placement by the originating session heading (append to an existing
group, or justify a new one).

## 3 · Evidence to history/ (only if long rationale exists)

`history/` is **never edited** — *create* a new file or *append* to an open in-progress session; never
rewrite a closed, signed record. Long rationale/alternatives/quotes go here; the one-line index goes in the
log; the consequence goes in the other pillars — **three distinct facts, no paragraph copied between them.**
Stitch the join: name the `D-NN` inside the evidence, point the log's `source` at the file. If the decision
"exhausts itself in one line", skip this step.

## 4 · Append the entry

Exact canonical format copied from neighbour entries (effect verb in italics, state `[IN-FORCE]`). **The
ONLY permitted edit to a closed entry** is adding `· SUPERSEDED-BY D-NN` (and flipping `[IN-FORCE]→
[SUPERSEDED]`) or a `· reframed|narrowed|refined by D-NN` pointer — **never rewrite text, never delete.** A
changed decision = a *new* entry, not an edit. Update the header `sources:` list only if a new evidence file
was born.

## 5 · Propagate the consequence as a QUAD, not a duplicate (the anti-drift core)

ROADMAP=WHAT+ORDER · calendar=the JOIN · PRD=HOW-testable · architecture=HOW-structural · DECISIONS=WHY-NOT.
Propagating the *consequence* to each is legitimate; **copying the same sentence into two is the drift this
skill exists to prevent.** The effect verb drives what to touch — and every calendar mutation is a
`calendar-ops.py` operation, never a hand edit:

- If it **CREATES a feature** → `calendar-ops.py add`. **MOVES** → `set-milestone`. **PROMOTES** →
  `set-status` (+ propose the narrative ROADMAP edit to the human). **KILLS** → `set-status <ref> killed` +
  `add-decision <ref> <this D-NN>` (the Graveyard is derived). Always `add-decision` to stamp the entry with
  this `D-NN`. Run `validate-release-calendar.py` after (must stay PASS).
- If it **reclassifies features across milestones/paths** → delegate the change-management reasoning to
  `bmad-correct-course` (the skill keeps the append-only entry, the kill discipline, and the routing).
- If it **changed a requirement** → the PRD FR is updated by `bmad-prd`.
- **Ask explicitly: does this touch the spine?** If yes, `bmad-agent-architect` **authors** the architecture
  entry in the right section with the right anchored/movable tag + this `D-NN` (the skill guarantees it
  *points*, doesn't restate). Omitting a needed spine footprint is a governance bug.

**CHECKPOINT before editing:** list, pillar by pillar, every file + row/FR/section, *what kind of fact* each
gets and *why it's distinct*, and the explicit spine answer. If the same sentence appears in two pillars,
rewrite until each has its own fact. Wait for OK.

## 6 · Verify & close

Re-read every touched zone: append-only intact, `history/` intact, no duplication, spine footprint
consistent with the answer above, references resolve both ways (grep the id/Ref), absolute dates, correct
per-doc language. Report file-by-file with clickable `path:line`; recommend a full `governance-check`.
