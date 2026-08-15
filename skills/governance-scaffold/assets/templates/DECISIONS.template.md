---
title: "<Project> — Decision Log (append-only)"
status: living
created: <YYYY-MM-DD>
governance: |
  Append-only. A closed decision is NOT edited or deleted. The only permitted edits are additive
  forward-pointers: `· SUPERSEDED-BY D-NN` (replaces it → old one becomes SUPERSEDED) or
  `· reframed|narrowed|refined by D-NN` (stays IN-FORCE; only its scope/reading changes).
  A change of substance = a new entry + SUPERSEDED-BY; a reframe = the old one stays alive + its pointer.
  The ROADMAP references these IDs; it never re-debates the decision. Long rationale/evidence lives in
  history/, not here — this is the consultable index.
sources:
  - history/<acta-file>.md   (<D-NN>..<D-NN>)
  - <session, no acta file> — <YYYY-MM-DD>   (<D-NN>)
---

# <Project> — Decision Log

> Format: `D-NN · title — decision (1 line) → *EFFECT* · [IN-FORCE|SUPERSEDED] · source`
> Effect verbs: CREATES · CONSTRAINS · KILLS · MOVES · PROMOTES · REWORKS · REFRAMES · governance.

## <Session / theme heading (<YYYY-MM-DD>)>

- **D-01 · <title>.** <the decision in one line.> → *CREATES <what it adds in features>.* IN-FORCE · <source>
- **D-02 · <title>.** <one-line decision.> → *CONSTRAINS <x>.* IN-FORCE · <source>

## <Next session heading (<YYYY-MM-DD>)>

<!-- A superseded entry keeps its ORIGINAL text and only gains its pointer: -->
- **D-03 · <title>.** <original one-line decision, never rewritten.> → *<original effect>.* SUPERSEDED-BY D-07 · <source>
<!-- A reframed-but-still-live entry: -->
- **D-04 · <title>.** <original decision.> → *<original effect>.* IN-FORCE · reframed by D-09 (<what it narrowed>) · <source>
