---
name: decision-intake
description: The process ABOVE feature-intake — take a raw idea, opportunity, request, or discovered technology from "someone said it out loud" to a business-sound, technically-grounded verdict, office-hours style. Diagnoses by phases with kill-gates (business → product → architecture-fit → business-model → verdict), suitable for non-technical stakeholders, capturing a lightweight dossier + a live RADAR + a granular intake graveyard. It NEVER writes governance by hand — the verdict (die · radar · advance) ROUTES to product-spec / feature-intake / decision-record / tech-scout. Use when the user says "I have an idea", "what if we…", "we got an opportunity/request", "I found this platform/vendor", or brings any product/business proposal with no shape yet. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# decision-intake

**Goal:** give a raw idea *shape* — decide whether it dies, sits on the radar, or advances — before any
governance is written. It is the workshop **before** the registry. Nothing here enters the four pillars
until a verdict routes it there. This is the office-hours funnel; obeys the kit's operating contract
(`reference/operating-contract.md`).

## On activation

Read `GOVERNANCE.md` (pillar paths, subsystems, product framing). This is a **conversation, not a form** —
open questions, one thread at a time, in the user's language. Delegate the thinking: `bmad-agent-pm` runs
the business/product diagnosis; `bmad-advanced-elicitation` challenges premises and forces alternatives;
`bmad-agent-architect` (read-only) judges spine-fit; `bmad-agent-analyst` + `bmad-technical-research` size
the business model with real numbers.

## The conversation rules (the real "office-hours" character — do not drop these)

- **Open questions, one at a time, plain language, never multiple-choice forms.** **Push twice** — the first
  answer is the polished version; the real one comes on the 2nd/3rd.
- **Anti-sycophancy is non-negotiable:** take a position every turn + state what evidence would change it.
  Banned: "interesting approach", "you could consider". **Specificity is the only currency** — "professionals"
  is not a customer; a name + a pain + a cost-of-status-quo is.
- **Non-technical-stakeholder safe:** zero jargon, zero bare codes; technical fit is judged by the architect
  persona and the verdict is **translated to plain language**. A "crazy" idea isn't dismissed for being crazy
  — it's dismissed *with a stated reason* or reformulated into a variant that fits (the original dies in the
  graveyard with its reason).
- **Every session closes office-hours style:** dossier updated + **the assignment** (the concrete unblocking
  action, with an owner). Never "let's keep talking".
- **Escape hatch:** if the user says "get to the point", compress to the two critical gates only — **but with
  a non-technical stakeholder, do NOT compress: the process is the protection.**

## Before anything: two gates

- **Scope gate.** Only product/business ideas pass through intake. Internal tooling/process improvements do
  NOT — route them to `AGENT-TODO.md` + `decision-record` and end.
- **Re-litigation gate.** `grep` the idea's terms across the graveyard + RADAR + dossiers *before writing
  anything*. If it died in intake, it doesn't reopen without new facts (cite the row, ask for new facts → a
  new dossier citing the old). If it's already live on the RADAR, resume *that* dossier at its phase.

## Declare the route (smart routing)

- **Complete** (a pivot / a new product line / an opportunity-with-contract): all diagnostic phases deep.
  Always Complete with a non-technical stakeholder.
- **Light** (a small feature of an existing line): business + product compressed; architecture and
  business-model may be "not applicable"; verdict goes straight to `feature-intake`.
- **Tech** (a vendor/library/service): business + product light; the whole technical diagnosis is run by
  `tech-scout` from the architecture phase.

**Two things never skip on any route:** the "is-this-us?" business kill-gate and the mandatory-alternatives
product kill-gate.

## The phased diagnosis (each phase is a kill-gate)

1. **Business** → `bmad-agent-pm` frames demand / status-quo / a named human / the narrowest wedge;
   `bmad-advanced-elicitation` (red-team/pre-mortem) stresses the frailest premise and is **MANDATORY before
   any KILL**. Played against the product's own identity (what IS / what is NOT this product).
2. **Product** → `bmad-agent-pm` for a crisp one-line job-to-be-done + fit with existing lines + **explicit
   committed-vs-hypothesis separation** (a hypothesis dressed as a commitment is governance debt);
   `bmad-advanced-elicitation` generates and stresses **≥2 alternatives from different angles** (another
   wedge, another packaging, "do nothing, revisit in N months", a manual/service version before software).
   Rejected alternatives become **granular graveyard rows** so they aren't re-argued.
3. **Architecture-fit (read-only)** → `bmad-agent-architect`: fits-spine / fits-with-delta / needs-new-spine;
   preliminary anchored-vs-movable; the small-team maintainability filter. **If the idea is a tech question,
   the engine of this phase IS `tech-scout`** — don't duplicate it. Translate the verdict to plain language.
4. **Business-model** → `bmad-agent-analyst` across economic / contractual-legal / offer lenses, with **real
   numbers and a cited source** (`bmad-technical-research` or a web search). **If a number is unknown, say
   "we don't know" and make it an open question — never fill it with a disguised estimate.** Legal work
   needing a human → `HUMAN-TODO.md` (the only write outside the intake workshop).

**Granular death at any gate:** the whole idea, a *variant*, a *feature*, or a considered *vendor* can each
die independently (an intake-graveyard row with phase + reason) while the rest lives on.

## Verdict & routing (human-closed — never writes governance by hand)

The skill *proposes* one of **die · radar · advance**; the human closes it. On **advance** it decomposes and
routes:

- a **whole product line** → `product-spec` (do NOT shred it into N features).
- a **single feature** → `feature-intake`, one by one, with the dossier as *evidence* + explicit
  anti-double-triage ("this is an approved intake; don't re-litigate business/product").
- a **closed decision** → `decision-record`.
- **pending technology** → `tech-scout`.

A **promoted dossier is archived to `history/`.** A RADAR dossier without a named open-question + an
assignment-with-owner is a **zombie** and the session doesn't close. **Graveyard frontier:** the boundary
between the intake-graveyard and the ROADMAP-graveyard is *"has a row in the registry"* — no double-burial.

## Report

The phase-by-phase diagnosis (what passed, where it nearly died), the verdict, and the exact route taken.
Never assign a `D-NN` or a `Ref` here — that's the downstream command's job.
