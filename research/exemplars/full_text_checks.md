# Full-text exemplar checks

These are five bounded full-text inspections used to test whether the
abstract-level practices remained accurate when a recommendation depended on
experimental detail. PDFs were retrieved from the authors' public arXiv copies
and kept under the ignored run cache. They are not a full-corpus reading.

| PaperWarehouse paper_id | Reading level | Inspected source | Locators | Use in synthesis |
| --- | --- | --- | --- | --- |
| `sigkdd-2024-3637528-3672020` | full text | [arXiv:2406.17931](https://arxiv.org/abs/2406.17931) | Sections 5.2–5.4, Tables 3–4, Section 5.5, Appendix A.2/Table 7 | matched interpretable and black-box baselines, task-specific metrics, component ablation |
| `sigkdd-2025-3711896-3737002` | full text | [arXiv:2506.11347](https://arxiv.org/abs/2506.11347) | Sections 5.1–5.5, Tables 2–4, Figure 4 | group-conditional metrics, calibration split, robustness comparison, ablation |
| `sigkdd-2025-3711896-3737421` | full text | [arXiv:2407.10916](https://arxiv.org/abs/2407.10916) | Sections 3.2–3.4, Table 1, Section 5.1, Table 3, Appendix reproducibility notes | dataset construction, split policy, simple baselines, scale and reproducibility |
| `sigkdd-2025-3711896-3737217` | full text | [arXiv:2502.08763](https://arxiv.org/abs/2502.08763) | Sections 3–4.3, Theorems 3.1–3.2, Section 5 | estimand and proxy conditions kept beside a decision rule |
| `sigkdd-2022-3534678-3539165` | full text | [arXiv:2207.07788](https://arxiv.org/abs/2207.07788) | Section 5.2.2, Tables 1–5, Sections 6.1–6.2 | fair configuration, horizon-specific metrics, deployment boundary |

These checks support examples of what the papers report. They do not establish
that the inspected choices caused an award or acceptance decision.
