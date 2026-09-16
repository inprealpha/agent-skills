---
name: reflect
description: "Extract durable lessons from a work session and route them to focused skill or tooling improvements."
disable-model-invocation: true
---

# Reflect

Turn observed workflow failures, repeated corrections, or successful techniques
into small durable improvements. Use the current conversation or a user-provided
session record. Broader history needs an explicit relevant scope and an available
history capability; use a digest when raw transcripts are unavailable.

1. **Collect evidence.** Identify concrete decisions, corrections, failed attempts,
   and outcomes. For each potential lesson, cite the event or artifact and describe
   the consequence. Distinguish an explicit user preference from an inferred pattern.
   A one-off workaround is not automatically a universal rule.
2. **Find the cause.** Ask whether the problem was missing knowledge, an unclear
   trigger, an instruction that was ignored, inadequate tooling, or a wrong check.
   A skill that was already correct and followed does not need another instruction.
3. **Choose the smallest home.** Prefer a test, lint, script, type, or runtime check
   for an enforceable invariant. Use skill prose for judgment and workflow guidance.
   Tighten a description only for an observed discovery failure, and preserve explicit
   user-only invocation. Create a new skill only for a distinct reusable workflow
   that does not fit an existing one.
4. **Draft focused changes.** Present the evidence, proposed destination, small diff,
   expected benefit, and how to verify it. Keep accepted proposals, rejected lessons,
   and unresolved ideas distinct. Resolve conflicts with existing guidance rather
   than appending another rule. Stay within the current project's authorized scope.
5. **Apply within authorization.** If the user already asked to update the relevant
   skills or tooling, apply those scoped changes and verify them. A request merely
   to reflect produces proposals for review. Report proposed external backlog items
   locally unless filing them was requested. Preserve applicable licenses when adapting
   material and keep installation separate from authoring.

Deliver the few durable lessons and exact changes or proposals, with evidence and
remaining uncertainty. Independent review can add perspective when authorized and
available; it is not required to learn from a single session.
