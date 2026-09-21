# KDD Paper Skill

KDD Paper Skill helps an author compare an idea, manuscript section, or
experiment plan with a small set of relevant SIGKDD examples. It also teaches
bounded research and evidence practices with source-linked examples and
exceptions.

It is not an acceptance predictor, a KDD scorecard, or a generic writing bot.
Recommendations preserve the author's scientific purpose and distinguish what
a source reports from an interpretation and a proposed action.

The current corpus contains 3,696 archival SIGKDD identities for 2022–2026 from
PaperWarehouse. The frozen upstream revision is recorded in
`research/corpus/manifest.jsonl` and
`research/abstract_distillation/results.md`.

Of those identities, 3,249 have OpenAlex-backed abstract retrieval cards and 447
lack a reliable abstract in the completed run. The cards were produced by the
bounded rule extractor and are retrieval aids with source locators; they are not
a semantic source audit. Source-dependent recommendations return to the
inspected abstract or to the bounded full-text checks before attribution.

Install the skill directory under a supported skills path, then invoke it for
requests to compare or learn from KDD evidence.
