#!/usr/bin/env python3
"""Copy stable identity and provenance metadata from a frozen PaperWarehouse revision."""

import ast
import json
from pathlib import Path

WAREHOUSE = Path("/Users/oian/Documents/PaperWarehouse")
OUT = Path(__file__).resolve().parent / "manifest.jsonl"
REVISION = "118a82ce657a2bf6915afdc82921553dc765740a"


def scalar(value):
    value = value.strip()
    if value in {"null", "~"}:
        return None
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value.strip('"')


def record(path):
    text = path.read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line and not line.startswith((" ", "-")):
            key, value = line.split(":", 1)
            fields[key.strip()] = scalar(value)
    return {
        "paper_id": fields["paper_id"],
        "title": fields["title"],
        "year": int(fields["publication_year"]),
        "track": fields.get("track"),
        "doi": fields.get("doi"),
        "official_paper_url": fields.get("official_paper_url"),
        "warehouse_revision": REVISION,
    }


paths = sorted((WAREHOUSE / "library" / "papers").glob("sigkdd-*.md"))
rows = [record(path) for path in paths]
rows.sort(key=lambda row: (-row["year"], row["paper_id"]))
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows), encoding="utf-8")
print(json.dumps({"records": len(rows), "warehouse_revision": REVISION}))
