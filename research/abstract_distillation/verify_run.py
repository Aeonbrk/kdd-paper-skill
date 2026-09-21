#!/usr/bin/env python3
"""Check concrete structural invariants of the KDD card run."""

from __future__ import annotations

import json
from collections import Counter
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CARDS = ROOT / "research" / "abstract_distillation" / "cards"
CACHE = ROOT / "research" / ".cache" / "openalex_records.json"
MANIFEST = ROOT / "research" / "corpus" / "manifest.jsonl"


def load_manifest():
    return [
        json.loads(line)
        for line in MANIFEST.read_text(encoding="utf-8").splitlines()
        if line
    ]


def load_cards():
    return [
        json.loads(path.read_text(encoding="utf-8"))
        for path in sorted(CARDS.glob("*.json"))
    ]


def abstract_for(card, openalex):
    item = openalex.get((card.get("doi") or "").lower())
    if not item:
        return ""
    index = item.get("abstract_inverted_index") or {}
    words = sorted(
        (position, word)
        for word, positions in index.items()
        for position in positions
    )
    return " ".join(word for _, word in words)


def source_ids(value):
    if isinstance(value, dict):
        ids = value.get("source_ids", [])
        nested = []
        for child in value.values():
            nested.extend(source_ids(child))
        return ids + nested
    if isinstance(value, list):
        result = []
        for child in value:
            result.extend(source_ids(child))
        return result
    return []


def claims(value):
    if isinstance(value, dict):
        found = []
        if isinstance(value.get("claim"), str):
            found.append(value["claim"])
        if isinstance(value.get("summary"), str):
            found.append(value["summary"])
        for child in value.values():
            found.extend(claims(child))
        return found
    if isinstance(value, list):
        result = []
        for child in value:
            result.extend(claims(child))
        return result
    return []


def main():
    manifest = load_manifest()
    cards = load_cards()
    cache_available = CACHE.exists()
    openalex = (
        json.loads(CACHE.read_text(encoding="utf-8"))
        if cache_available
        else {}
    )

    expected = {row["paper_id"]: row for row in manifest}
    actual = {card["paper_id"]: card for card in cards}
    errors = []

    if len(manifest) != 3696:
        errors.append(f"manifest count {len(manifest)} != 3696")
    if len(cards) != 3696 or len(actual) != 3696:
        errors.append(f"card count/uniqueness: {len(cards)}/{len(actual)}")
    if set(expected) != set(actual):
        errors.append("card identity set differs from manifest")

    year_expected = Counter(row["year"] for row in manifest)
    year_actual = Counter(card["year"] for card in cards)
    if year_expected != year_actual:
        errors.append(f"year counts differ: {year_expected} vs {year_actual}")

    source_counts = Counter()
    state_counts = Counter()
    structural_checked = 0
    copy_ratios = []

    for card in cards:
        state = card.get("validation_state")
        state_counts[(card["year"], state)] += 1

        if card.get("reading_level") != "abstract_only":
            errors.append(f"wrong reading level {card['paper_id']}")
        if card.get("title") != expected.get(card["paper_id"], {}).get("title"):
            errors.append(f"title changed {card['paper_id']}")

        if state == "completed":
            structural_checked += 1
            source_counts[card.get("abstract_source")] += 1
            if not card.get("source_locator") or not card.get("source_units"):
                errors.append(f"completed card lacks source {card['paper_id']}")

            unit_ids = {unit["id"] for unit in card.get("source_units", [])}
            for source_id in source_ids(card):
                if source_id not in unit_ids:
                    errors.append(
                        f"invalid source id {card['paper_id']}:{source_id}"
                    )

            if cache_available:
                abstract = abstract_for(card, openalex)
                for claim in claims(card):
                    if abstract:
                        copy_ratios.append(
                            SequenceMatcher(
                                None, claim.lower(), abstract.lower()
                            ).ratio()
                        )
        elif state == "missing_source":
            if card.get("source_locator") or card.get("source_units"):
                errors.append(
                    f"missing card has source data {card['paper_id']}"
                )
        else:
            errors.append(
                f"unknown validation state {card['paper_id']}:{state}"
            )

    if cache_available:
        copy_similarity = {
            "status": "checked",
            "claims_checked": len(copy_ratios),
            "max": max(copy_ratios) if copy_ratios else 0.0,
            "over_0_8": sum(value > 0.8 for value in copy_ratios),
        }
    else:
        copy_similarity = {
            "status": "not_checked_no_source_cache",
            "claims_checked": 0,
        }

    result = {
        "manifest_count": len(manifest),
        "card_count": len(cards),
        "year_counts": dict(sorted(year_actual.items())),
        "state_counts": {
            f"{year}:{state}": count
            for (year, state), count in sorted(state_counts.items())
        },
        "source_counts": dict(source_counts),
        "structural_source_linkage_checked": structural_checked,
        "semantic_fidelity_audit": "not_performed",
        "copy_similarity": copy_similarity,
        "errors": errors,
    }

    out_path = ROOT / "research" / "abstract_distillation" / "verification.json"
    out_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
