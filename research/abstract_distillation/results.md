# Abstract retrieval and semantic distillation results

PaperWarehouse source revision: `118a82ce657a2bf6915afdc82921553dc765740a`. The identity manifest contains all 3,696 SIGKDD records for 2022–2026. This downstream run did not change PaperWarehouse.

## Retrieval-card coverage

| Year | Catalog records | Completed retrieval cards | Missing reliable abstract |
| --- | ---: | ---: | ---: |
| 2026 | 1,408 | 1,109 | 299 |
| 2025 | 771 | 694 | 77 |
| 2024 | 562 | 561 | 1 |
| 2023 | 496 | 490 | 6 |
| 2022 | 459 | 395 | 64 |
| Total | 3,696 | 3,249 | 447 |

All 3,249 completed retrieval cards use OpenAlex abstract metadata and retain an OpenAlex work locator. No retrieval card uses an arXiv fallback. PaperWarehouse discovery synopses were not used as semantic source text.

The retrieval cards were produced by `bounded_rule_extractor_v1`. Their lexical cues help locate candidates; they are not paper-level semantic evidence.

## Research Track semantic-card coverage

| Year | Research Track identities | OpenAlex abstract | Other verified abstract | Semantic cards | No reliable abstract |
| --- | ---: | ---: | ---: | ---: | ---: |
| 2026 | 785 | 634 | 0 | 634 | 151 |
| 2025 | 552 | 493 | 3 | 496 | 56 |
| 2024 | 411 | 410 | 1 | 411 | 0 |
| 2023 | 313 | 308 | 1 | 309 | 4 |
| 2022 | 253 | 253 | 0 | 253 | 0 |
| Total | 2,314 | 2,098 | 5 | 2,103 | 211 |

Each semantic card was extracted from one verified abstract context and remains `reading_level: abstract_only`. Five fallbacks use three arXiv abstracts, one author-hosted proceedings PDF, and one author publication-page abstract. Each card retains its source locator. Missing abstracts have no semantic card.

## Pilot and synthesis

The 40-paper Research Track pilot covers eight papers per year. Its cards received 38 PASS, 2 MINOR, and 0 MATERIAL judgments. The minor cases are documented in [the pilot results](../semantic_pilot/results.md). This pilot does not establish semantic accuracy across the scaled corpus.

The current synthesis contains three bounded practices drawn from scaled Research Track semantic cards and five full-text synthesis checks. The five checks use public author copies and retain section, table, figure, or appendix locators in [the exemplar record](../exemplars/full_text_checks.md). Three additional full-text sources support a fresh-context behavior check and are separate from the synthesis examples.

Twenty-five official 2022–2025 award entries resolve to PaperWarehouse IDs. The 2022 ADS award page uses `EasyFGL`; ACM/Crossref proceedings metadata identifies the same work as `FederatedScope-GNN`, so the manifest records the published PaperWarehouse identity.

No KDD OpenReview review or meta-review is part of the current evidence set.

## Verification and limits

The retrieval-card structural checks cover identity, source locator, and source-unit references. Their run-time copy-similarity check inspected 34,764 generated claims and found no ratio above 0.8. These checks do not establish semantic fidelity.

The semantic pilot was compared claim-by-claim with its supplied abstract units. For the scaled cards, a bounded copy check covered 33,520 claims and 52,004 claim/cited-unit pairs reconstructable from the current OpenAlex cache; it found no exact sentence copies or near-verbatim pairs (at least 12 shared tokens covering at least 80% of both claim and source). Ninety-five claim references could not be aligned to the current cache's sentence segmentation. The five non-OpenAlex cards were checked against their linked abstracts; their 124 claim/cited-unit pairs had no exact or near-verbatim copy. Structural validation checks schema, identity, source locators, and source-unit references. Neither structural validation nor copy screening estimates semantic accuracy across the Research Track corpus.

Abstract-derived cards do not establish full-text experimental adequacy, proof correctness, reproducibility, or limitations omitted from the abstract. The 211 Research Track records without a reliable abstract remain unresolved for semantic extraction.
