# Abstract distillation run results

Run date: 2026-09-21.

PaperWarehouse source revision: `118a82ce657a2bf6915afdc82921553dc765740a`.
The identity manifest contains all 3,696 SIGKDD records for 2022–2026. The
downstream run did not change PaperWarehouse.

## Coverage

| Year | Catalog records | Completed retrieval cards | Missing reliable abstract |
| --- | ---: | ---: | ---: |
| 2026 | 1,408 | 1,109 | 299 |
| 2025 | 771 | 694 | 77 |
| 2024 | 562 | 561 | 1 |
| 2023 | 496 | 490 | 6 |
| 2022 | 459 | 395 | 64 |
| Total | 3,696 | 3,249 | 447 |

All completed cards use `openalex_abstract_metadata` and retain an OpenAlex
work locator. No completed card uses the arXiv fallback in this run. PaperWarehouse discovery
synopses were not used as semantic source text.

## Verification

All 3,249 completed cards passed the automated structural checks for identity,
source locator presence, and source-unit reference validity. The run-time
copy-similarity check inspected 34,764 generated claims and found no ratio above
0.8.

These checks establish corpus and source-linkage structure. They do not
establish semantic fidelity of the generated cues. A semantic source audit has
not been performed, and no corpus-wide semantic accuracy estimate is claimed.

## Synthesis

The 3,249 cards were produced by `bounded_rule_extractor_v1`. They are used to
locate candidate comparisons, not as measured prevalence evidence. The current
practice set relies on source-linked examples and five bounded full-text checks
for claims that depend on experimental or methodological detail.

Twenty-five official 2022–2025 award entries were resolved to PaperWarehouse
IDs. The 2022 ADS award page uses `EasyFGL`; ACM/Crossref proceedings metadata
identifies the same work as `FederatedScope-GNN`, so the manifest records the
published PaperWarehouse identity.

Five bounded full-text checks use public arXiv copies: CAT, Evidential
Alignment, H2GB, Evaluating Decision Rules Across Many Weak Experiments, and
Greykite. Their section, table, figure, and appendix locators are in
`research/exemplars/full_text_checks.md`.

No KDD OpenReview review or meta-review is part of the current evidence set.

## Limits

The rule extractor is not semantic source review. The 447 missing-source records
have no semantic card. Abstract-linked cards do not establish full-text
experimental adequacy, proof correctness, reproducibility, or award causes.
