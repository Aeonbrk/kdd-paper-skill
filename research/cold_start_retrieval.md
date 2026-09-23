# Cold-start retrieval experiment

Eight fresh-context cases tested the current skill without giving paper IDs or exemplar names in advance. Each case used targeted manifest/card lookup, then inspected the selected papers' actual abstract source before judging comparability. Selection was not based on awards.

## Result

PASS. Every case produced a small set containing at least two genuinely comparable KDD papers. The skill disclosed contribution-type, track, evidence, and setting mismatches instead of treating adjacent papers as identical. No case collapsed onto award or famous-paper status. No retrieval helper was added.

## Cases and selected source set

1. **Graph method with dynamic heterophily and weak evaluation design** — PASS. sigkdd-2025-3711896-3737155 (TIDFormer), sigkdd-2025-3711896-3737421 (heterophily benchmark), sigkdd-2022-3534678-3539431 (CrossHG-Meta), and sigkdd-2022-3534678-3539300 (ROLAND) cover dynamic/heterophilous graph structure, evaluation design, and scalability with explicit scope differences.
2. **Cold-start sequential recommender** — PASS. sigkdd-2023-3580305-3599519 (Recformer), sigkdd-2025-3690624-3709336 (PAM), and sigkdd-2024-3637528-3671588 (IHM) cover cold-start representation, online adaptation, and applied deployment constraints.
3. **Robustness and fairness without group labels** — PASS. sigkdd-2025-3711896-3737002 (Evidential Alignment), sigkdd-2024-3637528-3672006 (SPUME), and sigkdd-2023-3580305-3599514 (SURE) provide direct robustness, spurious-correlation, and fairness comparisons with evidence-boundary differences stated.
4. **Benchmark/resource for multimodal flood mapping** — PASS. sigkdd-2024-3637528-3671536 (CropNet), sigkdd-2025-3711896-3737440 (SatHealth), and sigkdd-2025-3711896-3737406 (ClimateIQA) are resource/benchmark analogs; none was treated as a substitute for a new predictor.
5. **Real-time applied demand-forecasting system** — PASS. sigkdd-2022-3534678-3539165 (Greykite), sigkdd-2022-3534678-3539058 (Lion), and sigkdd-2023-3580305-3599848 (Interactive GAM) cover operational forecasting, system constraints, and deployment-oriented modeling.
6. **Theory-heavy conformal graph method** — PASS. sigkdd-2024-3637528-3672061 (conformalized link prediction) and sigkdd-2025-3711896-3737064 (NCPNET) match assumption, coverage, and temporal-dependence questions while preserving theorem/evaluation boundaries.
7. **Weak causal experiment plan** — PASS. sigkdd-2024-3637528-3671950 (time-varying counterfactual generation) and sigkdd-2023-3580305-3599774 (TVAE) provide causal estimand, synthetic/real evaluation, and baseline-comparison analogs.
8. **Manuscript claim with unclear evidence attribution** — PASS. sigkdd-2024-3637528-3671655 (recommendation benchmarking), sigkdd-2025-3711896-3737428 (EBES), and sigkdd-2024-3637528-3671820 (PageRank) support attribution and evidence-boundary comparisons without turning source claims into warehouse judgments.

The selected IDs were verified against the frozen corpus manifest and the current abstract cache. The experiment did not change PaperWarehouse or the canonical corpus.
