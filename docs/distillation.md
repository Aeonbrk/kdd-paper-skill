# KDD distillation contract

## Scope

The corpus is every archival SIGKDD paper represented by PaperWarehouse for
2022–2026. The five yearly counts are 459, 496, 562, 771, and 1,408. A paper
is identified by the PaperWarehouse `paper_id`; downstream cards do not create
or merge scholarly identities.

Research Track is the primary synthesis surface. Applied Data Science,
Datasets and Benchmarks, AI for Sciences, Blue Sky Ideas, Health Day, and any
other archival tracks remain separate evidence surfaces when their paper types
or evaluation questions differ.

## Evidence levels

Cards use `reading_level: abstract_only`. The current corpus cards are produced
by `bounded_rule_extractor_v1` from verified abstract metadata. They preserve
paper identity, source locators, sentence-unit IDs, and compact retrieval cues.
They are not semantic source review and do not establish corpus-wide prevalence,
experimental adequacy, proof correctness, reproducibility, or full-paper
limitations.

A source-dependent recommendation must return to the actual abstract at the
recorded locator or to inspected full text. Full-text evidence records the
section, table, figure, or appendix locator. Public artifacts do not store bulk
abstract text.

The source order is official KDD or ACM metadata, authoritative publisher or
author metadata, verified arXiv metadata for the same work, then another
reliable scholarly metadata source when necessary. PaperWarehouse discovery
synopses are not semantic evidence for extraction.

## Card contract

Each completed card contains:

- PaperWarehouse identity, venue, year, and track;
- `reading_level: abstract_only`, abstract source, locator, and retrieval date;
- compact problem, contribution, and reported-evidence cues when the bounded
  extractor detects them;
- source-unit IDs for every generated cue;
- explicit unknowns;
- a validation state.

Null and empty arrays are valid. A card does not become a venue rule,
independent scientific verification, or an acceptance explanation.

## Run sequence

1. Freeze the PaperWarehouse revision and manifest.
2. Retrieve one abstract per paper with a strong identifier and retain raw
   responses only under an ignored cache.
3. Produce one bounded retrieval card per available abstract and keep
   missing-source records explicit.
4. Verify corpus identity, source locators, source-unit references, and
   accidental large verbatim reuse.
5. Use cards to locate candidate comparisons, then inspect the underlying
   abstract or full text before making an attributed semantic claim.
6. Keep synthesis track-aware and bounded.
7. Use full text when a recommendation depends on experimental, methodological,
   proof, figure, table, or reproducibility detail.

Failed validation, missing source, and completed cards remain distinguishable.
Do not invent cards for unavailable abstracts.

## Verification boundary

Automated verification establishes structural properties of the run. It can
detect missing identities, invalid source-unit references, absent locators, and
large verbatim overlap. It does not determine whether a paraphrased claim is
semantically faithful to the source sentence.

A semantic source audit requires comparing card claims with the underlying
abstract units. Until such an audit is performed, structural checks are not
semantic extraction accuracy.

## Official guidance and awards

Official KDD CFP guidance is stored separately from observed paper evidence.
The [KDD 2025 Research Track CFP](https://kdd2025.kdd.org/research-track-call-for-papers/)
and [KDD 2026 Research Track CFP](https://kdd2026.kdd.org/research-track-call-for-papers/)
mention technical merit, originality, potential impact, quality of execution
and presentation, related work, reproducibility, and ethics, and state that the
first eight content pages should be self-contained. These are venue-stated
considerations, not a score, weighting, gate, or acceptance model.

The exemplar manifest records only official award categories and linked
PaperWarehouse identities. An award label means official recognition in that
category. It is not a quality score or a template.

## Output boundary

Mode A compares a user's artifact with a small relevant source set and gives at
most three concrete improvements. Mode B teaches one bounded practice with
source-linked evidence and a focused reflection exercise. Both modes keep source
observation, interpretation, recommendation, and uncertainty distinct.
