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

Cards use `reading_level: abstract_only`. They paraphrase a verified abstract,
number its source sentences as `S1`, `S2`, and so on, and attach source IDs to
every substantive extracted field. Cards do not claim to verify experiments,
proofs, figures, reproducibility, or full-paper limitations.

Full-text evidence is added only for a bounded exemplar or comparison. The
card or exemplar records the section, table, figure, or appendix locator.
Public artifacts do not store bulk abstract text.

The source order is official KDD or ACM metadata, authoritative publisher or
author metadata, verified arXiv metadata for the same work, then another
reliable scholarly metadata source when necessary. The selected locator and
source are recorded per card. PaperWarehouse discovery synopses are not
semantic evidence for extraction.

## Card contract

Each completed card contains:

- PaperWarehouse identity, venue, year, and track;
- `reading_level: abstract_only`, abstract source, locator, and retrieval date;
- problem and stated gap when the abstract supports them;
- zero to three contribution entries with source IDs;
- stated novelty only when explicitly stated by the authors;
- zero to three author-reported findings or comparisons with conditions;
- a two to five beat narrative sequence in abstract order;
- zero to two candidate lessons, each split into observation, interpretation,
  application, and exception;
- material unknowns.

Null and empty arrays are valid. An abstract does not become a venue rule,
independent scientific verification, or an acceptance explanation.

## Run sequence

1. Freeze the PaperWarehouse revision and manifest.
2. Retrieve one abstract per paper with a strong identifier and retain raw
   responses only under an ignored cache.
3. Run a 30–40 paper stratified pilot across years, tracks, contribution
   types, award status, and abstract density.
4. Review the pilot against the numbered source units and correct the card
   contract once if needed.
5. Extract the remaining available abstracts in bounded resumable batches.
6. Synthesize cards in groups of at most 50, grouped by track and contribution
   type. Record supporting IDs, counterexamples, use, and exceptions.
7. Freeze a stratified random audit outside the pilot, then source-check every
   final exemplar and any card that materially drives a practice.
8. Build the user-facing skill from checked practices, not from the prior
   Oral-paper practice list.

Failed validation, missing source, and completed cards remain distinguishable.
Do not invent cards for unavailable abstracts.

## Official guidance and awards

Official KDD CFP guidance is stored separately from observed paper patterns.
The [KDD 2025 Research Track CFP](https://kdd2025.kdd.org/research-track-call-for-papers/)
and [KDD 2026 Research Track CFP](https://kdd2026.kdd.org/research-track-call-for-papers/)
mention technical merit,
originality, potential impact, quality of execution and presentation, related
work, reproducibility, and ethics, and state that the first eight content pages
should be self-contained. These are venue-stated considerations, not a score,
weighting, gate, or acceptance model.

The exemplar manifest records only official award categories and their linked
PaperWarehouse identities. An award label means official recognition in that
category. It is not a quality score or a template.

## Output boundary

Mode A compares a user's artifact with a small relevant source set and gives
at most three concrete improvements. Mode B teaches one bounded practice and
ends with one focused reflection exercise. Both modes keep source observation,
interpretation, recommendation, and uncertainty distinct.
