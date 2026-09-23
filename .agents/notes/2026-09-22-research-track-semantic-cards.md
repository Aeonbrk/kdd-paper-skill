# Research Track semantic cards

## Context / Trigger

The KDD retrieval cards located comparable papers but did not provide validated
paper-level semantic fields. A 40-paper Research Track pilot tested one-paper
abstract extraction contexts across 2022–2026 before scaling.

## Decision

Keep rule-extracted cards as retrieval aids for the complete KDD corpus. Add
source-grounded semantic cards for Research Track papers with reliable
abstracts. Semantic cards remain `reading_level: abstract_only`, preserve the
PaperWarehouse identity, cite supplied abstract-unit IDs, and keep
author-reported evidence separate from full-text findings. Other tracks remain
available through retrieval cards and source-on-demand inspection.

## Rejected Alternatives

- Treat rule-extracted retrieval cards as semantic evidence: rejected because
  their lexical cues were not validated as faithful paper-level meaning.

- Scale semantic extraction across every KDD track: rejected because the
  validated use case is Research Track comparison and other contribution types
  require separate evidence questions.

- Use full-text extraction during catalog retrieval: rejected because the
  semantic pilot is abstract-only and full-text evidence remains a separate
  bounded task.

## Consequences / Invariants

- Retrieval and semantic cards have distinct responsibilities and paths.
- A semantic claim must cite source-unit IDs from the supplied abstract.
- Missing abstracts remain missing; no card is fabricated from a title or
  snippet.
- Semantic cards do not change PaperWarehouse identity or corpus membership.
- Full-text claims require the existing section, table, figure, or appendix
  locator discipline.
