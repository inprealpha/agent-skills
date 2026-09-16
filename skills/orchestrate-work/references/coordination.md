# Coordination

Use a small active work record with one coordinator writer. Its location must be shared by participating workers, rather than copied into each worker’s workspace. The record describes ownership; it does not enforce locks against independent sessions.

Keep current assignments, answers, and status together, and keep prior events in a separate history section. Update the current entries when they change so a resumed reader does not have to infer which of several conflicting states applies.

## Assignments

Record these details when they apply:

- Task identity, requested outcome, acceptance criteria, owner, and assignment revision.
- Input versions or snapshots, output locations, permitted write paths, and explicitly excluded shared artifacts. For code changes, record the base commit, branch, and worktree.
- Dependencies and the accepted results that make them available.
- Accepted decision references and their revisions; shared interfaces or behavior the task assumes.
- Shared resources, such as a database, service account, build output, or listening port, and who may change them.
- State, outstanding questions, last acknowledged revision, result locations or versions, checks run, and remaining issues.

Use states with clear meanings: planned, waiting for a decision or prerequisite, running, ready for integration, integrated, and complete. Add a state only when it changes what someone should do. Distinguish a stopped worker from completed work.

The assignment is current execution information. Keep the durable ticket focused on desired outcome; working paths and input versions belong in the assignment and can be updated after inspection.

Send workers this instruction with their task:

> Work within the assigned edits and accepted decisions. Look up facts before raising a question. Send unresolved choices, proposed shared document changes, and requests for additional edit scope to the coordinator. Report evidence and the work affected. Continue useful work that does not depend on the answer. Return your assignment revision, relevant decision revisions, result locations and versions, changed artifacts, checks actually run, and unresolved concerns. Do not ask the user independently, change shared decision records, integrate other workers’ outputs, or expand the assignment yourself.

## Questions and decisions

For an open question, record the choice being made, its scope, known facts, options, recommendation, and affected tasks. Match existing questions by meaning and scope before creating another. Similar words can describe different decisions; do not combine them if the governing requirements differ.

For an answer, record the decision, who supplied it or the evidence supporting an agent choice, the scope where it applies, its revision, and affected tasks. Keep proposed and accepted decisions distinguishable. If an answer changes, retain the earlier context and mark what supersedes it.

An answer in one conversation becomes usable by another worker when the coordinator sends it or the worker reads and acknowledges the updated assignment. A record that another worker has not seen is insufficient for synchronization.

## Shared documents

The coordinator owns canonical glossary and decision record changes, or assigns one specific editor. Workers submit proposals with supporting evidence. Check existing records before creating a new one and link all relevant tasks to the same decision.

Record a glossary term when it resolves ambiguity that affects the work. Follow existing document locations and formats. Create a decision record when the choice has meaningful reversal cost, a future reader would need its rationale, and real alternatives were considered. Routine answers can stay in the work record.

Allocate decision record identities centrally. Separate workers can otherwise create conflicting identifiers or duplicate records for the same decision.

## Overlap and changes

Separate working copies protect local files. They do not isolate tracker edits, shared databases, services, or incompatible decisions. Assign those resources explicitly or avoid concurrent mutations.

Before granting additional edits, check other assignments and their read dependencies. Two workers can edit different files while relying on incompatible versions of the same interface. Choose a common contract and communicate it, or sequence the dependent changes.

When a worker reports unexpected changes in its workspace, preserve them and identify their source. Do not discard or overwrite another actor's work to restore the expected state. Stop affected edits until ownership and the base are understood.

## Resume, failure, and handoff

On resume, read the work record, current artifacts and workspace state, accepted decisions, and recent worker results. Reconcile them before dispatch. Verify that an apparently abandoned worker has stopped before transferring its edits or shared resources. Preserve its working copy and unfinished changes until they have been inspected.

A new coordinator needs an explicit handoff from the previous owner, or evidence that it has stopped and a reconciliation of outstanding work. Do not infer exclusive ownership from an old timestamp alone.

Before accepting a resumed worker's result, compare its assignment revision and decision assumptions with the current ones. Revalidate affected behavior against the integration candidate. Keep unrelated completed work rather than restarting the whole workflow.
