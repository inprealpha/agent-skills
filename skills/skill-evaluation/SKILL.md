---
name: skill-evaluation
description: "Compare skill variants on realistic tasks with controlled inputs and evidence-based scoring."
disable-model-invocation: true
---

# Skill evaluation

Evaluate whether an instruction change improves observable agent behavior.
Requires a way to run fresh agent sessions and inspect their artifacts. A static
review is useful when that capability is missing, but is not a behavioral trial.

1. **Define the comparison.** Name the candidate change, baseline, and intended
   behavioral improvement. Choose a small set of realistic tasks, including a case
   that should not trigger the skill where invocation behavior is under evaluation.
   Write a rubric with concrete observable criteria before running anything.
2. **Control the inputs.** Compare variants using the same model and configuration,
   task input, starting project state, tool access, and resource limits. Treat model
   changes as a separate experiment. Use fresh isolated sessions to avoid transfer
   from one variant to another. Record skill content hashes and environment details.
3. **Keep expectations out of the task.** Give each runner an ordinary user request
   and only the artifacts needed to perform it. Keep the judge rubric, expected
   result, other outputs, and variant identities outside runner-visible paths. Use
   neutral project names and sanitized output labels; avoid instructions asking the
   runner to claim it followed particular rules. Explicit-use tests may name the
   skill. Discovery tests must use the harness's real discovery mechanism.
4. **Run and retain evidence.** Capture final artifacts, executable check results,
   errors, and any available scoped tool trace. Repeated trials help distinguish
   instruction effects from variation. Decide the affordable trial count before
   examining results; explain later changes to the experiment. Keep timeouts and
   failed attempts in the results rather than silently dropping them.
5. **Score and inspect.** Prefer objective checks for observable behavior. A judge
   sees sanitized outputs on one rubric, without variant or model identity. Inspect
   actual files and check claimed results. Tool traces can establish whether a skill
   was read; self-report cannot. When traces are absent, mark that criterion unknown.
6. **Recommend.** Report the setup, per-task results, regressions, resource cost where
   available, and uncertainty. A small trial provides bounded evidence, not universal
   superiority or cross-harness compatibility. Recommend keep, revise, or inconclusive
   against the original criteria. Retain an exact mapping from labels to variants
   outside runner-visible resources so the experiment can be audited.

Controlled validation does not authorize installing skills for everyday use or
modifying unrelated harness settings. If isolation or independent sessions are
unavailable, deliver the prepared experiment and its specific execution blocker.
