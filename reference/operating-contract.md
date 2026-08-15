# The operating contract (shared by every skill in the kit)

Every skill in this kit obeys the same contract. It is stated once here and referenced by each `SKILL.md`
so the skills stay thin. If you extend the kit, a new skill must honour all of it.

## On activation

1. **Resolve the layer.** Read the target project's `GOVERNANCE.md` (the constitution the scaffolder wrote)
   to get the four pillar paths, the subsystem set + their FR namespaces, and the anti-drift laws. It is
   **binding**: if a skill and the constitution disagree, the constitution wins and the skill is the bug. If
   there is no governance layer, stop and route to `governance-scaffold`.
2. **Resolve the date** from the system clock, in absolute `YYYY-MM-DD` form.
3. **Language discipline.** Converse in the user's language. When *editing* a governed document, preserve
   *that document's* existing language — never translate on the fly. Quote/report in the source doc's
   language.

## Step processing (for multi-step skills)

1. **Read the whole step file before acting.**
2. **Follow the sequence** — never load two step files at once, never skip a step.
3. **Wait at every CHECKPOINT** for the human's decision.
4. **Load the next** step only when the current one says so.
5. **Smart routing exempts *content*, not the *load*.** A phase may run "light" or be declared "not
   applicable", but its step file is still loaded and the exemption is justified in one line.

## The delegation law

BMAD is the brain; the skill is the discipline. Could a BMAD command do this step? Then it does. **Every
step names the exact command it delegates to** — a step without its command cited is a bug in the skill.
Where a BMAD command is unavailable, the skill does the work itself and **says so** (graceful degradation).

## Write-scope declaration (the single most protective invariant)

Every skill **declares, up front, the only files it may write**, and routes everything else to the skill
that owns it. Read-only auditors write nothing. The scribe (`decision-record`) is the only writer of the
decision log. `governance-scaffold` is the only skill that creates fresh pillars; the operators edit
existing ones. `epics-projection` writes only the projection. `fix` writes only code/tests. A skill that is
about to write outside its scope has found a routing bug, not a task.

## Universal conventions

- **`path:line` citations** — cite files as clickable `path:line`, never paraphrase a location.
- **Absolute dates** (`2026-08-15`), never relative ("last week").
- **Reference, don't restate** — cite the `Ref`/`FR`/`D-NN`, don't copy its content.
- **Affirmative · timeless · additive** — durable knowledge states what *is*, not what isn't; avoid claims
  that expire. When state changes, add or supersede.
- **Talk to humans in names, not codes** — in chat/briefings/reports, name things in plain language; put a
  code in parentheses *after* the name if it adds traceability, never in place of it. Codes are the join key
  *between documents*, not the language for humans.
- **Tight, decision-first reports** — scannable, not walls of text.
- **Professional register** in any client-/stakeholder-facing output.

## Optional customization

A project may ship a `customize.toml` next to a skill to override its workflow (extra activation steps,
persistent facts, model tiers). Resolve base → team → user, deep-merging tables and concatenating arrays.
Absent files are skipped. This is optional; the skills work without it.
