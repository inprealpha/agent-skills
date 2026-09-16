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

A useful question: “What mistakes do you expect me to make—the ones you'd look for
if you were reviewing this yourself?” Use those anticipated failure modes to guide
both the work and the reviewers' focus.

After that, proceed autonomously. If the user says **no questions**, infer reasonable
defaults and begin. If they want to **stay involved**, bring them consequential
choices and return to them when the loop hits a snag or starts repeating itself.
Otherwise, reserve interruptions for blockers you cannot resolve within the agreed
scope. Follow any effort limits the user sets.

## Work, review, repeat

Do the work, then spawn a reviewer with a fresh context. Give it the user's intended
outcome, the relevant artifacts, and the review perspective—not the full conversation
or your argument for why the work is good. Use multiple reviewers in parallel when
the complexity warrants distinct perspectives; one reviewer can cover several sides
of a smaller task.

Evaluate the feedback, make worthwhile fixes, and send the updated work to newly
spawned reviewers. Adjust their prompts as the work evolves while keeping the user's
outcome fixed. Reviews should examine the result as a whole, not just confirm that
previous comments were addressed.

Finish when a fresh review of the current result has no unresolved major findings
and the work meets the agreed outcome. Optional polish need not keep the loop alive.
If reviews stop producing progress, change the approach or report the blocker;
stalling or reaching an effort limit is not convergence.
