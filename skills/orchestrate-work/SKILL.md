---
name: orchestrate-work
description: Coordinate delegated engineering work from a request through implementation, integration, and review. Use when managing several related tasks or workers, especially when they share decisions or code. Handle small changes directly when delegation adds no useful independence.
---

# Orchestrate work

Own the requested outcome across investigation, clarification, implementation, and review. Give workers bounded assignments and continue until the integrated result satisfies the request, or a specific dependency requires the user's input.

Use this skill as the coordinator. Workers receive an assignment and the relevant engineering guidance, rather than running another copy of the orchestration workflow.

## Establish the work

Read the request, repository instructions, current Git state, and relevant existing decisions. Preserve the user's scope, preferences, and authorization. Find facts in the repository or other available sources before asking the user. Reuse established project terminology.

Determine which other workflows are active in the same repository. Use one coordinator for their shared decisions, assignments, and integration. Join an existing coordinator through an explicit handoff when possible. If another session's ownership cannot be established, investigate without writing to its possible scope until ownership is resolved. A note on a different branch does not reserve a file.

This first version supports one coordinator and its participating workers. Independent coordinators need a shared mechanism that grants exclusive ownership and handles abandoned work. Do not claim that this skill provides that mechanism.

Choose a local directory for the active work record that every participating worker can read and that is outside their separate worktrees. The coordinator is its only writer. Record the coordinator identity and repository, requested outcome, current assignments, accepted decisions, open questions, and integration state. Follow [Coordination](references/coordination.md) when creating assignments, recording decisions, or resuming work.

Use the tools available in the current environment. For Codex delegation, read [Codex execution](references/codex.md). Model choices and tool names belong in that reference or the current assignment, not in the shared procedure. If delegation is unavailable, perform the tasks sequentially and report that limit.

## Resolve the decisions that affect the next work

Workers send facts, uncertainties, and proposed decisions to the coordinator. The coordinator checks prior answers and pending questions by meaning and scope, combines duplicates, and asks the user when needed. Carry one answer to all affected assignments.

Choose routine, reversible implementation details that follow the repository's conventions. Ask when an unresolved choice materially changes product behavior, scope, cost, or an expensive architectural commitment; when accepted requirements conflict; or when only the user can supply access or judge the result. An instruction to complete the task does not grant unrelated permissions.

For each question, explain the concrete choice, your recommendation and its consequence, and which work needs the answer. Ask related questions together when their answers are independent and the set is easy to respond to. Avoid reopening accepted choices without new evidence or changed scope.

Ask a consequential design question before implementing work that depends on it. Prepare a concrete result before asking for subjective review or permission for an external action. Reuse existing authorization. A required answer pauses only dependent work; continue other useful assignments. Silence is not an answer or permission.

Stop clarifying when the next assignment has enough information to implement and verify its intended behavior. An exhaustive interview is appropriate only when the user asks for that exercise.

## Assign and run the work

Describe small, independently verifiable outcomes. Use [Engineering procedures](references/engineering.md) for implementation, testing, and review. Split work when the assignments can make useful progress independently; keep tightly coupled changes together. A mechanical change across many callers may need an initial compatible interface, caller migrations, then removal of the old interface.

Before dispatch, check both dependencies and ownership. An assignment can run when its prerequisites are integrated, required decisions are settled, its edit scope is assigned, and its shared interfaces and resources are compatible with other active work. Investigation can start earlier against an identified snapshot.

Give each implementation worker a separate branch and worktree from an explicit commit. Include the current assignment revision, allowed edits, relevant decisions, verification requirements, and return destination. Workers may inspect other files but must report newly required edits or incompatible assumptions before changing outside their assignment. Give shared documents, interfaces, and resources a named owner. Resolve overlap by assigning a common prerequisite, transferring ownership after a handoff, combining tasks, or sequencing them.

Read worker messages as work progresses. When a decision or shared interface changes, identify affected assignments, pause dependent edits, and send updated instructions. Require acknowledgment before treating a running worker as aligned. Preserve completed work while deciding what can still be used.

## Integrate and review

Use one writer for the integration branch. A worker's result is ready for integration when its changes are committed, its actual diff fits the assignment, and it reports its assignment revision, relevant decision revisions, checks run, and remaining issues. Compare those revisions with the current record before applying the result. Reconcile stale results against the current decisions and revalidate affected behavior; a passing check under an earlier answer is insufficient. Keep a worker's uncommitted or unreviewed work available until its disposition is known.

Integrate one result at a time. Reconcile the intent of overlapping changes and check behavior that crosses task boundaries, even when Git merges cleanly. Compare the combined result with the request and accepted decisions. A prerequisite becomes available to dependent implementation after integration and the relevant checks, not merely after a worker says it is finished.

Give reviewers an immutable candidate commit and explicit comparison base, plus the request and applicable standards. Commit local candidate changes before a commit-based review; otherwise provide a complete immutable patch that includes staged, unstaged, and new files. Verify which candidate was reviewed. Reviewers return evidence and proposed fixes without editing the candidate.

Combine findings that describe the same cause, retaining their evidence and requirement links. Prioritize consequences and assign bounded fixes. Recheck affected behavior and review material changes after fixes. A review does not require implementing every stylistic suggestion.

Finish when the integrated candidate meets the acceptance criteria, required checks pass, and material review findings are resolved. Prepare any authorized delivery, and request missing authorization only for the concrete action that needs it. Report the result, checks actually run, and remaining limitations. Remove temporary worktrees only after their work is integrated or explicitly accounted for. Leave a resumable record if external input prevents completion.
