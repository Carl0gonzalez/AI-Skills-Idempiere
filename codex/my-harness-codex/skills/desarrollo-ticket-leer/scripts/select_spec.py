#!/usr/bin/env python3
"""Choose a ticket-specific numeric version without exposing attachment URLs."""
import argparse
import json
import re


def select(ticket, attachments):
    pattern = re.compile(r"spec-" + re.escape(ticket) + r"-v([1-9][0-9]*)\.md", re.IGNORECASE)
    candidates = []
    for entry in attachments:
        name = entry.get("title") or entry.get("name") or ""
        match = pattern.fullmatch(name)
        if match:
            candidates.append({"name": name, "version": int(match[1]),
                               "date": entry.get("date", entry.get("created_at"))})
    if not candidates:
        return {"status": "not_found", "ticket": ticket, "candidates": []}
    version = max(x["version"] for x in candidates)
    newest = [x for x in candidates if x["version"] == version]
    return {"status": "selected" if len(newest) == 1 else "ambiguous",
            "ticket": ticket, "candidates": newest}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ticket", required=True)
    parser.add_argument("--attachments", required=True)
    args = parser.parse_args()
    try:
        with open(args.attachments, encoding="utf-8") as handle:
            entries = json.load(handle)
        if not isinstance(entries, list) or not all(isinstance(x, dict) for x in entries):
            raise ValueError("Expected a JSON list of normalized attachment objects")
        print(json.dumps(select(args.ticket, entries), ensure_ascii=False))
    except (OSError, ValueError, TypeError) as exc:
        parser.exit(2, str(exc) + "\n")


if __name__ == "__main__":
    main()
