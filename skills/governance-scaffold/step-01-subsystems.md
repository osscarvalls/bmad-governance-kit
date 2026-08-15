# Step 01 — Fix the subsystems and FR namespaces

**Objective:** lock the small set of **subsystems/layers** the product decomposes into. These are the
backbone of the whole topology: they become the **FR namespaces** (`<SUB>-FRn`), they define what "one FR
per layer" means, and they structure both the PRDs and architecture §B. Getting this right once saves
churn everywhere downstream.

## RULES

- Writes nothing yet — this step **agrees the decomposition**. (The first writes happen in step-02.)
- **Boundaries own questions, not folders.** Each subsystem should own exactly one question ("what does the
  product *know*?", "what does it *decide*?", "what does the user *touch*?"). If two candidate subsystems
  answer the same question, merge them.
- Prefer **few** subsystems (typically 3–6). Over-decomposition makes "one FR per layer" noisy; under-
  decomposition hides real seams. When unsure, delegate the boundary call to **`bmad-agent-architect`**.

## 1 · Derive the candidate decomposition from the plan

From the architecture's module boundaries and the PRD's structure (recorded in step-00), draft the
subsystem set. For each candidate subsystem capture:

- **Name** — a stable, human name (this is what people say).
- **The one question it owns** — one sentence.
- **Namespace prefix** — a short uppercase slug for its FRs (e.g. `CORE`, `API`, `DATA`, `UI`, `AGENT`).
  This is the FR namespace: requirements for that subsystem are numbered `<PREFIX>-FR1`, `<PREFIX>-FR2`, …
- **Provenance** — which part of the plan it came from (`path:line`).

> **Namespacing, not a global sequence.** FRs are numbered **per subsystem** (`CORE-FR1`, `API-FR1` are
> different requirements), never one global `FR-1..N` counter. This is what makes `grep <PREFIX>-FR` return
> exactly one subsystem's requirements.

## 2 · Reconcile with the existing PRD numbering (merge mode)

If the PRD already uses `FR-1..N` (a global sequence) or ad-hoc numbering, **do not renumber destructively.**
Plan a mapping table (old id → `<PREFIX>-FRn`) that step-03 will apply, and keep the old id visible as an
alias on first migration so existing references (in stories, commits, tickets) still resolve. In greenfield
mode you assign clean namespaced ids directly.

## 3 · Handle NFRs and provisional slugs

- **NFRs are not subsystems and not FRs.** Latency, security, residency, cost, observability, accessibility
  → they will live in an **NFR section** of the relevant PRD (step-03), not as a subsystem here.
- **Provisional slugs.** Cross-cutting capabilities the plan mentions but hasn't assigned to a layer yet
  (integration seams, ops, legal, UX) can carry a **provisional slug** (`INT-*`, `OPS-*`, `UX-*`, `LEG-*`)
  until the PRD gives them a real FR. Note them; step-02 will register them, step-03 resolves them.

## CHECKPOINT — Confirm the decomposition

Present the subsystem table: **Name · the one question it owns · namespace prefix · provenance**, plus the
old→new FR mapping (merge mode) and the list of provisional slugs. Flag anywhere the plan was silent and you
had to propose a boundary.

**Stop and wait.** Are these the right subsystems and namespaces? This set is load-bearing for every later
step — do not proceed until confirmed.

## Next step

Once the decomposition is confirmed, read it fully and follow: `./step-02-registry.md`.
