# Handoff

Authoritative branch: `main`.

PaperWarehouse source revision:
`118a82ce657a2bf6915afdc82921553dc765740a`.

## Current validated state

- KDD 2022–2026 corpus identity is frozen at 3,696 papers.
- Cold-start retrieval passed 8 of 8 cases. No retrieval helper is needed.
- The 40-paper Research Track semantic pilot produced 38 PASS, 2 MINOR, and
  0 MATERIAL cases after one bounded prompt/schema redesign.
- Research Track contains 2,314 identities, 2,103 semantic cards, and 211 papers
  without a reliable abstract.
- The current synthesis contains three bounded practices and eight distinct
  source-linked examples.
- Eight full-text exemplars have been inspected. Five support synthesis and
  three support behavior checks.
- PaperWarehouse remains unchanged.

## Current decision

Do not reopen corpus enumeration, retrieval architecture, semantic-card scaling,
missing-abstract recovery, or synthesis breadth without new evidence that one of
those layers caused a user-visible failure.

Five fresh-context behavior cases produced 3 PASS and 2 MIXED outcomes. The
remaining blocker is final source binding.

The two concrete failures are:

1. One experiment-design answer used valid sources but omitted paper names in
   its source observations.
2. One result-interpretation answer attributed an analysis to the wrong paper
   and used a locator that did not cover the condition cited by the
   recommendation.

## Next action

Inspect only those two mixed cases first. Trace each failure through the
retrieved paper, evidence record, selected source observation, locator, and
final recommendation. Find the first layer where the evidence and output
diverge, then fix that layer only.

After the smallest fix, rerun the two failing cases and at most three genuinely
fresh regression cases. Include one case where no substantive change is
warranted.

If the source-binding failures are gone and no new material failure appears,
stop.

## Known limitations

- 211 Research Track papers lack a reliable abstract.
- Ninety-five scaled-card claim references could not be replayed against the
  current OpenAlex cache sentence segmentation. They are not established source
  errors and are not a blocker unless a final recommendation depends on one of
  them.
- Abstract-only cards do not establish full-text experimental adequacy, proof
  correctness, reproducibility, or omitted limitations.
