---
name: kdd-paper-skill
description: Compare a research idea, manuscript, or experiment plan with relevant SIGKDD evidence, or teach one source-linked KDD research practice. Use for KDD Research, Applied Data Science, Datasets and Benchmarks, AI for Sciences, and related archival-track work. Not an acceptance predictor or generic writing formatter.
---

# KDD Paper Skill

Use this skill to help an author learn from inspected SIGKDD papers while
preserving the author's scientific purpose and judgment. PaperWarehouse is the
neutral identity and discovery warehouse. This downstream repository owns
study-specific retrieval cards, checked examples, practices, and manuscript
comparison guidance.

## Evidence boundary

Read [sources and evidence](references/sources-and-evidence.md) when selecting
examples or making an attributed claim. Read [KDD practices](references/kdd-practices.md)
through `research/synthesis/practices.md` when applying a practice. Read
[archetypes](references/archetypes.md) before comparing papers with different
contribution types.

The general corpus cards are abstract-linked retrieval aids produced by a
bounded rule extractor. Their source-unit IDs establish traceability, not
semantic fidelity. Research Track papers with available abstracts also have
one-paper semantic cards under `research/semantic_cards/research_track/`.
Those cards are source-grounded abstract evidence, not full-text reading.
Before attributing an abstract-level claim from either card surface, inspect
the underlying abstract at the recorded source locator. Use
[full-text checks](../../research/exemplars/full_text_checks.md) when a
recommendation depends on experimental, methodological, proof, figure, table,
or reproducibility detail.

Keep four things distinct:

- source observation: what the inspected paper or official venue page reports;
- interpretation: why that observation may help an author;
- recommendation: what the user could change or check;
- unknown: what the inspected source does not establish.

Never infer acceptance causes from an award or an accepted paper. Do not output
KDD scores, acceptance probabilities, KDD-ready percentages, GO/WAIT/KILL
verdicts, or a universal checklist.

## Select evidence

Use the frozen corpus manifest and targeted retrieval or semantic cards to find
a small comparison set. Select by problem structure, contribution type,
evidence need, evaluation setting, and resource constraints. Do not select by
fame or award status alone. Use Research Track semantic cards when available;
for other tracks, use retrieval cards and inspect the source on demand. Keep
Research, Applied Data Science, Datasets and Benchmarks, AI for Sciences, Blue
Sky Ideas, Health Day, and other tracks distinct when their evidence questions
differ.

Do not enumerate or load the full retrieval or semantic card directories for
one request. Use targeted manifest, track/year, award, title, and paper-ID
lookups. Then inspect the underlying source for every attributed comparison
that matters to the advice.

Do not use PaperWarehouse discovery synopses or search snippets as semantic
evidence. When a source cannot be inspected, label the statement as general
research guidance and omit source attribution.

For every KDD-derived observation, name the paper and link the direct abstract
or inspected full-text locator. A program or table-of-contents page, retrieval
card, or search result can locate a candidate but is not a semantic evidence
locator. Do not report an attributed source comparison without that link.

## Mode A: compare and improve

Use this mode when the user supplies an idea, abstract, introduction, method,
experiment plan, results section, or manuscript.

1. Identify the user's actual claim, contribution type, current evidence,
   stage, and important constraints.
2. Choose a small relevant KDD comparison set.
3. Return at most three high-priority improvements by default. For each one,
   connect:

   `user artifact location → inspected source observation and locator → concrete change or feasible next check → why it applies → important difference or limit`

4. Keep source observation separate from the proposed action. Preserve metrics,
   populations, horizons, information budgets, model classes, and guarantee
   conditions beside conclusions.

Do not manufacture a gap. If the artifact already has adequate support, say so.
If a suggestion depends on a full-text experiment or figure, use an inspected
locator instead of inferring it from an abstract.

## Mode B: learn and reflect

Use this mode when the user asks how KDD papers frame contributions, design
comparisons, report evidence, or present a resource. Teach one practice with:

- a source-linked KDD example and reading level;
- the purpose of the practice;
- when it applies;
- an important exception or transfer limit;
- one focused exercise on the user's own paragraph, comparison, or plan.

Do not dump the whole corpus or every practice. Do not force method, theory,
empirical, system, resource, applied, and position papers into one evidence
template.

## KDD context

Official KDD CFP guidance is context, not a score. The [KDD 2025 Research Track
CFP](https://kdd2025.kdd.org/research-track-call-for-papers/) and [KDD 2026
Research Track CFP](https://kdd2026.kdd.org/research-track-call-for-papers/)
mention technical merit, originality, potential impact, quality of execution and
presentation, related work, reproducibility, and ethics, and say the first
eight content pages should be self-contained. Cite the official page when using
that context. Keep it separate from paper evidence and advice to the user.

Official award metadata is selection metadata. It can help locate a clear
exemplar, but it is not evidence that the example caused recognition or that
the user should copy it. Test-of-Time awards are outside this 2022–2026 corpus.

## Writing discipline

Use concrete paper-specific language. Avoid generic claims such as "important
problem," "innovative framework," "extensive experiments," and "valuable
insights." Do not silently upgrade an author's claim into an independent
conclusion. Keep unknowns unknown and state the actual reading level.
