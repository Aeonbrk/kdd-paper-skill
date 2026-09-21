#!/usr/bin/env python3
"""Resolve official award titles to frozen PaperWarehouse paper IDs."""

import json
import re
from pathlib import Path

WAREHOUSE = Path("/Users/oian/Documents/PaperWarehouse/library/papers")
OUT = Path(__file__).resolve().parent / "official_awards.json"


def norm(text):
    return re.sub(r"[^a-z0-9]+", "", text.lower())


def records():
    result = {}
    for path in WAREHOUSE.glob("sigkdd-*.md"):
        text = path.read_text(encoding="utf-8")
        match = re.search(r'^title:\s*["\']?(.*?)["\']?$', text, re.MULTILINE)
        if match:
            result[norm(match.group(1))] = path.stem
    return result


entries = [
    (2022, "Best Paper Award", "Research Track", "Learning Causal Effects on Hypergraphs", "https://www.kdd.org/awards/view/2022-sigkdd-best-paper-award-winners"),
    (2022, "Best Paper Award runner-up", "Research Track", "Partial-Quasi-Newton Methods: Efficient Algorithms for Minimax Optimization Problems with Unbalanced Dimensionality", "https://www.kdd.org/awards/view/2022-sigkdd-best-paper-award-winners"),
    (2022, "Best Student Paper Award", "Research Track", "Flexible Modeling and Multitask Learning using Differentiable Tree Ensembles", "https://www.kdd.org/awards/view/2022-sigkdd-best-paper-award-winners"),
    (2022, "Best Paper Award", "Applied Data Science Track", "EasyFGL: Towards a Unified, Comprehensive and Efficient Platform for Federated Graph Learning", "https://www.kdd.org/awards/view/2022-sigkdd-best-paper-award-winners"),
    (2022, "Best Paper Award runner-up", "Applied Data Science Track", "Greykite: Deploying Flexible Forecasting at Scale at LinkedIn", "https://www.kdd.org/awards/view/2022-sigkdd-best-paper-award-winners"),
    (2023, "Best Paper Award", "Research Track", "All in One: Multi-task Prompting for Graph Neural Networks", "https://www.kdd.org/awards/view/2023-sigkdd-best-paper-award-winners"),
    (2023, "Best Student Paper Award", "Research Track", "Feature-based Learning for Diverse and Privacy-Preserving Counterfactual Explanations", "https://www.kdd.org/awards/view/2023-sigkdd-best-paper-award-winners"),
    (2023, "Best Paper Award", "Applied Data Science Track", "Improving Training Stability for Multitask Ranking Models in Recommender Systems", "https://www.kdd.org/awards/view/2023-sigkdd-best-paper-award-winners"),
    (2024, "Best Paper Award", "Research Track", "CAT: Interpretable Concept-based Taylor Additive Models", "https://www.kdd.org/awards/view/2024-sigkdd-best-paper-award-winners"),
    (2024, "Best Student Paper Award", "Research Track", "Dataset Regeneration for Sequential Recommendation", "https://www.kdd.org/awards/view/2024-sigkdd-best-paper-award-winners"),
    (2024, "Best Paper Award", "Applied Data Science Track", "LiGNN: Graph Neural Networks at LinkedIn", "https://www.kdd.org/awards/view/2024-sigkdd-best-paper-award-winners"),
    (2024, "Best Paper Award runner-up", "Applied Data Science Track", "Nested Fusion: A Method for Learning High Resolution Latent Structure of Multi-Scale Measurement Data on Mars", "https://www.kdd.org/awards/view/2024-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award", "Research Track", "Improving Group Robustness on Spurious Correlation via Evidential Alignment", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award runner-up", "Research Track", "Monitoring Robustness and Individual Fairness", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award honorable mention", "Research Track", "SIGEM: A Simple Yet Effective Similarity Based Graph Embedding Method", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Student Paper Award", "Research Track", "Taming Recommendation Bias with Causal Intervention on Evolving Personal Popularity", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Student Paper Award runner-up", "Research Track", "Brain Effective Connectivity Estimation via Fourier Spatiotemporal Attention", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Student Paper Award honorable mention", "Research Track", "Verification of Incomplete Graph Unlearning Through Adversarial Perturbations", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award", "Applied Data Science Track", "Evaluating Decision Rules Across Many Weak Experiments", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award runner-up", "Applied Data Science Track", "Put Teacher in Student’s Shoes: Cross-Distillation for Ultra-compact Model Compression Framework", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award honorable mention", "Applied Data Science Track", "Web Scale Graph Mining for Cyber Threat Intelligence", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award honorable mention", "Applied Data Science Track", "VLM as Policy: Common-Law Content Moderation Framework for Short Video Platform", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award", "Datasets and Benchmarks Track", "When Heterophily Meets Heterogeneity: Challenges and a New Large-Scale Graph Benchmark", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award runner-up", "Datasets and Benchmarks Track", "A Guide to Misinformation Detection Data and Evaluation", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
    (2025, "Best Paper Award runner-up", "Datasets and Benchmarks Track", "HtFLlib: A Comprehensive Heterogeneous Federated Learning Library and Benchmark", "https://www.kdd.org/awards/view/2025-sigkdd-best-paper-award-winners"),
]

index = records()
# The official 2022 award page used the conference presentation title
# "EasyFGL"; ACM/Crossref proceedings metadata uses the published title.
index[norm("EasyFGL: Towards a Unified, Comprehensive and Efficient Platform for Federated Graph Learning")] = "sigkdd-2022-3534678-3539112"
out = []
unresolved = []
for year, category, track, title, source in entries:
    paper_id = index.get(norm(title))
    if not paper_id:
        unresolved.append({"year": year, "title": title})
    out.append({"year": year, "category": category, "track": track, "title": title, "paper_id": paper_id, "official_source": source})
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps({"entries": out, "unresolved": unresolved}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"entries": len(out), "unresolved": len(unresolved)}))
