# KDD Research Track practice synthesis

This synthesis draws bounded examples from Research Track semantic cards across 2022–2026 and five full-text checks. The selected examples do not estimate prevalence, explain acceptance, or rank papers.

## Name the task, limitation, and changed object

Observed pattern: Several abstracts state a concrete constraint before describing the operation that addresses it. PSMC identifies motif-instance enumeration and graph-scale costs, then introduces a locally computable Motif Resident metric and dynamic updates. DEXA describes data scarcity and a semantic gap in modular extreme-classification training before adding auxiliary parameters to encoder training. The incentive-policy paper identifies the failure to identify “Always Buyers” before proposing counterfactual strata and estimators.

Supporting sources:

- PSMC, `sigkdd-2024-3637528-3671666`, [abstract metadata](https://openalex.org/W4401863181), source units S3–S11.
- Deep Encoders with Auxiliary Parameters for Extreme Classification, `sigkdd-2023-3580305-3599301`, [abstract metadata](https://openalex.org/W4385567541), source units S2–S7.
- Who Should Be Given Incentives?, `sigkdd-2023-3580305-3599550`, [abstract metadata](https://openalex.org/W4385562472), source units S3–S8.

Variation and boundary: Dual-view Molecular Pre-training states a molecular-representation task but does not identify a distinct prior-work limitation in its abstract; its semantic card leaves the gap absent (`sigkdd-2023-3580305-3599317`, [abstract metadata](https://openalex.org/W4385567824), source unit S1). A gap should remain unknown when the source does not state one.

Interpretation: Naming the task and the stated limitation makes the intended role of a proposed mechanism easier to inspect.

Possible application: State the task, the source-supported limitation, and the object or operation changed before describing a module or framework.

Applicability boundary: Abstracts report the authors’ framing. They do not establish that a claimed gap holds across the field or that the proposed mechanism resolves it.

## Keep operating conditions beside reported results

Observed pattern: Abstracts sometimes bind a result to the regime that gives it meaning. Matrix Profile XXIV reports exact left-discord computation at up to 300,000 Hz on a commodity desktop and describes datasets with trillions of datapoints. DEXA reports different accuracy improvements on benchmark and proprietary datasets and says it scales to 40 million labels. Conformal Counterfactual Inference reports marginal coverage under hidden confounding and a split-conformal variant with lower computational cost.

Supporting sources:

- Matrix Profile XXIV, `sigkdd-2022-3534678-3539271`, [abstract metadata](https://openalex.org/W4290878309), source units S7–S9.
- Deep Encoders with Auxiliary Parameters for Extreme Classification, `sigkdd-2023-3580305-3599301`, [abstract metadata](https://openalex.org/W4385567541), source unit S6.
- Conformal Counterfactual Inference under Hidden Confounding, `sigkdd-2024-3637528-3671976`, [abstract metadata](https://openalex.org/W4401863895), source units S4, S7, and S9.

Variation and boundary: GEO reports up to 40% greater visibility and says strategy effectiveness varies by domain (`sigkdd-2024-3637528-3671900`, [abstract metadata](https://openalex.org/W4401864200), source units S8–S10). These performance claims use different tasks and measures; they cannot be combined into a common ranking.

Interpretation: A result without its dataset, assumption, resource limit, or operating regime can imply broader support than the abstract provides.

Possible application: Keep the metric, dataset or population, model scale, assumption, and resource condition in the sentence that states a result. If the abstract omits a condition, leave it unknown.

Applicability boundary: These are author-reported abstract claims, not independent checks of the result or its operating limits.

## Match evidence to the contribution

Observed pattern: The evidence form varies with the claim. The incentive-policy paper reports estimator properties and a policy-reward bound alongside experiments on three real-world datasets and two incentive scenarios. Numerical Tuple Extraction introduces a finance dataset of 19,264 tables and 604,000 tuples for evaluating a relation-extraction framework. GEO separates a visibility-optimization method from GEO-bench, a benchmark of queries and web sources, and reports domain variation in strategy effectiveness.

Supporting sources:

- Who Should Be Given Incentives?, `sigkdd-2023-3580305-3599550`, [abstract metadata](https://openalex.org/W4385562472), source units S6–S9.
- Numerical Tuple Extraction from Tables with Pre-training, `sigkdd-2022-3534678-3539460`, [abstract metadata](https://openalex.org/W4290876141), source units S9–S13.
- GEO: Generative Engine Optimization, `sigkdd-2024-3637528-3671900`, [abstract metadata](https://openalex.org/W4401864200), source units S7–S10.

Variation and boundary: A dataset contribution needs evidence about the resource and its evaluation use; a theoretical claim needs its stated assumptions and guarantee; a method claim needs task-appropriate comparisons. An abstract may describe only part of those details, as in the tuple-extraction paper, whose abstract gives dataset size and a baseline comparison but does not establish dataset coverage or access conditions.

Interpretation: A baseline comparison alone does not test every kind of contribution. Evidence should address the claim the paper makes.

Possible application: For each manuscript claim, name the evidence that could distinguish it: theorem conditions for formal claims, task-specific measurements for empirical methods, and coverage or access details for resources.

Applicability boundary: These examples show how the authors describe their evidence. They do not verify proofs, data quality, benchmark completeness, or full experimental results.

## Full-text boundary

The five [full-text checks](../exemplars/full_text_checks.md) used for synthesis cover the method, experiment, and reporting details needed by these bounded examples. The three additional checks listed there were used for a fresh-context behavior case, not for this synthesis.
