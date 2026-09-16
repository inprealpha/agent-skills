---
name: blast-radius
description: Assess what a change could break beyond its diff and test the assumptions its safety depends on.
disable-model-invocation: true
---

# Blast radius

Review the requested change beyond its immediate callers. Produce supported
risks, cleared concerns, and executable evidence for the critical assumptions.
Requires repository reading and search; execution is needed for runtime proof.

1. **Anchor the change.** Identify the requested diff or proposed behavior, its
   base revision, and any working-tree edits included. Read surrounding code and
   tests until you can describe the behavioral change, including implicit changes
   to defaults, ordering, ownership, or error handling.
2. **Trace hidden contracts.** Follow relevant consumers across serialization,
   storage, language boundaries, feature flags, and lifecycle timing. Inspect the
   actual pinned dependency source and local patches when behavior depends on a
   library. Caller search alone does not establish coverage. Name the important
   paths you inspected and any unavailable consumers.
3. **Name the safety assumptions.** Identify the few facts on which the change's
   safety depends. For each, describe a concrete failure if it is false. Keep
   plausible, consequential risks; resolve speculative concerns by reading or
   running the relevant path rather than padding the report.
4. **Challenge those assumptions.** Use the cheapest meaningful executable check
   that calls the real implementation. Where useful, contrast the base and changed
   revisions against the same expected behavior. Confirm failures are caused by
   the suspected behavior, not setup. Run in an isolated scratch location when a
   probe mutates state; retain its commands, result, and evidence path. A source
   argument is still useful when execution is unavailable, but label it unproven
   at runtime. Code changes require an implementation request.
5. **Deliver the assessment.** Explain the change, each critical assumption and
   its evidence, confirmed risks with file/line references and failure conditions,
   concerns checked and cleared, and the smallest remaining pre-merge check.
   Distinguish source-supported, executed, and observed-in-app evidence. Report
   missing coverage explicitly; a clean local probe does not prove all consumers
   safe.

For a broad review, use independent reviewers only when available and authorized.
Verify their findings against the actual code and evidence. A single agent can
complete this workflow; repeated passes are not independent review.
