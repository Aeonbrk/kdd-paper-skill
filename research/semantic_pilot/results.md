# Semantic extraction pilot

## Pilot contract

- 40 Research Track papers, eight from each year (2022–2026).
- Each one-paper context contains a PaperWarehouse identity and numbered units reconstructed from the retrieved OpenAlex abstract metadata.
- Cards preserve identity fields, cite source-unit IDs, separate author-reported evidence from verification, and leave unsupported fields null or empty.
- The extraction contract preserves every identity field exactly and records source units by ID only.

## Fidelity review

Every card was compared with its supplied abstract units. The pilot cards contain 38 PASS, 2 MINOR, and 0 MATERIAL cases.

The two MINOR cases are a code-availability statement placed under contributions (GPPT) and a sparse abstract's task statement placed in the gap field (ELEGANT). No card invented a novelty claim, converted a proposal into independent evidence, or changed a reported condition or comparison direction. Optional lesson objects without source-grounded claims were omitted.

## Decision

Cold-start retrieval and semantic extraction passed the pilot. Research Track-only semantic scaling proceeded. Other KDD tracks remain on the retrieval-card and source-on-demand path.

## Source and storage

Pilot source locators and selection strata are in [manifest.jsonl](manifest.jsonl). Semantic cards use `reading_level: abstract_only`, `abstract_source: OpenAlex abstract metadata`, and `extraction_method: semantic_model_pilot_v1`. No raw abstract text is stored in the repository.
