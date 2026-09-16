# Engineering procedures

Use the parts that fit the assignment. These procedures do not independently ask the user, publish documents, or manage other workers.

## Isolate and integrate code changes

Inspect repository instructions and current Git state before assigning edits. Give each implementation worker a separate branch and worktree from an explicit base commit. Keep the shared work record outside worker worktrees and use one writer for the integration branch.

Accept results when changes are committed, the actual diff fits the assignment, and the worker reports its assignment and decision revisions, changed files, checks, and remaining issues. Preserve uncommitted work until its disposition is known. Integrate sequentially and check cross-task behavior even when Git merges cleanly. A broad caller migration may need a compatible interface first, caller updates next, then removal of the old interface.

Give reviewers an immutable candidate commit and explicit comparison base. Commit local candidate changes before a commit-based review; otherwise provide a complete immutable patch including staged, unstaged, and new files. Remove temporary worktrees only after their work is integrated or accounted for.

## Investigate and specify

Read the relevant code and existing requirements. For a bug, try to reproduce the reported behavior and record the result. If a runnable reproduction is unavailable, inspect the code and other evidence to narrow the cause; say what remains unverified.

Describe the current behavior, requested behavior, and acceptance criteria. Include the cases needed for the agreed scope. Carry existing testing and design decisions forward instead of requesting them again. Ask the coordinator about a missing choice only when it changes what should be built or how success will be assessed.

Prefer a small end-to-end change that can be verified independently. For a broad mechanical migration, preserve compatibility while changing callers when practical. Shared prerequisites must be integrated before dependent implementation uses them.

## Implement and test

Follow the repository's conventions and choose tests that can detect the requested failure or missing behavior. Test observable behavior through suitable interfaces. Expected results should come from the requirements, independently worked examples, or known correct data, rather than recomputing the implementation in the assertion.

For a behavior change where test-first work is useful, write a failing test, verify that it fails for the intended reason, then implement enough to pass. Refactor when that improves the change while preserving passing tests. Use existing test interfaces when they fit; selecting a routine test location does not require another user confirmation.

Preserve useful existing tests. Before replacing tests, check which behaviors they protect and whether the replacement still detects those failures. Private or lower-level tests can be justified when they protect behavior that broader tests do not adequately cover.

Run focused checks during the change. Run the repository's required checks on the integrated candidate, including behavior that spans assignments. Expand testing when changed behavior or new evidence warrants it. Report commands and observed outcomes; distinguish checks that passed, failed, or could not run.

## Review

Review against an explicit base and immutable candidate. Include the request, accepted decisions, applicable repository standards, and relevant check results. Check that the candidate includes the work intended for review, including changes that were uncommitted before candidate capture.

Independent reviewers can examine requirements and engineering correctness when both passes are useful. Report concrete failure cases, missing requirements, and material risks with file evidence. Distinguish required fixes from optional design suggestions. Look beyond text conflicts for incompatible assumptions between tasks.

Return findings to the coordinator. It combines duplicate causes and assigns fixes, preserving the evidence from each review. The coordinator verifies that the final result still matches the requested behavior after integration and fixes.
