# Sources and evidence

Use the local research artifacts when this repository is present:

- `research/corpus/manifest.jsonl` for PaperWarehouse identity and the frozen
  source revision;
- `research/abstract_distillation/cards/` for abstract-linked retrieval cards
  and source locators;
- `research/semantic_cards/research_track/` for source-grounded semantic cards
  derived from available Research Track abstracts;
- `research/synthesis/practices.md` for current source-linked guidance;
- `research/exemplars/full_text_checks.md` for inspected full-text locators;
- `research/exemplars/official_awards.json` for official recognition metadata.

Retrieval cards are produced by `bounded_rule_extractor_v1`; their source IDs
establish traceability, not semantic fidelity. Research Track semantic cards
are produced one paper per context by `semantic_model_pilot_v1` and remain
abstract-only evidence. Inspect the underlying abstract before using either
card surface as an attributed comparison. A full-text claim requires the
recorded section, figure, table, or appendix locator.

Keep these levels separate:

1. `abstract`: an inspected abstract supports framing, stated contribution,
   and author-reported evidence;
2. `full-text section` or `figure/table`: experimental, methodological, or
   proof detail at the cited locator;
3. `review/meta-review`: reviewer opinion, not scientific fact;
4. `official venue guidance` or `award`: venue context or official
   recognition, not evidence that a design caused a decision.

If the relevant source cannot be inspected, give general research guidance
without inventing a citation, review, result, or KDD requirement.
