---
name: interrogate
description: "Adversarially review a change and deliver a prioritized verdict grounded in reachable failures."
disable-model-invocation: true
---

# Interrogate

Review the requested diff or artifact against its intended outcome. Deliver a
verdict; apply fixes only when implementation is also requested. Requires the
artifact and surrounding context; execution strengthens uncertain findings.

1. **Define scope and intent.** Identify the requested revisions, working-tree
   changes, and relevant constraints. Derive the intended behavior from the user's
   request, specification, or PR. Resolve uncertainty that would change the verdict
   before classifying behavior as a bug.
2. **Challenge the change.** Inspect correctness, failure paths, boundary validation,
   compatibility, state ownership, test coverage, and maintainability where relevant.
   For each proposed finding, name the trigger, reachable path, observable consequence,
   and precise location. Distinguish introduced failures from pre-existing issues.
3. **Check the findings.** Trace real callers and guards, and run a small meaningful
   reproducer where affordable. A hypothetical input is not a reachable bug without
   supporting evidence. A suggested abstraction needs a concrete benefit in this
   scope. Keep valuable rationale comments; comment removal is not a quality metric.
4. **Judge and prioritize.** Deduplicate and classify supported findings as act on,
   consider, or contextual. Dismiss incorrect or purely stylistic claims with a brief
   reason when they were material to the review. A single verified severe finding
   outweighs reviewer agreement. Avoid quotas on either findings or dismissals.
5. **Deliver the verdict.** Lead with actionable findings ordered by impact, each
   with a source location, trigger, consequence, and evidence or verification gap.
   Explain material tradeoffs and disagreements. If there are no supported findings,
   say so and state the review's coverage limits without inventing issues.

If the task requests independent reviewers and the harness supports them, give
reviewers the same intent and context before they see each other's conclusions.
Verify their reports yourself. Multiple opinions are optional evidence-gathering;
consensus is not proof, and sequential passes by one agent are not independent.
