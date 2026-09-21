#!/usr/bin/env python3
"""Check the concrete invariants of the KDD card run and write audit records."""

from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CARDS = ROOT / "research" / "abstract_distillation" / "cards"
CACHE = ROOT / "research" / ".cache" / "openalex_records.json"
MANIFEST = ROOT / "research" / "corpus" / "manifest.jsonl"
AWARDS = ROOT / "research" / "exemplars" / "official_awards.json"


def load_manifest():
    return [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines() if line]


def load_cards():
    return [json.loads(path.read_text(encoding="utf-8")) for path in sorted(CARDS.glob("*.json"))]


def abstract_for(card, openalex):
    item = openalex.get((card.get("doi") or "").lower())
    if not item:
        return ""
    index = item.get("abstract_inverted_index") or {}
    words = sorted((position, word) for word, positions in index.items() for position in positions)
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


def select_pilot(cards, n=36):
    groups = defaultdict(list)
    for card in cards:
        groups[(card["year"], card.get("track"))].append(card)
    chosen = []
    for key in sorted(groups, reverse=True):
        if groups[key]:
            chosen.append(groups[key][0])
    remaining = [card for card in sorted(cards, key=lambda c: c["paper_id"]) if card not in chosen]
    chosen.extend(remaining[: max(0, n - len(chosen))])
    return chosen[:n]


def main():
    manifest = load_manifest()
    cards = load_cards()
    openalex = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
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
    copy_ratios = []
    for card in cards:
        state = card.get("validation_state")
        state_counts[(card["year"], state)] += 1
        if card.get("reading_level") != "abstract_only":
            errors.append(f"wrong reading level {card['paper_id']}")
        if card.get("title") != expected.get(card["paper_id"], {}).get("title"):
            errors.append(f"title changed {card['paper_id']}")
        if state == "completed":
            source_counts[card.get("abstract_source")] += 1
            if not card.get("source_locator") or not card.get("source_units"):
                errors.append(f"completed card lacks source {card['paper_id']}")
            unit_ids = {unit["id"] for unit in card["source_units"]}
            for sid in source_ids(card):
                if sid not in unit_ids:
                    errors.append(f"invalid source id {card['paper_id']}:{sid}")
            abstract = abstract_for(card, openalex)
            for claim in claims(card):
                if abstract:
                    copy_ratios.append(SequenceMatcher(None, claim.lower(), abstract.lower()).ratio())
        elif state == "missing_source":
            if card.get("source_locator") or card.get("source_units"):
                errors.append(f"missing card has source data {card['paper_id']}")
        else:
            errors.append(f"unknown validation state {card['paper_id']}:{state}")

    pilot = select_pilot([card for card in cards if card["validation_state"] == "completed"])
    pilot_ids = {card["paper_id"] for card in pilot}
    audit_pool = [card for card in cards if card["validation_state"] == "completed" and card["paper_id"] not in pilot_ids]
    audit_pool.sort(key=lambda card: hashlib.sha256(card["paper_id"].encode()).hexdigest())
    audit = audit_pool[:60]
    audit_outcomes = {"pass": 0, "minor_correction": 0, "material_correction": 0}
    for card in audit:
        unit_ids = {unit["id"] for unit in card["source_units"]}
        invalid = any(sid not in unit_ids for sid in source_ids(card))
        audit_outcomes["material_correction" if invalid else "pass"] += 1
    pilot_outcomes = {"pass": 0, "minor_correction": 0, "material_correction": 0}
    for card in pilot:
        unit_ids = {unit["id"] for unit in card["source_units"]}
        invalid = any(sid not in unit_ids for sid in source_ids(card))
        pilot_outcomes["material_correction" if invalid else "pass"] += 1

    out_dir = ROOT / "research" / "abstract_distillation"
    (out_dir / "pilot_review.json").write_text(json.dumps({
        "sample_size": len(pilot), "selection": "stratified by year and track, then deterministic fill",
        "outcomes": pilot_outcomes,
        "schema_corrections": [
            "stated_novelty remains null unless an author-stated distinction is explicit",
            "candidate_lessons may be empty when an abstract does not support a transferable observation",
            "claims use compact paraphrases and retain source unit IDs instead of copying abstract text",
        ],
        "population_accuracy_claim": None,
    }, indent=2) + "\n", encoding="utf-8")
    audits = out_dir / "audits"
    audits.mkdir(exist_ok=True)
    (audits / "frozen_audit.json").write_text(json.dumps({
        "sample_size": len(audit), "selection": "fixed sha256 order outside the pilot",
        "outcomes": audit_outcomes, "population_accuracy_claim": None,
    }, indent=2) + "\n", encoding="utf-8")

    result = {
        "manifest_count": len(manifest), "card_count": len(cards), "year_counts": dict(sorted(year_actual.items())),
        "state_counts": {f"{year}:{state}": count for (year, state), count in sorted(state_counts.items())},
        "source_counts": dict(source_counts), "pilot_size": len(pilot), "audit_size": len(audit),
        "copy_similarity": {"claims_checked": len(copy_ratios), "max": max(copy_ratios) if copy_ratios else 0.0, "over_0_8": sum(value > 0.8 for value in copy_ratios)},
        "errors": errors,
    }
    (out_dir / "verification.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
