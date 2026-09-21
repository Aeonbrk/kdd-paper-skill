---
name: kdd-paper-skill
description: Compare a research idea, manuscript, or experiment plan with relevant SIGKDD evidence, or teach one source-linked KDD research practice. Use for KDD Research, Applied Data Science, Datasets and Benchmarks, AI for Sciences, and related archival-track work. Not an acceptance predictor or generic writing formatter.
---

# KDD Paper Skill

Use this skill to help an author learn from inspected SIGKDD papers while
preserving the author's scientific purpose and judgment. PaperWarehouse is the
neutral identity and discovery warehouse. This downstream repository owns
study cards, checked examples, practices, and manuscript comparison guidance.

## Evidence boundary

Read [sources and evidence](references/sources-and-evidence.md) when selecting
examples or making an attributed claim. Read [KDD practices](references/kdd-practices.md)
through `research/synthesis/practices.md` when applying a practice. Read
[archetypes](references/archetypes.md) before comparing papers with different
contribution types.

Abstract cards are `abstract_only`. They support problem framing, stated
contributions, and author-reported evidence. They do not verify experimental
adequacy, proof correctness, figure design, reproducibility, or full-text
limitations. Use [full-text checks](../../research/exemplars/full_text_checks.md)
when a recommendation depends on those details.

Keep four things distinct:

- source observation: what the paper or official venue page reports;
- interpretation: why that pattern may help an author;
- recommendation: what the user could change or check;
- unknown: what the inspected source does not establish.

Never infer acceptance causes from an award or an accepted paper. Do not output
KDD scores, acceptance probabilities, KDD-ready percentages, GO/WAIT/KILL
verdicts, or a universal checklist.

## Select evidence

Use the frozen corpus manifest and retrieve a small comparison set. Select by
problem structure, contribution type, evidence need, evaluation setting, and
resource constraints. Do not select by fame or award status alone. Keep Research,
Applied Data Science, Datasets and Benchmarks, AI for Sciences, Blue Sky Ideas,
Health Day, and other tracks distinct when their evidence questions differ.
Do not enumerate or load the full card directory for one request. Use the
manifest, track/year fields, award manifest, and targeted title or paper-ID
lookups to choose the few cards needed.

If the local cards do not answer the question, retrieve the actual abstract or
full text from the recorded source locator. Do not use PaperWarehouse's
discovery synopsis as a replacement for the source. Do not use search snippets
as semantic evidence. When a source cannot be inspected, label any statement
as general guidance and omit the citation.

## Mode A: compare and improve

Use this mode when the user supplies an idea, abstract, introduction, method,
experiment plan, results section, or manuscript.

1. Identify the user's actual claim, contribution type, current evidence,
   stage, and important constraints.
2. Choose a small relevant KDD comparison set.
3. Return at most three high-priority improvements by default. For each one,
   connect:

   `user artifact location → source observation and locator → concrete change or feasible next check → why it applies → important difference or limit`

4. Keep paper observations separate from your proposed action. Preserve
   metrics, populations, horizons, information budgets, model classes, and
   guarantee conditions beside conclusions.

Do not manufacture a gap. If the artifact already has adequate support, say so.
If a suggestion depends on a full-text experiment or figure, name the exact
locator or ask for the source instead of inferring it from an abstract.

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

Official KDD CFP guidance is context, not a score. The [KDD 2025 Research
Track CFP](https://kdd2025.kdd.org/research-track-call-for-papers/) and [KDD
2026 Research Track CFP](https://kdd2026.kdd.org/research-track-call-for-papers/)
mention technical merit, originality, potential impact, quality of execution
and presentation, related work, reproducibility, and ethics, and says the first
eight content pages should be self-contained. Cite the official page when using
that context. Keep it separate from observed paper patterns and from advice to
the user.

Official award metadata is selection metadata. It can help choose a clear
exemplar, but it is not evidence that the example caused recognition or that
the user should copy it. Test-of-Time awards are outside this 2022–2026 skill
corpus.

## Writing discipline

Use concrete paper-specific language. Avoid generic claims such as
"important problem," "innovative framework," "extensive experiments," and
"valuable insights." Do not silently upgrade an author's claim into an
independent conclusion. Keep unknowns unknown and state when evidence is
abstract-only.
