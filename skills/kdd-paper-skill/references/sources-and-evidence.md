# Sources and evidence

Use the local research artifacts when this repository is present:

- `research/corpus/manifest.jsonl` for PaperWarehouse identity and the frozen
  source revision;
- `research/abstract_distillation/cards/` for abstract-only cards and source
  locators;
- `research/synthesis/practices.md` for checked practices and examples;
- `research/exemplars/full_text_checks.md` for full-text locators;
- `research/exemplars/official_awards.json` for official recognition metadata.

Cards point to sentence IDs in a retrieved abstract snapshot that is not
committed publicly. A source locator and card claim are not substitutes for
reading the full text when the recommendation depends on an experiment, proof,
figure, table, limitation, or reproducibility detail.

Keep these levels separate:

1. `abstract`: framing, stated contribution, and author-reported evidence;
2. `full-text section` or `figure/table`: experimental, methodological, or
   proof details at the cited locator;
3. `review/meta-review`: reviewer opinion, not scientific fact;
4. `official venue guidance` or `award`: venue context or official recognition,
   not evidence that a design caused a decision.

If the source is unavailable, label advice as general research guidance. Never
invent a citation, review, result, or KDD requirement.
