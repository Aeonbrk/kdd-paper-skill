#!/usr/bin/env python3
"""Retrieve verified abstracts and write one compact evidence card per paper.

This is a bounded KDD run utility, not a general scholarly ingestion service.
Raw abstract responses are written only below the ignored research/.cache path.
"""

from __future__ import annotations

import argparse
import ast
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from difflib import SequenceMatcher
from pathlib import Path


PAPERWAREHOUSE = Path("/Users/oian/Documents/PaperWarehouse")
ROOT = Path(__file__).resolve().parents[2]
CACHE = ROOT / "research" / ".cache"
CARDS = ROOT / "research" / "abstract_distillation" / "cards"
TODAY = "2026-09-21"


def parse_scalar(value: str):
    value = value.strip()
    if value in {"null", "~"}:
        return None
    try:
        return ast.literal_eval(value)
    except (ValueError, SyntaxError):
        return value.strip('"')


def read_record(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError(f"missing front matter: {path}")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError(f"unterminated front matter: {path}")
    fields = {}
    for line in text[4:end].splitlines():
        if not line or line.startswith("  ") or line.startswith("-"):
            continue
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = parse_scalar(value)
    return {
        "paper_id": fields["paper_id"],
        "title": fields["title"],
        "year": int(fields["publication_year"]),
        "track": fields.get("track"),
        "doi": fields.get("doi"),
        "official_paper_url": fields.get("official_paper_url"),
    }


def load_records() -> list[dict]:
    paths = sorted((PAPERWAREHOUSE / "library" / "papers").glob("sigkdd-*.md"))
    records = [read_record(path) for path in paths]
    records.sort(key=lambda r: (-r["year"], r["paper_id"]))
    return records


def norm(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def title_match(a: str, b: str) -> float:
    return SequenceMatcher(None, norm(a), norm(b)).ratio()


def request_json(url: str, payload: bytes | None = None, retries: int = 5):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(
                url,
                data=payload,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "KDDPaperSkill/0.1 (abstract evidence run)",
                },
            )
            with urllib.request.urlopen(req, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt == retries - 1:
                raise
            time.sleep(min(2 ** attempt, 12))
        except (urllib.error.URLError, TimeoutError):
            if attempt == retries - 1:
                raise
            time.sleep(min(2 ** attempt, 12))
    raise RuntimeError("unreachable")


def reconstruct_abstract(index: dict | None) -> str | None:
    if not index:
        return None
    tokens = []
    for word, positions in index.items():
        for pos in positions:
            tokens.append((pos, word))
    tokens.sort()
    text = " ".join(word for _, word in tokens)
    return re.sub(r"\s+([,.;:!?])", r"\1", text).strip()


def openalex_records(records: list[dict]) -> dict[str, dict]:
    key = os.environ.get("OPENALEX_API_KEY")
    if not key:
        raise SystemExit("OPENALEX_API_KEY is required for the bounded retrieval run")
    CACHE.mkdir(parents=True, exist_ok=True)
    cache_path = CACHE / "openalex_records.json"
    cached = {}
    if cache_path.exists():
        cached = json.loads(cache_path.read_text(encoding="utf-8"))
        # The first pilot cache used only the ACM suffix. Normalize it in
        # memory so the record DOI remains the stable lookup key.
        cached = {
            (key if key.startswith("10.") else "10.1145/" + key): value
            for key, value in cached.items()
        }
    missing = [r for r in records if r.get("doi") and r["doi"].lower() not in cached]
    for start in range(0, len(missing), 50):
        batch = missing[start : start + 50]
        doi_filter = "|".join(r["doi"].lower() for r in batch)
        params = urllib.parse.urlencode(
            {
                "filter": "doi:" + doi_filter,
                "per-page": 200,
                "api_key": key,
            },
            safe="|",
        )
        url = "https://api.openalex.org/works?" + params
        data = request_json(url)
        for item in data.get("results", []):
            doi = (item.get("doi") or "").replace("https://doi.org/", "").lower()
            if doi:
                cached[doi] = item
        cache_path.write_text(json.dumps(cached), encoding="utf-8")
        if start + 50 < len(missing):
            time.sleep(0.25)
    return cached


def arxiv_id_from_record(record: dict) -> str | None:
    text = (PAPERWAREHOUSE / "library" / "papers" / f"{record['paper_id']}.md").read_text(encoding="utf-8")
    match = re.search(r"^arxiv_id:\s*['\"]?([^'\"\n]+)", text, flags=re.MULTILINE)
    if match and match.group(1) not in {"null", "None"}:
        return match.group(1)
    return None


def arxiv_id_from_item(item: dict | None) -> str | None:
    if not item:
        return None
    for location in item.get("locations", []):
        for field in ("landing_page_url", "pdf_url"):
            url = location.get(field) or ""
            match = re.search(r"arxiv\.org/(?:abs|pdf)/([^/?#]+)", url)
            if match:
                return match.group(1).removesuffix(".pdf")
    return None


def parse_arxiv_xml(data: bytes) -> dict[str, tuple[str, str, str]]:
    ns = {"a": "http://www.w3.org/2005/Atom"}
    result = {}
    try:
        root = ET.fromstring(data)
    except ET.ParseError:
        return result
    for entry in root.findall("a:entry", ns):
        entry_id = entry.findtext("a:id", default="", namespaces=ns)
        match = re.search(r"arxiv\.org/abs/([^/?#]+)", entry_id)
        if not match:
            continue
        arxiv_id = match.group(1)
        title = " ".join(entry.findtext("a:title", default="", namespaces=ns).split())
        abstract = " ".join(entry.findtext("a:summary", default="", namespaces=ns).split())
        if abstract:
            result[arxiv_id] = (title, abstract, f"https://arxiv.org/abs/{arxiv_id}")
    return result


def arxiv_abstract(record: dict, item: dict | None = None) -> tuple[str, str] | None:
    arxiv_id = arxiv_id_from_record(record) or arxiv_id_from_item(item)
    if not arxiv_id:
        return None
    query = urllib.parse.urlencode({"id_list": arxiv_id, "max_results": 1})
    url = "https://export.arxiv.org/api/query?" + query
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "KDDPaperSkill/0.1"})
        with urllib.request.urlopen(req, timeout=60) as response:
            found = parse_arxiv_xml(response.read()).get(arxiv_id)
    except Exception:
        return None
    if not found:
        return None
    title, abstract, locator = found
    if not abstract:
        return None
    if title_match(title, record["title"]) < 0.90:
        return None
    return abstract, locator


def arxiv_batch(records: list[dict], openalex: dict[str, dict]) -> dict[str, tuple[str, str]]:
    candidates = {}
    for record in records:
        item = openalex.get((record.get("doi") or "").lower())
        arxiv_id = arxiv_id_from_record(record) or arxiv_id_from_item(item)
        if arxiv_id:
            candidates[record["paper_id"]] = arxiv_id
    found_by_id = {}
    ids = sorted(set(candidates.values()))
    for start in range(0, len(ids), 20):
        query = urllib.parse.urlencode({"id_list": ",".join(ids[start : start + 20]), "max_results": 100})
        url = "https://export.arxiv.org/api/query?" + query
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "KDDPaperSkill/0.1"})
            with urllib.request.urlopen(req, timeout=60) as response:
                found_by_id.update(parse_arxiv_xml(response.read()))
        except Exception:
            continue
        time.sleep(0.2)
    result = {}
    for record in records:
        arxiv_id = candidates.get(record["paper_id"])
        found = found_by_id.get(arxiv_id) if arxiv_id else None
        if found and title_match(found[0], record["title"]) >= 0.90:
            result[record["paper_id"]] = (found[1], found[2])
    return result


def arxiv_title_search(record: dict) -> tuple[str, str] | None:
    query = urllib.parse.urlencode({"search_query": 'ti:"' + record["title"] + '"', "max_results": 3})
    url = "https://export.arxiv.org/api/query?" + query
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "KDDPaperSkill/0.1"})
        with urllib.request.urlopen(req, timeout=60) as response:
            found = parse_arxiv_xml(response.read())
    except Exception:
        return None
    time.sleep(0.2)
    for title, abstract, locator in found.values():
        if title_match(title, record["title"]) >= 0.94:
            return abstract, locator
    return None
    if title_match(title, record["title"]) < 0.90 or not abstract:
        return None
    return abstract, f"https://arxiv.org/abs/{arxiv_id}"


def sentences(abstract: str) -> list[str]:
    abstract = re.sub(r"\s+", " ", abstract).strip()
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", abstract)
    parts = [p.strip() for p in parts if p.strip()]
    return parts[:20]


def reliable_abstract(abstract: str | None) -> bool:
    if not abstract or len(abstract.strip()) < 80:
        return False
    placeholder = abstract.strip().lower().rstrip(".")
    return placeholder not in {"international audience", "no description supplied", "no abstract available"}


def paraphrase(sentence: str, role: str) -> str:
    """Compress source-specific terms into a short paraphrase.

    The card keeps source IDs, not source sentences. A keyword compression
    avoids copying an abstract while retaining names, metrics, datasets, and
    the central operation needed for later retrieval.
    """
    stop = {
        "a", "an", "and", "are", "as", "at", "be", "by", "for", "from",
        "in", "into", "is", "it", "its", "of", "on", "or", "that", "the",
        "their", "this", "to", "using", "we", "with", "our", "can", "may",
        "more", "than", "which", "where", "while", "these", "such", "also",
    }
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9+./-]*|\d+(?:\.\d+)?%?", sentence)
    terms = []
    for token in tokens:
        if token.lower() in stop or len(token) == 1:
            continue
        if token.lower() not in {term.lower() for term in terms}:
            terms.append(token)
        if len(terms) == 18:
            break
    phrase = " ".join(terms) or "the reported task"
    if role == "evidence":
        return f"The authors report evidence involving {phrase}."
    if role == "contribution":
        return f"Describes a contribution involving {phrase}."
    if role == "gap":
        return f"Frames a limitation involving {phrase}."
    return f"Examines {phrase}."


def classify(sentence: str) -> set[str]:
    low = sentence.lower()
    labels = set()
    if re.search(r"\bhowever\b|\balthough\b|\bbut\b|\black of\b|\bremain", low):
        labels.add("gap")
    if re.search(r"\bwe\b|\bintroduc|\bpropos|\bdevelop|\bpresent|\bdesign|\bframework|\bmethod\b|\bmodel\b|\balgorithm\b|\bbenchmark\b|\bdataset\b", low):
        labels.add("contribution")
    if re.search(r"\bexperiment|\bevaluat|\bresult|\boutperform|\bachiev|\bdemonstrat|\bimprov|\bcomparison|\btheorem|\bproof|\baccuracy|\bf1\b|\bauc\b|\brecall\b|\bprecision\b", low):
        labels.add("evidence")
    return labels


def card_for(record: dict, abstract: str, source: str, locator: str) -> dict:
    units = sentences(abstract)
    unit_ids = [f"S{i}" for i in range(1, len(units) + 1)]
    classes = [classify(s) for s in units]
    gap_ids = [unit_ids[i] for i, labels in enumerate(classes) if "gap" in labels]
    contribution_ids = [unit_ids[i] for i, labels in enumerate(classes) if "contribution" in labels]
    evidence_ids = [unit_ids[i] for i, labels in enumerate(classes) if "evidence" in labels]
    problem_ids = [unit_ids[0]] if units else []
    if gap_ids:
        problem_ids = problem_ids + gap_ids[:1]

    contribution_entries = []
    for i, labels in enumerate(classes):
        if "contribution" not in labels:
            continue
        sentence = units[i]
        low = sentence.lower()
        if "dataset" in low or "benchmark" in low or "resource" in low:
            kind = "resource"
        elif "theorem" in low or "proof" in low or "bound" in low:
            kind = "theory"
        elif "system" in low or "platform" in low or "deployment" in low:
            kind = "system"
        elif "framework" in low or "method" in low or "algorithm" in low or "model" in low:
            kind = "method"
        else:
            kind = "contribution"
        contribution_entries.append({"type": kind, "claim": paraphrase(sentence, "contribution"), "source_ids": [unit_ids[i]]})
        if len(contribution_entries) == 3:
            break

    evidence_entries = []
    for i, labels in enumerate(classes):
        if "evidence" not in labels:
            continue
        evidence_entries.append({"claim": paraphrase(units[i], "evidence"), "source_ids": [unit_ids[i]]})
        if len(evidence_entries) == 3:
            break

    narrative = []
    if units:
        narrative.append({"role": "context", "summary": paraphrase(units[0], "context"), "source_ids": ["S1"]})
    if gap_ids:
        idx = unit_ids.index(gap_ids[0])
        narrative.append({"role": "gap", "summary": paraphrase(units[idx], "gap"), "source_ids": [gap_ids[0]]})
    for entry in contribution_entries[:2]:
        narrative.append({"role": "contribution", "summary": entry["claim"], "source_ids": entry["source_ids"]})
    for entry in evidence_entries[:1]:
        narrative.append({"role": "reported evidence", "summary": entry["claim"], "source_ids": entry["source_ids"]})
    narrative = narrative[:5]

    unknowns = []
    if not evidence_entries:
        unknowns.append("The abstract does not report a concrete evaluation or theoretical result.")
    if not gap_ids:
        unknowns.append("The abstract does not state a distinct limitation of prior work.")

    return {
        "paper_id": record["paper_id"],
        "venue": "SIGKDD",
        "year": record["year"],
        "track": record["track"],
        "title": record["title"],
        "doi": record["doi"],
        "reading_level": "abstract_only",
        "abstract_source": source,
        "source_locator": locator,
        "retrieved_on": TODAY,
        "source_units": [{"id": unit_id, "kind": "sentence"} for unit_id in unit_ids],
        "problem_and_gap": {
            "problem": {"claim": paraphrase(units[0], "problem"), "source_ids": problem_ids[:2]} if units else None,
            "gap": {"claim": paraphrase(units[unit_ids.index(gap_ids[0])], "gap"), "source_ids": [gap_ids[0]]} if gap_ids else None,
        },
        "contributions": contribution_entries,
        "stated_novelty": None,
        "author_reported_evidence": evidence_entries,
        "narrative_sequence": narrative,
        "candidate_lessons": [],
        "unknowns": unknowns,
        "validation_state": "completed",
        "extraction_method": "bounded_rule_extractor_v1",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--year", type=int, action="append")
    parser.add_argument("--skip-title-fallback", action="store_true")
    parser.add_argument("--cards-dir", type=Path, default=CARDS)
    args = parser.parse_args()
    records = load_records()
    if args.year:
        records = [r for r in records if r["year"] in args.year]
    if args.limit:
        records = records[: args.limit]
    openalex = openalex_records(records)
    arxiv_found = arxiv_batch(records, openalex)
    args.cards_dir.mkdir(parents=True, exist_ok=True)
    stats = {"completed": 0, "missing_source": 0, "failed_validation": 0, "by_year": {}}
    for record in records:
        doi_key = (record.get("doi") or "").lower()
        item = openalex.get(doi_key)
        abstract = reconstruct_abstract(item.get("abstract_inverted_index") if item else None)
        source = "openalex_abstract_metadata"
        locator = item.get("id") if item else None
        if not reliable_abstract(abstract):
            abstract = None
        if abstract and item and title_match(record["title"], item.get("title", "")) < 0.82:
            abstract = None
        if not abstract:
            fallback = arxiv_found.get(record["paper_id"])
            if not fallback and not args.skip_title_fallback:
                fallback = arxiv_title_search(record)
            if fallback:
                abstract, locator = fallback
                source = "arxiv_abstract"
        if abstract and locator:
            card = card_for(record, abstract, source, locator)
            stats["completed"] += 1
        else:
            card = {
                "paper_id": record["paper_id"], "venue": "SIGKDD", "year": record["year"],
                "track": record["track"], "title": record["title"], "doi": record["doi"],
                "reading_level": "abstract_only", "abstract_source": None,
                "source_locator": None, "retrieved_on": TODAY, "source_units": [],
                "problem_and_gap": {"problem": None, "gap": None}, "contributions": [],
                "stated_novelty": None, "author_reported_evidence": [],
                "narrative_sequence": [], "candidate_lessons": [],
                "unknowns": ["No reliable abstract source was available during this run."],
                "validation_state": "missing_source", "extraction_method": "bounded_rule_extractor_v1",
            }
            stats["missing_source"] += 1
        stats["by_year"].setdefault(str(record["year"]), {"completed": 0, "missing_source": 0})
        stats["by_year"][str(record["year"])][card["validation_state"]] += 1
        (args.cards_dir / f"{record['paper_id']}.json").write_text(json.dumps(card, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (ROOT / "research" / "abstract_distillation" / "run_stats.json").write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(stats, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
