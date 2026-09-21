# KDD practice synthesis

Run scope: all 3,696 SIGKDD 2022–2026 cards, grouped by track and contribution
type after the abstract extraction run. Research Track is the primary surface.
The practices below are bounded editorial guidance, not venue laws. Abstract
examples are linked to card source locators. Full-text examples identify the
inspected locator separately.

## State the changed object and the research tension

Observed pattern: Research abstracts often pair an operational or scientific
constraint with a changed object, such as a representation, estimator, model
component, or benchmark. CAT changes the representation used for an
interpretable predictor, while STEADY combines a statistical estimator with
physical dynamics. The cards identify these statements at abstract sentence
units rather than treating a method name as the contribution.

Why it may help: A reader can see what the work changes before deciding whether
the change matters. This is an editorial interpretation, not a measured cause
of acceptance.

Try this: Name the task constraint, the prior object or operation, the precise
change, and what the change is meant to enable. Keep an explanation or
novelty claim attributed unless the supplied evidence establishes it.

Use when: The draft introduces a module or framework but the contribution
delta is hard to state without the method name.

Exception: A resource or descriptive finding may contribute through coverage,
measurement, or characterization rather than replacing a prior method.

Examples:

- [CAT: Interpretable Concept-based Taylor Additive Models](https://doi.org/10.1145/3637528.3672020), `sigkdd-2024-3637528-3672020`, abstract, Research Track. Full-text check: Sections 4.1–4.2 and 5.5.
- [Stein-type Estimator Assisted by Dynamics](https://doi.org/10.1145/3770854.3780166), `sigkdd-2026-3770854-3780166`, abstract, Research Track.

## Keep the measured condition beside the conclusion

Observed pattern: KDD abstracts and checked papers state results with a task,
population, horizon, metric, or resource condition. CAT reports separate
regression and classification metrics across six benchmarks. Greykite reports
horizon- and frequency-specific comparisons and then describes LinkedIn
deployment conditions.

Why it may help: Removing the condition can turn a bounded observation into a
claim about a broader capability than the evidence covers.

Try this: Put the metric, unit, data population, forecast horizon, model
class, or guarantee regime in the same sentence as the result. If a condition
is absent, narrow the claim or mark the missing check.

Use when: The draft says a method is better, robust, efficient, or general but
does not identify the comparison boundary.

Exception: A formal statement may have a different boundary from an empirical
result. Do not add experimental qualifiers to a theorem or imply a guarantee
that the source does not state.

Examples:

- [CAT: Interpretable Concept-based Taylor Additive Models](https://doi.org/10.1145/3637528.3672020), `sigkdd-2024-3637528-3672020`, full text, Table 3 and Section 5.4.
- [Greykite: Deploying Flexible Forecasting at Scale at LinkedIn](https://doi.org/10.1145/3534678.3539165), `sigkdd-2022-3534678-3539165`, full text, Section 5.2.2, Tables 1–2, and Section 6.1.
- [Stein-type Estimator Assisted by Dynamics](https://doi.org/10.1145/3770854.3780166), `sigkdd-2026-3770854-3780166`, abstract, Research Track.

## Choose comparisons that answer the stated claim

Observed pattern: The checked method papers name the baseline family and the
property being compared. CAT compares interpretable and black-box models and
reports parameter and throughput tables. Evidential Alignment compares
worst-group accuracy, average accuracy, and the accuracy gap across image and
text datasets. These are observations from the cited papers, not instructions
that every paper must reproduce them.

Why it may help: A comparison is useful when its design distinguishes the
claim from plausible alternative explanations.

Try this: Write the decision the comparison should resolve, then name what is
held fixed, what changes, the outcome, and the interpretation for each result.
Use a component ablation only when attribution is the decision. Compare
delivered systems when the claim concerns the system as used.

Use when: A proposed experiment lists baselines or ablations without saying
what each comparison is meant to decide.

Exception: A resource, theory, or position paper may need coverage, theorem
conditions, or argument comparison rather than a model leaderboard.

Examples:

- [CAT: Interpretable Concept-based Taylor Additive Models](https://doi.org/10.1145/3637528.3672020), `sigkdd-2024-3637528-3672020`, full text, Section 5.2, Tables 3–4, Appendix A.2/Table 7.
- [Improving Group Robustness on Spurious Correlation via Evidential Alignment](https://doi.org/10.1145/3711896.3737002), `sigkdd-2025-3711896-3737002`, full text, Sections 5.1–5.5, Tables 2–4.
- [Evaluating Decision Rules Across Many Weak Experiments](https://doi.org/10.1145/3711896.3737217), `sigkdd-2025-3711896-3737217`, full text, Sections 3–4.3.

## Treat systems and resources as bounded research contributions

Observed pattern: ADS and Datasets and Benchmarks papers describe the
interface, data scope, workload, split or access conditions, and activity
enabled. Greykite ties forecast configuration to operational dashboards and
forecast horizons. H2GB records dataset domains, split policy, metrics,
baseline groups, and reproducibility configuration.

Why it may help: A resource or deployed system can be evaluated on what it
enables and under which conditions, without forcing it into a new-algorithm
template.

Try this: State the units, construction or interface, access status, intended
use, demonstrated use, and the boundary that remains untested.

Use when: The contribution is a dataset, benchmark, library, deployment, or
system rather than only a predictive component.

Exception: Do not claim broad coverage, validity, or production impact from a
small demonstration or an abstract that does not report the relevant detail.

Examples:

- [When Heterophily Meets Heterogeneity: Challenges and a New Large-Scale Graph Benchmark](https://doi.org/10.1145/3711896.3737421), `sigkdd-2025-3711896-3737421`, full text, Sections 3.2–3.4, Table 1, Section 5.1.
- [Greykite: Deploying Flexible Forecasting at Scale at LinkedIn](https://doi.org/10.1145/3534678.3539165), `sigkdd-2022-3534678-3539165`, full text, Sections 5.2.2 and 6.1–6.2.

## Use official guidance as context, not as a score

Observed venue guidance: KDD 2025 and 2026 Research Track CFP material lists
technical merit, originality, potential impact, quality of execution and
presentation, related work, reproducibility, and ethics, and says that the
first eight content pages should be self-contained. The pages do not define a
numeric weighting or acceptance function.

Try this: Use the guidance to decide what context a manuscript section must
make legible, then use comparable paper evidence to choose a concrete revision.

Exception: Guidance does not override the contribution type or prove that a
particular paper choice caused acceptance.

Sources: [KDD 2025 Research Track CFP](https://kdd2025.kdd.org/research-track-call-for-papers/) and [KDD 2026 Research Track CFP](https://kdd2026.kdd.org/research-track-call-for-papers/).
