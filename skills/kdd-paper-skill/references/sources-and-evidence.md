# Sources and evidence

Use the local research artifacts when this repository is present:

- `research/corpus/manifest.jsonl` for PaperWarehouse identity and the frozen
  source revision;
- `research/abstract_distillation/cards/` for abstract-linked retrieval cards
  and source locators;
- `research/synthesis/practices.md` for current source-linked guidance;
- `research/exemplars/full_text_checks.md` for inspected full-text locators;
- `research/exemplars/official_awards.json` for official recognition metadata.

The current cards are produced by `bounded_rule_extractor_v1`. Their source IDs
establish traceability, not semantic fidelity. Inspect the underlying abstract
before using a card as semantic evidence. A full-text claim requires the
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
