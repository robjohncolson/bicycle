#!/usr/bin/env python3
"""Diff two Phaserunner Suite parameter exports (Baserunner/Phaserunner XML).

Usage: python3 tune-diff.py OLD.xml NEW.xml

Emits a markdown table of every Address whose Value differs, using the
parameter Notes to give the human decode. Where Notes describes a bitfield
(lines of the form "N - X [label]"), the specific bits that flipped are
decoded from the integer values — "bit 11: 0->1 [Power Map enable]" is
useful; "174: 1024 -> 3072" is not. Addresses present in only one file are
listed separately.

Stdlib only. The Suite export format is ArrayOfSerializableParameter with
<Address>/<Value>/<Notes> triples; Value is always an integer register.
"""

import re
import sys
import xml.etree.ElementTree as ET

BIT_LINE = re.compile(r"^\s*(\d+)\s*-\s*([01])\s*\[(.*?)\]\s*$")


def parse_export(path):
    """Return {address:int -> (value:int, notes:str)}."""
    params = {}
    root = ET.parse(path).getroot()
    for p in root.iter("SerializableParameter"):
        addr = int(p.findtext("Address"))
        value = int(p.findtext("Value"))
        notes = (p.findtext("Notes") or "").strip()
        params[addr] = (value, notes)
    return params


def bit_labels(notes):
    """Return {bit:int -> label:str} if Notes is a bitfield decode, else {}."""
    labels = {}
    for line in notes.splitlines():
        m = BIT_LINE.match(line)
        if m:
            labels[int(m.group(1))] = m.group(3).strip()
    # A real bitfield decode lists several bits; one stray match is noise.
    return labels if len(labels) >= 2 else {}


def summary_line(notes):
    """First line of Notes: the parameter name and decoded value."""
    return notes.splitlines()[0].strip() if notes else "(no notes)"


def param_name(notes):
    """Name portion of the Notes first line (text before the first colon)."""
    first = summary_line(notes)
    return first.split(":", 1)[0].strip() if ":" in first else first


def decoded_value(notes):
    """Decoded-value portion of the Notes first line (text after the colon)."""
    first = summary_line(notes)
    if ":" in first:
        rest = first.split(":", 1)[1].strip()
        if rest:
            return rest
    return ""


def describe_bit_changes(old_val, new_val, labels):
    """List which bits differ between two register values, with labels."""
    changes = []
    for bit in range(max(old_val.bit_length(), new_val.bit_length(), 16)):
        ob = (old_val >> bit) & 1
        nb = (new_val >> bit) & 1
        if ob != nb:
            label = labels.get(bit, "?")
            changes.append(f"bit {bit}: {ob}->{nb} [{label}]")
    return changes


def md_escape(text):
    return text.replace("|", "\\|")


def main(argv):
    if len(argv) != 3:
        print(__doc__.strip().splitlines()[2], file=sys.stderr)
        return 2
    old_path, new_path = argv[1], argv[2]
    old = parse_export(old_path)
    new = parse_export(new_path)

    changed = sorted(a for a in old.keys() & new.keys() if old[a][0] != new[a][0])
    only_old = sorted(old.keys() - new.keys())
    only_new = sorted(new.keys() - old.keys())

    print(f"# Tune diff: `{old_path}` -> `{new_path}`")
    print()
    print(f"{len(old)} params in old, {len(new)} in new, "
          f"{len(changed)} changed, {len(only_old)} removed, {len(only_new)} added.")
    print()

    if changed:
        print("## Changed values")
        print()
        print("| Addr | Parameter | Old | New | Detail |")
        print("|---|---|---|---|---|")
        for addr in changed:
            old_val, old_notes = old[addr]
            new_val, new_notes = new[addr]
            labels = bit_labels(new_notes) or bit_labels(old_notes)
            name = param_name(new_notes) or param_name(old_notes)
            if labels:
                detail = "; ".join(describe_bit_changes(old_val, new_val, labels))
                old_disp, new_disp = str(old_val), str(new_val)
            else:
                old_dec = decoded_value(old_notes)
                new_dec = decoded_value(new_notes)
                old_disp = f"{old_val} ({old_dec})" if old_dec else str(old_val)
                new_disp = f"{new_val} ({new_dec})" if new_dec else str(new_val)
                detail = ""
            print(f"| {addr} | {md_escape(name)} | {md_escape(old_disp)} "
                  f"| {md_escape(new_disp)} | {md_escape(detail)} |")
        print()

    for title, addrs, side in (("Only in old file", only_old, old),
                               ("Only in new file", only_new, new)):
        if addrs:
            print(f"## {title}")
            print()
            print("| Addr | Parameter | Value |")
            print("|---|---|---|")
            for addr in addrs:
                val, notes = side[addr]
                dec = decoded_value(notes)
                disp = f"{val} ({dec})" if dec else str(val)
                print(f"| {addr} | {md_escape(param_name(notes))} | {md_escape(disp)} |")
            print()

    if not (changed or only_old or only_new):
        print("No differences.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
