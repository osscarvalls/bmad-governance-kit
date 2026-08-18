#!/usr/bin/env python3
"""Validate the release-calendar.yaml join against the PRDs (schema, not fragile grep).

Project-agnostic: everything project-specific (subsystem FR namespaces, PRD paths, the
milestone vocabulary) is read from the calendar's own top-level `config:` block, so this
script is copied verbatim into any governed project.

Checks:
  1. Every FR listed in the calendar exists as `#### <NS>-FRn` in its subsystem PRD.
  2. Every (feature, FR) pair: the FR's tag in the PRD declares `serves <feature>`.
  3. Every feature named in a PRD `serves` clause exists as an entry in the calendar.
Output: a report + exit 0 (PASS) / exit 1 (there are ERRORs).

Requires: PyYAML (`pip install pyyaml`).
"""
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent
CAL = ROOT / "release-calendar.yaml"


def load_config(cal):
    """Resolve subsystem namespaces + PRD paths + the FR/tag regexes from `config:`."""
    cfg = cal.get("config") or {}
    subs = cfg.get("subsystems") or {}
    if not subs:
        sys.exit("ERROR: calendar `config.subsystems` is empty — cannot resolve PRDs/namespaces.")
    prd_dir = ROOT / (cfg.get("prd_dir") or "prds")
    prds = {ns: prd_dir / fname for ns, fname in subs.items()}
    ns_alt = "|".join(re.escape(ns) for ns in subs)
    fr_re = re.compile(rf"^####\s+((?:{ns_alt})-FR\d+)\b", re.M)
    # The FR-side declaration lives ONLY in the backtick tag on the line right after the
    # header: `#### <FR> — Title` then `` `[... · serves <feature>, <feature2>]` ``.
    tag_re = re.compile(rf"^####\s+((?:{ns_alt})-FR\d+)[^\n]*\n\s*`\[([^\]\n]*)\]", re.M)
    return prds, fr_re, tag_re


def parse_serves(bracket):
    """Extract the feature-handle list from a tag bracket's `serves ...` segment."""
    if "serves" not in bracket:
        return set()
    seg = bracket.split("serves", 1)[1]
    handles = set()
    for raw in re.split(r"[,;]", seg):
        h = raw.split("→")[0].split("·")[0]  # drop "→ <FR>" and "· <D-NN>"
        h = re.sub(r"\s*\(.*$", "", h)  # drop trailing "(platform layer)" etc.
        h = h.strip().strip("`").strip()
        if h and " " not in h:  # a real handle token has no spaces
            handles.add(h)
    return handles


def load_prds(prds, fr_re, tag_re):
    """Return (existing_frs:set, fr_to_serves:dict FR->set(handle), all_served:set)."""
    existing = set()
    fr_serves = {}
    served = set()
    for text in (p.read_text() for p in prds.values() if p.exists()):
        existing.update(fr_re.findall(text))
        for fr, bracket in tag_re.findall(text):
            handles = parse_serves(bracket)
            fr_serves.setdefault(fr, set()).update(handles)
            served.update(handles)
    return existing, fr_serves, served


def main():
    if not CAL.exists():
        sys.exit(f"ERROR: {CAL} not found.")
    cal = yaml.safe_load(CAL.read_text())
    prds, fr_re, tag_re = load_config(cal)
    existing, fr_serves, served = load_prds(prds, fr_re, tag_re)

    cal_handles = set()
    pairs = []  # (feature, FR)
    for rel in (cal.get("releases") or {}).values():
        for block in ("features", "enablers"):
            for handle, entry in (rel.get(block) or {}).items():
                cal_handles.add(handle)
                for fr in (entry or {}).get("frs", []) or []:
                    pairs.append((handle, fr))

    errors, warns = [], []
    for handle, fr in pairs:
        if fr not in existing:
            errors.append(f"FR {fr} (feature {handle}) does NOT exist in any PRD")
        elif handle not in fr_serves.get(fr, set()):
            warns.append(f"join: {fr} does not declare `serves {handle}` in its PRD")
    for handle in sorted(served - cal_handles):
        warns.append(f"orphan: a PRD declares `serves {handle}` but {handle} is not a calendar feature")

    print(f"features={len(cal_handles)} · (feature,FR) pairs={len(pairs)} · FRs in PRDs={len(existing)}")
    for e in errors:
        print("  ERROR ·", e)
    for w in warns:
        print("  WARN  ·", w)
    print(f"\n{'FAIL' if errors else 'PASS'} — {len(errors)} errors, {len(warns)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
