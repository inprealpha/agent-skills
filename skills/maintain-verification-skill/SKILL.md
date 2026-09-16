---
name: maintain-verification-skill
description: "Audit a project verification skill against current source and observed application behavior."
disable-model-invocation: true
---

# Maintain a verification skill

Audit the specified verification skill and feature map. Requires its project and
runtime tools. Edit only that skill's directory and owned helpers; report product
regressions separately. A request to audit alone produces findings; apply repairs
when the user requested maintenance or corrections.

1. **Establish coverage.** Locate the target skill and read its launch and cleanup
   instructions. Reconcile the feature index with its files. Identify new user
   surfaces from concrete source paths. If several targets fit, resolve the target
   before editing.
2. **Check source.** For every mapped feature, trace entry points and compare the
   documented behavior, prerequisites, and driver handles to the implementation.
   Record likely drift with citations and a concise live recipe. Combine overlapping
   recipes without losing distinct entry points. Source inspection cannot mark a
   live recipe as passed.
3. **Drive the app.** Follow its launch model and exercise every mapped feature.
   One agent owns a shared instance; use isolated sessions where the driver requires
   them. Health-check before driving and after surprising behavior. Reset a wedged
   UI even if the process is healthy. Capture evidence outside cleanup targets and
   clean failed-run residue before retrying. An unavailable feature gets its attempted
   route and missing prerequisite recorded as blocked, not passed.
4. **Classify differences.** Outdated instructions are documentation drift. Working
   behavior with unusable driving steps is a harness gap. A real product failure is
   a regression to report, not a reason to rewrite the expected behavior. Repair
   authorized documentation and helper problems within scope, then re-drive affected
   paths. If the intended behavior is uncertain, record the disagreement instead of
   treating the current implementation as the specification.
5. **Close the run.** Tear down owned resources and verify evidence still exists.
   Report each feature as passed, failed, or blocked with evidence, corrections made,
   and remaining product issues. Call the map clean only if all required coverage
   completed successfully. Publication or PR creation follows the user's task scope;
   a local maintenance request does not require a PR.
