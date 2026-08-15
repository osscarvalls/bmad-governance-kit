---
name: decision-intake
description: The process ABOVE feature-intake — take a raw idea, opportunity, request, or discovered technology from "someone said it out loud" to a business-sound, technically-grounded verdict, office-hours style. Diagnoses by phases with kill-gates (business → product → architecture-fit → business-model → verdict), suitable for non-technical stakeholders, and captures a lightweight dossier + a live RADAR + a granular intake graveyard at each transition. It NEVER writes governance by hand — the verdict (die · radar · advance) ROUTES to feature-intake / decision-record / tech-scout. Use when the user says "I have an idea", "what if we…", "we got an opportunity/request", "I found this platform/vendor", or brings any product/business proposal that has no shape yet. Requires a governance layer (see governance-scaffold); reads GOVERNANCE.md.
---

# decision-intake

**Goal:** give a raw idea *shape* — diagnose whether it should die, sit on the radar, or advance — before
any governance is written. It is the workshop **before** the registry; nothing here enters the four pillars
until a verdict routes it there.

## On activation

1. **Resolve the layer.** Read `{gov}/GOVERNANCE.md` for the pillar paths, the subsystem set, and the
   product framing. If there is no governance layer, you can still run the diagnosis, but say the verdict
   can't be landed until `governance-scaffold` exists.
2. Talk to the user in their language. This is a **conversation**, not a form — ask open questions, one
   thread at a time.
3. Delegate the thinking to BMAD where available: `bmad-agent-pm` (John) runs the business/product
   diagnosis; `bmad-advanced-elicitation` challenges premises and forces alternatives; `bmad-agent-architect`
   (Winston, read-only) judges spine-fit; `bmad-agent-analyst` (Mary) + `bmad-technical-research` size the
   business model with real numbers.

## The phased diagnosis (each phase is a kill-gate)

Run in order. A phase can **kill** the idea (→ verdict: die, with a reason) or send it to the **radar**
(promising but not now). Only an idea that clears every gate reaches "advance".

1. **Business.** What job does this do, for whom, why now? What breaks if we don't? If there's no real job
   or no one who feels the pain → kill or radar.
2. **Product.** What's the thinnest version that delivers the value? Force at least one alternative
   (`bmad-advanced-elicitation`). If every version is bloated or the value is diffuse → kill or radar.
3. **Architecture-fit (read-only).** Does it fit the spine, or does it demand a retrofit? Is it boring-tech,
   maintainable by a small team? Does it clash with a **live** `D-NN`? If it forces a spine rewrite with no
   commensurate payoff → kill, radar, or (if it's fundamentally a tech question) route to `tech-scout`.
4. **Business model.** Does the math work — cost to build/run vs value captured? Use real numbers
   (`bmad-technical-research`). If it can't pay for itself → kill or radar.
5. **Verdict.** die · radar · advance.

## Capture as you go (the workshop artifacts — NOT governance)

Keep a lightweight dossier per idea under a workshop area (e.g. `{gov}/_intake/`), plus a live **RADAR**
(ideas parked, not dead) and an **intake graveyard** (granular deaths: phase reached + reason). These are
pre-governance scratch — they are **not** the ROADMAP Backlog or the DECISIONS log. The boundary: an idea
earns a ROADMAP row only when a verdict advances it.

## The verdict routes (never write governance by hand)

- **die** → record the death in the intake graveyard with the phase + reason. If it also closes a real
  decision (e.g. "we will not do X"), route to `decision-record`.
- **radar** → park it on the RADAR with what would have to change for it to advance.
- **advance** →
  - a **new feature** → `feature-intake` (Backlog → triage → FRs).
  - a **closed decision** → `decision-record` (append-only `D-NN` + propagation).
  - a **technology to adopt** → `tech-scout` (evaluate → adopt/record).

## Report

Show the phase-by-phase diagnosis (what passed, where it nearly died), the verdict, and the exact route
taken. Never assign a `D-NN` or a `Ref` here — that's the downstream command's job.
