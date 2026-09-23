# KDD Paper Skill

This repository is a downstream learning tool built from the neutral
PaperWarehouse corpus.

- Treat PaperWarehouse as read-only evidence. Reference its stable `paper_id`
  and record the exact source revision used for a run.
- Keep bibliographic identity in PaperWarehouse. Keep study cards, synthesis,
  exemplars, reviews, and manuscript guidance here.
- Use official KDD pages for venue guidance and awards. Use paper abstracts,
  full text, figures, tables, and reviews only at their stated reading level.
- Separate source observation, interpretation, and recommendation. Unknown is
  valid. Do not infer acceptance, quality, novelty, or causal effects.
- Keep Research, Applied Data Science, Datasets and Benchmarks, AI for
  Sciences, and other archival tracks distinct when evidence differs.
- Never output KDD scores, acceptance probabilities, or a universal checklist.
- Do not add raw copyrighted abstracts to tracked files. Keep temporary source
  snapshots under ignored paths when needed for a bounded run.
- Keep prose concrete and free of generic generated filler.

Read `docs/distillation.md` before changing extraction or synthesis artifacts.

## Authority and startup

Before substantial work:

1. Fetch the remote and determine the authoritative branch and revision. Do not
   trust a handoff or local checkout when they disagree with the live remote.
2. Read the nearest applicable `AGENTS.md`, then `Handoff.md`, the current
   docs needed for the task, and only the relevant Decision Notes.
3. Read run evidence only when it affects the current decision. Do not reload
   repository history by default.
4. Before changing shared work, confirm the remote has not advanced.

When records disagree, prefer direct run evidence, then current research
artifacts, current docs and contracts, Decision Notes, and old summaries.

## Knowledge placement

- `docs/` describes the current system, evidence contract, and workflow.
- `research/` stores run-local evidence, experiments, audits, and scientific
  results.
- `skills/` stores current user-facing behavior and compact references.
- `.agents/notes/` stores durable engineering or methodology decisions whose
  reasons cannot be recovered from code, current docs, and tests alone.
- `Handoff.md` is a short pointer to the current validated state and next
  decision.
- Git records how files changed. Do not duplicate commit history in docs.

Update an existing Note when the decision is unchanged and only facts or paths
move. Create a new Note only when the rationale changes or a new non-trivial
architecture, interface, evidence-boundary, schema, workflow, or testing
decision must survive future context loss. Routine fixes and ordinary execution
need no Note.

## Change discipline

Work as an atomic change with one clear purpose. State what must remain
unchanged, identify the most dangerous unresolved assumption, and get the
cheapest evidence that could change the decision before expanding the change.

Checks must protect a reachable invariant. A failed check should change the
implementation, the evidence claim, or the decision. Otherwise do not add the
check.

Normal bug handling is:

```text
determine impact
→ smallest correct fix
→ scoped regression check
→ continue
```

Final code, docs, Notes, commits, and summaries describe the correct end state.
Keep negative scientific or behavior evidence when it changes future decisions.
Do not preserve ordinary debugging traces.

## SCOPE LIMITS (these bound what you PROPOSE, never what you look for)

Report anything that is actually wrong here — including a rare-looking case, if
this project actually produces it. Then keep the fix in scope:

1. This is not a security paper. Verification is welcome; over-defense is not.
   Unless this project states otherwise, assume a cooperating operator on their
   own machine; if it has a real adversary, it will say so and that scope wins.
2. Do not add hashes, checksums or fingerprints unless the hash replaces a
   materially more expensive operation AND its result changes what happens next.
3. No defensive scaffolding: no feature flags, migration frameworks, compat
   layers or wrappers for cases that do not occur here.
4. No corner-case obsession: exotic encodings, symlink races, RTL text and
   millisecond races are out of scope unless the case is reachable through this
   project's supported use — its documented inputs, its published interface, its
   real data. Reachable is enough; you do not need a reproduction. Constructible
   in principle is not enough.
5. Where judgement is needed, judge. Do not replace it with a scoring table, a
   checklist, or a re-verification loop over something already settled.
6. None of this overrides security, migration, verification or review that the
   user, this project's own conventions, or a higher-priority rule asked for.
   Those were requested; they are the work, not scope creep.
7. Deliverable text is not a defense transcript. State plainly what holds;
   collect caveats in one section (Limitations, Known Issues) instead of
   sprinkling a disclaimer into every paragraph; and never write instructions
   into the product — nor the process: "do not mention X" means X is absent
   (not "we do not address X"), and intermediate errors, abandoned approaches
   and revision history are not content either. Lead with the strongest
   result — a paper is a launch, not a progress report. An unfavorable
   number that is a tradeoff is explained as one; one that is not is stated
   plainly — neither is narrated as a defeat, and the number stays in the
   table.
8. Momentum is part of the deliverable. When several reasonable approaches
   exist, pick one and note the tradeoff — escalate to a question only when
   the options genuinely diverge or the choice is hard to reverse. A detail
   that does not block the goal gets recorded, not solved first. Stalling to
   avoid picking wrong is itself a wrong pick.
9. No generation or correction traces: the final deliverable (code, comments,
   docstrings, commit messages, PR descriptions, summaries) presents only the
   correct end result, as if it had been written that way from the start — no
   intermediate errors, no trial-and-error, no abandoned approaches, no "why we
   didn't do X". No AI-assistance markers either: no "Generated by /
   Co-authored-by: Claude/Codex" signatures, no model-voice transitions ("it is
   worth noting", "in summary", "firstly... secondly... finally"), no "here
   is..." openers. Match the wording and level of detail to the project's
   existing style.

Shapes already seen, for calibration. Examples, not a checklist — a real finding
is not dismissed by resembling one:

  H  hashing every row of two spreadsheets to answer what comparing cells answers
  H  writing checksum files that nothing ever reads
  E  hardening the accounts of an app that has no users and no deployment
  R  auditing your own patch all night while the feature stays unwritten
  R  a reviewer that returns a failing verdict on everything
  O  guards whose justification is the previous guard, not the requirement

And two that look like the above and are not. Report these:

  ✓  a digest that lets you skip re-reading a large file you already have
  ✓  a rare-looking input this project's own documentation example produces

Before running any check, answer: what specific failure would this detect, and
what would I do differently if it occurred? No answer means do not run it.

Say plainly when something is correct. Do not manufacture findings.
