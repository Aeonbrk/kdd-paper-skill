# Skill behavior checks

Date: 2026-09-21

Four fresh-context runs exercised the skill with targeted reads only. The
checks used the skill file, its named evidence references, the practice
synthesis, the full-text inspection notes, and five named card/manifest
lookups. They did not enumerate the card directory.

- Mode A, longitudinal treatment-response artifact: returned three bounded
  changes tied to source locators, preserved the distinction between prediction
  and causal treatment effects, and marked the clinical adaptations as
  recommendations rather than reported source experiments.
- Mode A, graph node-classification artifact: returned three changes for
  controlled comparison, component attribution, and a prespecified robustness
  condition, with contribution-type and transfer limits.
- Mode B, benchmark-reporting question: taught one checked practice with a
  source example, reading level, purpose, transfer limit, and focused exercise.
- Guard test, acceptance probability and ranking request: refused the
  prohibited judgment and offered bounded source-linked revision guidance.

The runs used local full-text inspection notes for the evidence-dependent
examples; they did not claim new PDF reading. The checks test routing,
evidence labeling, output bounds, and prohibited-output handling. They do not
measure scientific correctness or user benefit.

## Fresh-context checks

Date: 2026-09-23.

Five unseen artifacts were run through the local skill in separate read-only
contexts without comparator IDs or exemplar names in the prompts.

- Method framing: retrieved ROLAND and TIDFormer for temporal graph comparison,
  linked their arXiv abstracts, and limited a third fraud-delay candidate to
  title-level overlap because its abstract was not inspectable. The answer
  rejected the unsupported “first” claim and separated split leakage from
  delayed-label validity. PASS.
- Recommender experiment design: proposed matched tuning, seed variation, and
  one temporal split. It linked three actual abstracts and kept cold-start
  analysis optional, but did not name the compared papers in its source
  observations. MIXED.
- Retrospective policy-result interpretation: historical outcome MIXED. The
  exact prompt and answer are unavailable, so the source-attribution and locator
  failure mechanism remains unresolved. The linked MRSA paper reports
  patient-subpopulation treatment effects in §4.9/Table 3 and hospital-unit
  estimates in Table 4 ([full text](https://arxiv.org/html/2307.08237)).
- Resource and model contribution: separated a healthcare benchmark claim
  from its model claim, linked KDD resource and evaluation examples, and
  bounded the “first” and partial-release claims. PASS.
- Already adequate fraud-method protocol: stated that no substantive new
  analysis was warranted, suggested only result-caption/scope wording, and did
  not manufacture a method critique. PASS.

Three cases passed and two were mixed. Retrieval found comparable KDD records
without supplied IDs. No retrieval helper was added. These checks do not
establish general retrieval or scientific accuracy.

## Source-attribution regression

Date: 2026-09-23.

- Artifact: cross-plant anomaly-detection dataset and graph method; windows from
  every plant are randomly split, with one-run average AUROC and no per-failure
  counts.
- *Diverse Intra- and Inter-Domain Activity Style Fusion for Cross-Person
  Generalization in Activity Recognition* (DI2SDiff): the answer attributed
  cross-person source/target grouping to this paper; §6.1 and Appendix E.1
  support that observation ([full text](https://arxiv.org/html/2406.04609)).
- *HAROOD: A Benchmark for Out-of-distribution Generalization in Sensor-based
  Human Activity Recognition*: the answer attributed dataset dimensions, OOD
  scenarios, and class-varying results to this paper; Table 2, §4, and
  §6.1/Figure 4 support those observations ([full text](https://arxiv.org/html/2512.10807)).
  The answer kept activity-recognition evidence distinct from equipment-failure
  claims.
- PASS for paper naming, attribution, and locator coverage. This does not
  reproduce either historical MIXED case.
