# KDD Paper Skill

KDD Paper Skill compares a research idea, manuscript section, or experiment
plan with a small set of relevant SIGKDD examples. It also teaches bounded
research and evidence practices with source-linked examples and transfer
limits.

It is not an acceptance predictor, a KDD scorecard, or a generic writing bot.
Recommendations keep source observation, interpretation, and proposed action
separate.

The current evidence base contains 3,696 archival SIGKDD identities for
2022–2026 from PaperWarehouse revision
`118a82ce657a2bf6915afdc82921553dc765740a`.

The general corpus has 3,249 retrieval cards and 447 records without a reliable
abstract in the completed retrieval run. Research Track has 2,314 identities,
2,103 source-grounded semantic cards, and 211 records without a reliable
abstract. A 40-paper semantic pilot produced 38 PASS, 2 MINOR, and 0 MATERIAL
fidelity judgments before Research Track scaling.

Cold-start retrieval passed 8 of 8 fresh cases without a retrieval helper. Five
fresh-context behavior cases produced 3 PASS and 2 MIXED outcomes. One confirmed
source-binding defect is missing paper names in source observations. The other
historical MIXED case has no retained prompt or answer, so its cause is
unresolved.

See `Handoff.md` for the current next decision, `docs/distillation.md` for the
evidence contract, and `skills/kdd-paper-skill/SKILL.md` for user-facing
behavior.
