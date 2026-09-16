---
name: architect
description: "Design caller usage, interfaces, data types, and module ownership before implementing a change."
disable-model-invocation: true
---

# Architect

Settle the shape of a non-trivial change before filling in implementation.
Requires repository reading; executable prototypes need the project's runtime.
Respect the requested deliverable: a design-only request ends with a design;
continue into implementation when the user already requested it.

1. **Ground the constraints.** Trace affected entry points, data flow, ownership,
   and existing contracts. Check history when a proposed boundary change might
   discard an intentional constraint. Finish with named requirements, invariants,
   and unresolved decisions rather than a list of files.
2. **Write the caller first.** Sketch one realistic usage example, then derive the
   types, signatures, error results, and module responsibilities needed to support
   it. Make ownership and lifetime explicit. Parse untrusted data at boundaries and
   represent meaningful states in the domain model. Keep sketches outside production
   paths unless an implementation step explicitly needs a scaffold.
3. **Compare shapes where it matters.** For a consequential unsettled boundary,
   produce at least two structurally different candidates and compare caller effort,
   hidden complexity, migration cost, and verification. A settled mechanical change
   can use one sketch with a reason. One agent can generate alternatives; independent
   candidates are optional when available and authorized.
4. **Review the interface.** Look for callers coordinating internal stages, the same
   policy duplicated across modules, meaningless forwarding layers, or mutable state
   shared without a domain reason. Prefer a boundary that owns a coherent decision.
   Apply these as design questions, not unconditional bans on adapters or wire types.
5. **Choose and verify.** Deliver the usage, shape, decision rationale, rejected
   alternatives, and a concrete way to test the main invariant. Compile or exercise a
   small prototype when it resolves an empirical uncertainty. Label untested sketches.
   If implementation is authorized, fill in the chosen shape and verify behavior.
   Repeated workarounds of the same kind are a signal to revisit ownership or types;
   revise only the affected design, preserving unrelated work.

Honor an explicitly requested checkpoint. A design must not quietly broaden the
feature or turn every minor edit into an architecture project.
