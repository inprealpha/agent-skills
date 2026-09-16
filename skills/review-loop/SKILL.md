---
name: review-loop
description: Iterate on a deliverable through fresh-context subagent reviews and fixes until no material findings remain. Use when the user wants repeated independent review, with autonomous progress or user checkpoints tailored to their preference.
---

# Review loop

Own the work and its verification. Use new reviewers to challenge the current result,
evaluate their feedback, fix supported problems, and repeat. This applies to code,
documents, plans, and other reviewable deliverables; choose evidence appropriate to
the work. Reviewer agreement alone does not establish correctness.

## 1. Set the working agreement

Infer the intended outcome, acceptance criteria, scope, and involvement preference
from the request and available context. Resolve factual gaps by inspecting the work.
Keep clarification limited to decisions that change the next work.

- **Default:** promptly ask only the few missing questions whose answers materially
  affect the outcome or autonomous execution. If none are needed, begin. Thereafter
  make routine decisions and return to the user for consequential unresolved choices,
  blockers, or stalled progress.
- **Autonomous:** minimize interruptions and choose reasonable, reversible defaults.
  This alone does not prohibit a necessary question.
- **No questions:** do not ask clarification questions. State consequential
  assumptions and proceed within the authorized scope. If an indispensable decision
  or permission is missing, complete independent work and report the blocked part
  without guessing authorization.
- **Keep me involved:** ask at meaningful decision points, before committing to
  consequential alternatives, and when blocked or repeating failed approaches. Offer
  a concrete recommendation and explain what depends on the answer. Do not ask about
  every mechanical fix. Honor any cadence the user specifies.

Combine these preferences where possible; an explicit no-questions instruction takes
precedence over optional check-ins. Previously supplied answers and permissions carry
forward. Continue independent work while an essential answer is pending; silence is
not an answer. None of these modes grants additional permission to publish, deploy,
send messages, or otherwise expand the task.

When asking, group independent questions into one short round, each with a recommended
answer and its consequence. Defer questions that depend on an unanswered choice. Ask
about decisions the user needs to own; resolve implementation details yourself. A
clean review or routine fix needs no approval checkpoint unless the user requested one.

Begin execution once the outcome, constraints, and next action are clear; leave only
work dependent on an essential answer pending. State a compact plan, acceptance
criteria, and review budget. Honor user-specified
time, cost, and round limits. Otherwise use an initial limit of five review rounds
and stop sooner on convergence or a stall. A round reviews one candidate, whether
with one reviewer or several. Reaching a limit is a checkpoint, not success; do not
silently extend it. Explicit instructions to continue until convergence override the
default round limit, but do not justify repeating a stalled approach indefinitely.

## 2. Prepare and review a candidate

Do the requested work, or inspect the existing deliverable if the assignment starts
with review. Run proportionate checks before requesting review. Keep a compact work
record of the criteria, candidate versions, checks, findings and dispositions, and
remaining budget; a conversation record suffices for short loops.

Use the harness's actual subagent facility. Each round needs newly created reviewers
with fresh context, not resumed reviewers or a copy of the coordinator's conversation.
Supply only the task, constraints, relevant source artifacts, and review assignment.
Prefer precise artifact paths or links over copying large documents into prompts;
confirm each reviewer can access them. Include essential requirements directly when
the source is inaccessible from the review context.
If independent contexts are unavailable, disclose that limitation; do not present
self-review as independent review. In no-questions mode, do useful available checks
and report the unmet independence requirement.

Start with one reviewer. Use multiple reviewers concurrently when distinct concerns
warrant independent attention, such as correctness and integration, usability and
accessibility, or factual support and argument quality. Give each a bounded lens and
enough common context to judge the whole outcome. Add a reviewer only when their
perspective or coverage provides useful independence.

Give all reviewers in a round the same stable candidate. Use a commit, snapshot,
export, or unchanged working state and identify it in the assignment. Include new
files and relevant surrounding context, not just a partial diff. Keep the candidate
unchanged until the reviews finish; if it changes, reconcile or repeat affected
reviews before counting them. Reviewers inspect and report; the coordinator owns
edits. Reviewers do not launch their own review loops.

Construct each review prompt from these elements:

> Review [candidate and location] against [user outcome and acceptance criteria].
> Inspect [source artifacts and relevant context], focusing on [lens and likely
> failure modes]. Check the artifacts directly; do not rely solely on the author's
> summary. Do not edit them or delegate further. Return actionable findings with
> severity, precise location, evidence or reproduction, practical impact, and a
> suggested correction. Distinguish material defects from optional polish. Report
> checks actually performed, coverage limits, and uncertainty. Return only supported
> findings; a review with no material findings is a valid result.

Keep success criteria stable across rounds. Adapt the lens and questions to changed
areas, evidence gaps, and newly discovered risks. Later reviews should check both
fixes and their wider consequences. Preserve independence by letting a fresh reviewer
assess the result before consulting earlier conclusions; then supply specific prior
findings when needed to verify their closure. Keep prompts neutral and disputed
findings visible during reconciliation. Ensure the final review covers the overall
criteria as well as the last patch.

Before dispatch, confirm that the candidate is identifiable, the review inputs are
accessible, and each acceptance criterion has an assigned reviewer or verification
check. A missing formal spec is not itself a reason to interrupt: the user's request
and established constraints can supply the criteria. Resolve any material ambiguity
according to the working agreement.

## 3. Evaluate, fix, and repeat

Wait for assigned reviews or record incomplete coverage. Deduplicate findings by
underlying cause. A material finding threatens acceptance criteria, correctness,
reliability, usability, or another explicit requirement; stylistic preferences alone
do not block completion unless style is part of the requirement.

Verify findings against the artifacts. Accept supported findings, reject unsupported
ones with reasons, and investigate uncertain ones. Resolve reviewer disagreement
through evidence or a targeted check. Keep each material concern open until evidence
resolves it, even when other reviewers missed it.

Implement accepted fixes within scope, run relevant checks, update the work record,
and request another fresh review of the revised candidate. Optional polish need not
cause another round. Any material edit after a clean review requires affected checks
and fresh review before claiming convergence.

Keep progress updates consistent: name the round, summarize material findings and
their disposition, and state the next action. Provide updates at meaningful changes;
updates are not requests for permission. Keep detailed reviewer exchanges in the work
record and bring the user only the decisions their involvement preference calls for.

Track repeated findings, reopened decisions, and oscillating fixes. Two consecutive
rounds without material progress, or recurrence of the same underlying blocker after
attempted fixes, is a stall: diagnose it and change the approach rather than merely
rephrasing the review prompt. Under default or involved modes, bring the concrete
tradeoff to the user. Under no-questions mode, take an evidence-supported alternative
within scope if available; otherwise stop with an honest blocker report.

## 4. Finish or hand back control

Convergence means a complete fresh review round on the latest candidate finds no
unresolved material issues, acceptance criteria are met, and required checks pass.
One such round is sufficient; endless unanimous approval is not required. Missing
review coverage, failed checks, and uncertainty that prevents assessing a material
requirement cannot be counted as clean results.

If the budget ends, progress stalls, or required input is unavailable, distinguish
that outcome from convergence. Leave the current result and remaining work resumable.
Report what changed, rounds and review lenses used, verification actually performed,
unresolved findings or limitations, and the reason the loop ended. Do not claim the
result is defect-free or compatible with harnesses that were not exercised.
