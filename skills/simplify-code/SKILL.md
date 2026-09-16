---
name: simplify-code
description: Simplify code when asked to review over-engineering or apply cleanup, including redundant tests and avoidable dependencies. Preserve behavior; keep unrelated feature work and general correctness reviews outside this skill's scope.
---

# Simplify code

Reduce maintenance effort while preserving required behavior. Leave reasonable code alone; clarity matters more than brevity.

## Establish the scope

Use the named files or change under review; inspect relevant callers and tests to understand their contracts. Expand to the whole repository only when requested. If neither a target nor a current change is identifiable, ask for the target rather than inventing a broad cleanup.

Review requests produce findings without edits. Cleanup requests authorize focused edits and verification without another approval step. Preserve existing user changes. Include generated code, vendored tools, agent assets, or unrelated configuration only when specifically requested.

## Choose changes with evidence

For each candidate, identify what makes it unnecessary and what behavior must survive. Prefer, in order, removing functionality that is demonstrably unused and not contractual, reusing existing code, and using an appropriate standard-library, platform, or installed-dependency feature. Write custom code when those do not fit the actual requirements.

Look for redundant wrappers, dead options, repeated logic, and speculative flexibility. A single caller, one implementation, or one exported symbol is not by itself evidence of waste: boundaries can support testing, ownership, or external consumers. Check usage and contracts before removing them; report uncertainty when usage cannot be established.

Prefer readable control flow and cohesive files over one-liners or abstractions introduced only to reduce repetition. Preserve public interfaces, boundary validation, error handling, security, accessibility, and supported runtimes, including relevant edge cases of replacements. Claim runtime improvements only with evidence.

## Judge tests by what they catch

Keep tests that protect distinct behavior or regressions. Before removing or consolidating a test, establish that its meaningful coverage remains elsewhere or that the behavior it asserted is intentionally obsolete. Tests coupled to implementation details may need rewriting to assert behavior rather than deletion.

Reuse existing test infrastructure. Add or adjust focused tests for meaningful coverage gaps, with effort proportional to risk rather than a test quota. Preserve assertions that catch real failures; a failing test calls for diagnosis, not removal to make cleanup pass.

## Work with the project's tooling

Read the applicable lint, formatter, typecheck, and test configuration; use it as the source of truth, including locally customized anti-slop rules when present. Anti-slop is optional and separately managed; leave its installation and rule maintenance outside cleanup.

Preserve comments explaining invariants, constraints, or required type-assertion safety. Simplification must not disable rules, add suppressions, fabricate type evidence, or remove validation to obtain a clean lint result. Do not add schema libraries or dependency-injection frameworks just to accommodate a cleanup idea. If a candidate needs a policy or architecture decision beyond the request, leave that candidate unchanged, explain the specific tradeoff, and continue other useful work.

## Verify and finish

After edits, run relevant existing checks and repository-required checks, including formatter/lint checks when formatting changes. Distinguish pre-existing failures from new ones where possible; repair or undo your own changes that break required behavior. Report unavailable checks as unverified.

Review is complete when each finding has a location, evidence, and a concrete replacement, or the inspected scope has no supported findings. Rank by practical value.

Cleanup is complete when the final diff stays within scope, each edit has a behavior-preserving rationale, and check results or limitations are reported. Summarize useful changes and unresolved risks briefly, then stop. An unchanged result is valid; there is no deletion target.

Adapted from [Ponytail](https://github.com/dietrichgebert/ponytail), copyright (c) 2026 DietrichGebert, under the [MIT license](LICENSE). Source revision: `356918eba965ee1eac64bd3a7f0dd02108350de5`.
