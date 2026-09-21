# Separate neutral warehouse evidence from KDD-derived study

## Context / Trigger

PaperWarehouse is a reusable neutral corpus across downstream research projects.
KDD Paper Skill derives venue-specific practices, selects examples, and turns
inspected evidence into manuscript guidance. Combining those responsibilities
would make project-specific interpretation part of canonical paper semantics.

## Decision

PaperWarehouse owns scholarly identity, bibliographic provenance, and neutral
paper memory. KDD Paper Skill owns KDD-specific retrieval cards, synthesis,
official-recognition context, exemplar selection, and manuscript guidance.

KDD Paper Skill references upstream work by stable `paper_id` and records the
exact PaperWarehouse revision used by a run. Derived KDD judgments do not flow
back into canonical PaperWarehouse records.

## Rejected alternatives

Store KDD-specific practices and exemplar judgments directly in PaperWarehouse.
That would couple a general evidence corpus to one submission target.

Duplicate full PaperWarehouse records here. That would create competing
scholarly-identity sources and make later corrections ambiguous.

## Consequences / invariants

- PaperWarehouse remains the authority for canonical paper identity.
- This repository keeps study-specific evidence and interpretation.
- Downstream artifacts cite `paper_id` plus the upstream revision used.
- KDD-specific practices, award interpretation, and manuscript recommendations
  are not written back as canonical paper semantics.
- Bibliographic corrections belong in PaperWarehouse.
