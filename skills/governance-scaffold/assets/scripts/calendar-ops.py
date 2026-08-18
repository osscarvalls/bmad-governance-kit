#!/usr/bin/env python3
"""Structured operation over release-calendar.yaml: parse, mutate and dump the yaml while
preserving the header comment. This is the ONLY sanctioned way to write the calendar —
never hand-edit it and never mutate it by string-match.

Project-agnostic: the milestone vocabulary is read from the calendar's own `config.milestones`,
so this script is copied verbatim into any governed project.

Subcommands:
  get [<entry>]                            print the calendar (or one entry) as JSON
  add <features|enablers> <entry> --milestone <m> [--frs ..] [--nfrs ..] [--release v1.0]
  set-frs <entry> <FR ..>                  replace frs[]  (also set-nfrs / set-epics / set-stories)
  add-frs <entry> <FR ..>                  append to frs[] without dupes (also add-nfrs / add-epics / add-stories)
  set-status <entry> <status>              entry status (backlog|in-progress|done|unscheduled|blocked|killed)
  set-milestone <entry> <milestone>        entry milestone (validated against config.milestones)
  add-decision <entry> <D-NN ..>           append to decisions[] without dupes
  rename <entry> <new-name>                rename the entry

After every write run: python3 validate-release-calendar.py (must still be PASS).

Requires: PyYAML (`pip install pyyaml`).
"""
import argparse
import json
import sys
from pathlib import Path

import yaml

CAL = Path(__file__).resolve().parent / "release-calendar.yaml"
STATUSES = {"backlog", "in-progress", "done", "unscheduled", "blocked", "killed"}
LIST_FIELDS = ("frs", "nfrs", "epics", "stories")


def load():
    text = CAL.read_text()
    header = []
    for line in text.splitlines():
        if line.startswith("#"):
            header.append(line)
        else:
            break
    return header, yaml.safe_load(text)


def dump(header, data):
    body = yaml.safe_dump(
        data, sort_keys=False, allow_unicode=True, default_flow_style=None, width=4096
    )
    CAL.write_text("\n".join(header) + "\n" + body)


def milestones(data):
    ms = ((data.get("config") or {}).get("milestones")) or []
    if not ms:
        sys.exit("ERROR: calendar `config.milestones` is empty — cannot validate milestones.")
    return ms


def find(data, name):
    """Return (entry_dict, container_dict) for entry `name` across all releases/blocks."""
    for rel in (data.get("releases") or {}).values():
        for block in ("features", "enablers"):
            entries = rel.get(block) or {}
            if name in entries:
                return entries[name], entries
    sys.exit(f"ERROR: entry '{name}' does not exist in the calendar")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="cmd", required=True)

    g = sub.add_parser("get")
    g.add_argument("name", nargs="?")

    a = sub.add_parser("add")
    a.add_argument("block", choices=["features", "enablers"])
    a.add_argument("name")
    a.add_argument("--milestone", required=True)
    a.add_argument("--frs", nargs="*", default=[])
    a.add_argument("--nfrs", nargs="*", default=[])
    a.add_argument("--release", default=None)

    for field in LIST_FIELDS:
        for verb in ("set", "add"):
            s = sub.add_parser(f"{verb}-{field}")
            s.add_argument("name")
            s.add_argument("values", nargs="+")

    e = sub.add_parser("set-status")
    e.add_argument("name")
    e.add_argument("status", choices=sorted(STATUSES))

    m = sub.add_parser("set-milestone")
    m.add_argument("name")
    m.add_argument("milestone")

    d = sub.add_parser("add-decision")
    d.add_argument("name")
    d.add_argument("values", nargs="+")

    r = sub.add_parser("rename")
    r.add_argument("name")
    r.add_argument("new_name")

    args = p.parse_args()
    header, data = load()

    if args.cmd == "get":
        out = find(data, args.name)[0] if args.name else data
        print(json.dumps(out, indent=2, ensure_ascii=False))
        return

    if args.cmd == "add":
        if args.milestone not in milestones(data):
            sys.exit(f"ERROR: milestone '{args.milestone}' not in config.milestones {milestones(data)}")
        releases = data.setdefault("releases", {})
        rel_name = args.release or next(iter(releases), None)
        if rel_name is None:
            sys.exit("ERROR: no releases exist yet — pass --release <name> to create the first one.")
        rel = releases.setdefault(rel_name, {"status": "backlog"})
        entries = rel.setdefault(args.block, {})
        if args.name in entries:
            sys.exit(f"ERROR: '{args.name}' already exists in {rel_name}.{args.block}")
        entries[args.name] = {
            "milestone": args.milestone,
            "frs": list(args.frs),
            "nfrs": list(args.nfrs),
            "epics": [],
            "stories": [],
        }
    elif args.cmd == "set-status":
        find(data, args.name)[0]["status"] = args.status
    elif args.cmd == "set-milestone":
        if args.milestone not in milestones(data):
            sys.exit(f"ERROR: milestone '{args.milestone}' not in config.milestones {milestones(data)}")
        find(data, args.name)[0]["milestone"] = args.milestone
    elif args.cmd == "add-decision":
        entry = find(data, args.name)[0]
        cur = entry.setdefault("decisions", [])
        entry["decisions"] = cur + [v for v in args.values if v not in cur]
    elif args.cmd == "rename":
        entry, container = find(data, args.name)
        if args.new_name in container:
            sys.exit(f"ERROR: '{args.new_name}' already exists")
        del container[args.name]
        container[args.new_name] = entry
    else:
        verb, field = args.cmd.split("-", 1)
        entry = find(data, args.name)[0]
        if verb == "set":
            entry[field] = list(args.values)
        else:
            cur = entry.setdefault(field, [])
            entry[field] = cur + [v for v in args.values if v not in cur]

    dump(header, data)
    print(f"OK · {args.cmd} applied. Validate: python3 {CAL.parent / 'validate-release-calendar.py'}")


if __name__ == "__main__":
    main()
