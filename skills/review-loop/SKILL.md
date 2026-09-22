---
name: review-loop
description: Finish work through repeated fresh-context reviews and fixes. Use when the user wants an autonomous review loop after a brief alignment on the outcome and review perspectives.
---

# Review loop

The user wants finished work, improved through independent scrutiny without having
to manage each review round.

## Align first

Ask a few quick questions up front only where the request leaves meaningful choices:
what does a good result look like, and which perspectives should the reviews cover?
For software, consider both technical quality and product behavior or UX; let the
user's priorities determine the emphasis. Offer a sensible default instead of an
open-ended interview. If the answers are already clear, start working.

Infer likely failure modes from the work. When alignment would help, briefly offer
your view of what to watch for and invite corrections or additions. Adapt this to
the project and what the user has already said; skip it when priorities are clear.
Use those anticipated failure modes to guide both the work and the reviewers' focus.

After that, proceed autonomously. If the user says **no questions**, infer reasonable
defaults and begin. If they want to **stay involved**, bring them consequential
choices and return to them when the loop hits a snag or starts repeating itself.
Otherwise, reserve interruptions for blockers you cannot resolve within the agreed
scope. Follow any effort limits the user sets.

## Work, review, repeat

Do the work, then spawn a reviewer with a fresh context. Give it the user's intended
outcome, constraints, relevant artifacts, and review perspective—not the full
conversation, other reviewers' verdicts, or your argument for why the work is good.
Use multiple reviewers in parallel when distinct perspectives warrant it; one can
cover several sides of a smaller task. Keep review coordination with the main agent;
reviewers should not recursively recruit more reviewers.

Match review evidence to the concern: visual reviewers inspect the rendered artifact,
usability reviewers exercise the relevant flows, and engineering reviewers examine
implementation and meaningful checks. Ask for concrete findings with evidence, user
impact, and what they could not inspect. Missing access or verification is a coverage
gap, not a clean approval. If fresh-context delegation is unavailable, report that
limitation; self-review does not establish independent convergence.

Evaluate the feedback, make worthwhile fixes, and send the updated work to newly
spawned reviewers. Resolve disagreement against the user's outcome and observable
evidence, not a vote; do not make changes merely to satisfy a reviewer. Adjust prompts
as the work evolves while keeping the user's outcome fixed. Reviews should examine
the current result as a whole, not just confirm that previous comments were addressed.

Finish when a fresh review of the current result has no unresolved material findings or
material coverage gaps and the work meets the agreed outcome. Optional polish need
not keep the loop alive.
If reviews stop producing progress, change the approach or report the blocker;
stalling or reaching an effort limit is not convergence.
