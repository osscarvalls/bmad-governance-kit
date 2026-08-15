---
name: test-strategy
description: Design HOW a milestone is tested and stand up its test infra — the milestone-altitude layer above the per-story pipelines. A thin wrapper over the BMAD test-architect suite (bmad-tea + bmad-testarch-test-design/nfr/framework/ci) plus the project-specific quality delta the test-architect doesn't know (the test layers, per-plane harness, root correctness gate, deploy-blocking performance gate, pinned stack, and traceability test→AC→FR→Ref), derived from the architecture cross-cutting section + closed decisions. It OWNS the test-standards doc — filling its [TBD]s so the per-story pipelines read and execute them. It re-implements no testing logic and invokes no execution pipelines. Use when the user says "design the test strategy for <milestone>", "stand up the test infra", "define the test gates", or is about to stand up testing before building a milestone's stories. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# test-strategy

**Goal:** design **how a milestone is tested** and **stand up its test infra** — the milestone-altitude layer
*above* the per-story pipelines. A **thin wrapper** over the BMAD test-architect suite plus the
project-specific quality delta the test-architect doesn't know. It **owns the test-standards doc** — filling
its `[TBD]`s so the per-story pipelines can read and execute them. It re-implements no testing logic and
invokes no execution pipelines. Obeys the kit's operating contract (`reference/operating-contract.md`).

## Bi-phasic (detect the phase)

- **Pre-code** (no app/package yet): test-design + NFR run in full; framework + CI produce the **spec, not
  real scaffolding**; the test-standards doc is filled where resolvable.
- **With-skeleton** (a walking skeleton exists): framework + CI are **applied for real**.

Detect via "does a package manifest / app dir exist?" and propose the phase.

## Step sequence

| Step | Phase | Delegates to | Gate |
|---|---|---|---|
| 01 | Load + scope + activate the test-architect | `bmad-tea` (persona) | CHECKPOINT |
| 02 | Risk-based milestone test plan | `bmad-testarch-test-design` | CHECKPOINT |
| 03 | NFR evidence plan | `bmad-testarch-nfr` | CHECKPOINT |
| 04 | Framework (pinned to the stack) | `bmad-testarch-framework` | CHECKPOINT |
| 05 | CI gates (with project gates embedded) | `bmad-testarch-ci` | CHECKPOINT |
| 06 | Consolidate to the test-standards doc + close | — (in-skill) + recommend `governance-check` | complete-when |

**Load-bearing nuances:**

- **01.** Pick the milestone + phase. Load **all** input the test-architect needs — the projected `epics.md`
  (the scope the suite must cover; if missing, offer to run `epics-projection` first), the **architecture
  cross-cutting section** (the *source* strategy: the layered test taxonomy, the per-plane harness, any
  root-gate like a golden-set, any deploy gate like a p95 budget), the **PRD NFR sections** (thresholds come
  from there, not from an FR), and the closed **gate decisions**. Read the test-standards doc whole and
  **identify its `[TBD]`s = the step-06 work list.** Activate the test-architect persona — it drives 02–05;
  the skill feeds it the project delta and enforces topology.
- **02.** Delegate the risk-based plan entirely; feed the coverage taxonomy (the layered test model as
  *mandatory* coverage — none omitted without a reason), the harness mapping, the root gate (treated as
  *living infra* with a recurring cost, not just a test), the deploy exit-criterion, the **traceability**
  (each test zone → AC→FR→Ref so the per-story trace gate can assert it later), and the anchored/movable risk
  lens (anchored = more rigour). Don't re-implement risk analysis; reference the architecture strategy, don't
  duplicate it. A missing layer/gate in the *source* strategy is a **risk to report**, not to fix here.
- **03.** Delegate; feed NFRs **derived from the PRD NFR sections + gate decisions** (performance, security =
  *proving the deny path not just allow*, data-residency, reliability/idempotency, any cost-of-evaluation
  measured as an NFR). Map each threshold to its origin. **Never invent a threshold** — a source-less NFR is
  a gap to route.
- **04.** Delegate the scaffold but **pin the params to the project stack** (unit/integration runner, lint/
  format, schema validation; browser E2E only where a UI exists; service-level E2E against the running
  service, not mocking the seam under test) and apply the **spine-constraints filter** (boring-tech,
  residency/sandboxing, small-team maintainability) — reject anything failing it. Specify fixtures/helpers
  (test-app factory, external-service stubs, an **injectable clock — never real time calls**). Pre-code =
  spec; with-skeleton = real scaffold.
- **05.** Delegate the pipeline but **embed the project gates as blocking, in increasing-cost order** (static
  quality → unit/integration → any deploy-blocking budget → any root gate that gates promotion and must
  assert the lane *actually ran*, assertions > 0 — a green-by-skip doesn't cover its AC → flaky detection).
  Decision-backed gates are *blocking*, not "recommended".
- **06.** **Fill the test-standards `[TBD]`s** *per phase* — leave non-pre-code-resolvable ones marked *with
  what/when resolves them*, don't invent paths. Assert the project invariants (layer coverage, harness,
  blocking decision-gates + deny-path, traceability, stack respected, **no duplication of the architecture
  strategy, source untouched**); list strategy gaps as risks routed to tech-scout/decision-record/
  feature-intake; recommend `governance-check`. **Handoff:** the per-story pipelines READ the test-standards
  doc and execute per-story — **this skill does not invoke them.**

## Guardrails

The **only** hand-written knowledge file is the test-standards doc; plan artifacts are written by the
test-architect in its artifacts dir. Never edits the architecture strategy source, the ROADMAP/decisions/
PRDs, or `epics.md`. Routes **in** from `epics-projection`; routes **out** to the per-story pipelines. Re-run
if the strategy (architecture cross-cutting) or the scope (`epics.md`) changes.
