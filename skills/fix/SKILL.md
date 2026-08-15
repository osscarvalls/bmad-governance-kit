---
name: fix
description: Fix a bug or a small change that creates NO new capability (no new Ref/FR) via the short path — bmad-investigate (cause) → bmad-quick-dev (fix + a test that pins the bug) → bmad-code-review (cold, fresh sub-agent) — with governance discipline: scoped writes (code/tests only, never planning artifacts), no green-by-skip, and a deploy-safe close. Use when the user says "fix this bug", "fix <x>", reports a defect/regression, or asks for a small non-feature change to existing code. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md + the project's test standards.
---

# fix

**Goal:** fix a bug or small change that **creates no new capability** (no new `Ref`/`FR`) via the short
path — investigate → quick-dev → cold review — with scoped writes and no faked green. Obeys the kit's
operating contract (`reference/operating-contract.md`).

## Entry gate (before touching anything)

1. **Is it really a fix?** If it **adds a capability** / needs a new `Ref`/`FR` → **STOP, route to
   `feature-intake`.** If it reveals a **spec or decision is wrong** (the source in the planning pillars) →
   **STOP, route to `decision-record` / `feature-intake`.** **This skill NEVER edits planning artifacts.**
2. **Load fundamentals:** `GOVERNANCE.md` (binding — especially the project's merge/deploy rules), the
   project's **test standards** (stack, targets, live lanes, no-green-by-skip), and the architecture spine
   invariants. If the fix touches a spine invariant, name it and treat the change as **sensitive**.

## The three steps (each names its command)

1. **Cause → `bmad-investigate`** on the symptom (an isolated sub-agent if large). Deliverable: the root
   cause with `file:line` evidence, the minimal fix scope, and *what test was missing that would have caught
   it*. If it doesn't converge on a cause, escalate with what was learned — don't patch blindly.
2. **Fix → `bmad-quick-dev`** (or `bmad-dev-story` if a formal story exists) with the exact finding. Hard
   rules: the fix arrives with a test that **first REPRODUCES the bug (red), then the fix turns it green**;
   **stay in scope** (no opportunistic refactors); run test + typecheck + lint + the live lanes the touched
   area requires — **real assertion counts, not green-by-skip.**
3. **Cold review → `bmad-code-review`** in a **fresh sub-agent with no context of how it was fixed**, over
   the diff. A BLOCKER → back to step 2 with the exact finding (≤2 loops; no convergence → escalate).

## Close (the project's deploy discipline)

One commit = one logical unit, on a `fix/<slug>` branch → PR → wait for green CI. **Dev-safe** (verified +
reversible, green CI + clean cold review) → merge to the main branch, verify the dev deploy is healthy,
notify the human. **Sensitive** (destructive migration · auth/security/secrets · the deploy pipeline itself ·
a major dependency bump · an anchored invariant the review didn't clarify) → PR left **open for the human,
never auto-merged.** Rollback = revert-forward (a new PR); the main branch always deployable. (Adjust these
exact rules to whatever the project's `GOVERNANCE.md` declares — it is binding.)

## Write scope (guardrail)

Code/tests only (+ the test-standards doc *only* if the fix concretizes a binding). **Never** touches
planning artifacts, stories, or the sprint tracker — *a fix is not a story; if it turns out to be one, you're
in the wrong skill.*
