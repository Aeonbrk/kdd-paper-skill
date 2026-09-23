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

Five fresh-context behavior cases produced 3 PASS and 2 MIXED outcomes. One
confirmed defect is that a recommender experiment-design answer omitted paper
names from its source observations. The other MIXED result is historical only;
its exact prompt and answer are unavailable, so its failure mechanism is
unresolved.

The linked MRSA paper reports patient-subpopulation treatment effects in
§4.9/Table 3 and hospital-unit estimates in Table 4. Do not treat those
observations as unsupported.

## Source-attribution regression

One new fresh-context multi-paper case passed the scoped checks: both papers
were named, observations were attributed to the correct paper, and the cited
sections/tables supported the claims and conditions. The historical second
MIXED case remains unresolved; its prompt and answer are unavailable. This
regression does not reproduce or resolve it.

## Known limitations

- 211 Research Track papers lack a reliable abstract.
- Ninety-five scaled-card claim references could not be replayed against the
  current OpenAlex cache sentence segmentation. They are not established source
  errors and are not a blocker unless a final recommendation depends on one of
  them.
- Abstract-only cards do not establish full-text experimental adequacy, proof
  correctness, reproducibility, or omitted limitations.
