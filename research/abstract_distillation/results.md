# Abstract distillation run results

Run date: 2026-09-21.

PaperWarehouse source revision: `118a82ce657a2bf6915afdc82921553dc765740a`.
The identity manifest contains all 3,696 SIGKDD records for 2022–2026. The
downstream run did not change PaperWarehouse.

## Coverage

| Year | Catalog records | Completed abstract cards | Missing reliable abstract |
| --- | ---: | ---: | ---: |
| 2026 | 1,408 | 1,109 | 299 |
| 2025 | 771 | 694 | 77 |
| 2024 | 562 | 561 | 1 |
| 2023 | 496 | 490 | 6 |
| 2022 | 459 | 395 | 64 |
| Total | 3,696 | 3,249 | 447 |

All completed cards use `openalex_abstract_metadata` and retain an OpenAlex
work locator. Exact-title arXiv fallback queries were attempted for records
without a usable OpenAlex abstract; they did not produce an additional card in
this run. The warehouse's discovery synopses were not used as semantic source
text. Placeholder metadata such as `International audience` and `No
description supplied` remains missing.

## Pilot and audit

The pilot contains 36 completed cards selected across years and tracks. The
pilot review froze these schema decisions:

- `stated_novelty` is null unless the abstract explicitly states a distinction;
- candidate lessons may be empty when the abstract does not support a bounded
  transferable observation;
- claims use compact source-grounded paraphrases and sentence IDs rather than
  copied abstract text.

A fixed 60-card audit was selected by SHA-256 order outside the pilot. All 60
passed structural source checks. These pilot and audit counts are extraction
quality evidence for the inspected samples, not a corpus-wide accuracy
estimate. See `pilot_review.json`, `audits/frozen_audit.json`, and
`verification.json`.

## Synthesis

The primary synthesis surface is Research Track. Four cross-track or
track-specific practices were retained: state the changed object and tension;
keep measured conditions beside conclusions; choose comparisons that answer the
claim; and treat systems and resources as bounded contributions. Official KDD
2025 and 2026 Research Track CFP guidance is recorded separately and is not a
score or acceptance model.

Twenty-five official 2022–2025 award entries were resolved to PaperWarehouse
IDs. The 2022 ADS award page uses `EasyFGL`; ACM/Crossref proceedings metadata
identifies the same work as `FederatedScope-GNN`, so the manifest records the
published PaperWarehouse identity.

Five bounded full-text checks used public arXiv copies. They cover CAT,
Evidential Alignment, H2GB, Evaluating Decision Rules Across Many Weak
Experiments, and Greykite. Their section, table, figure, and appendix locators
are in `research/exemplars/full_text_checks.md`.

No KDD OpenReview review or meta-review was used. The final skill does not
depend on review availability.

## Limits

The rule-based extractor preserves source locators and compact terms but is not
a human scientific review. The 447 missing-source records have no card and are
not represented as evidence. Abstract cards do not establish full-text
experimental adequacy, proof correctness, reproducibility, or award causes.
