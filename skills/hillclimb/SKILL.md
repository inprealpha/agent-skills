---
name: hillclimb
description: "Improve one measurable outcome through isolated hypotheses, repeated measurements, and regression checks."
disable-model-invocation: true
---

# Hillclimb

Improve a measured outcome while preserving correctness. Requires a reproducible
workload, measurement tools, and authority to edit the target. Use for sustained
optimization; match the effort to the user's target and resource budget.

1. **Ground the metric.** Reproduce the reported problem on a realistic workload.
   Name the metric, direction of improvement, constraints, and checkable stopping
   target. Establish a bounded time or attempt budget from the request or state a
   reasonable initial budget before beginning. If the workload cannot reproduce the
   problem, improve the reproduction before optimizing.
2. **Validate measurement.** Use one repeatable command and enough samples to estimate
   noise. Confirm the harness distinguishes meaningfully different workloads. Record
   the baseline and passing correctness checks, then keep workload and measurement
   settings fixed. A necessary harness correction invalidates earlier comparisons:
   re-baseline and explain the change.
3. **Run one hypothesis at a time.** Name the mechanism expected to improve the metric,
   make a bounded change in an isolated branch or scratch copy, measure under the same
   conditions, and run relevant regression checks. Keep only changes with a supported
   benefit and preserved behavior; revert only the experiment's own edits otherwise.
   Inspect artifacts yourself when experiments are delegated. Parallel attempts need
   separate state and uncontended measurements.
4. **Record each decision.** Keep a compact local log: hypothesis, change, baseline,
   result, sample variability, regression outcome, keep/revert decision, and evidence
   path. Preserve failed attempts so the next hypothesis can use them. A simplification
   that holds performance may be valuable; label it a simplification rather than a
   measured speed improvement.
5. **Stop and verify.** Stop at the target, budget, a material blocker, or diminishing
   returns after plausible alternatives were considered. Keep the original success
   criteria intact and report an unmet target honestly. Rerun the final accepted state
   against the baseline workload and correctness checks. Keep accepted changes
   reviewable; commits and publication follow the user's requested scope.

Report baseline to final, variability and measurement method, accepted changes,
rejected attempts, evidence paths, and any remaining promising hypothesis. An
unmeasured intuition or a gain smaller than noise is not an established win.
