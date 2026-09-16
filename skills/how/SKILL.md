---
name: how
description: "Explain a subsystem through traced runtime flow, data ownership, and concrete code references."
disable-model-invocation: true
---

# How

Build a working mental model of the requested code or subsystem. Requires reading
and search access. This workflow explains current behavior; historical motivation
needs evidence from history or documents rather than inference from code.

1. **Bound the question.** Identify the subsystem and the user's purpose: onboarding,
   debugging, reviewing, or deciding where a change belongs. Use conversation context
   to choose depth. Start directly for a narrow question.
2. **Trace a real path.** Follow a representative trigger from entry point to result.
   Read the relevant implementations and tests. Track data transformations, state
   ownership, asynchronous boundaries, errors, cancellation, and cleanup where they
   affect the explanation. Finish with a trace that connects the observable outcome
   to actual code, not just symbol names.
3. **Resolve boundaries.** For placement or layering questions, identify which module
   owns the state or invariant and which consumers depend on it. Explain why a proposed
   location fits that responsibility, separating the current arrangement from advice.
4. **Explain at useful depth.** Lead with what the subsystem does. Introduce the few
   concepts needed to follow the trace, then walk through the flow in plain language.
   Cite concrete files or symbols, include important gotchas and a small file map when
   useful, and use a diagram only when it makes relationships easier to follow.
5. **Calibrate the account.** Resolve contradictory source readings before delivery.
   Label behavior inferred from source versus observed in execution. Name unavailable
   components or remaining gaps. End when the bounded question is answered; avoid an
   exhaustive tour of unrelated code.

For a large subsystem, independent exploration of separate paths is optional when
available and authorized. Reconcile the returned paths against source before using
those findings in the explanation.
