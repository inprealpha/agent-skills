---
name: craft
description: Simplify writing, documentation, code, architecture, interfaces, and creative work so people can quickly understand and use it. Use for “AI slop,” confusing or overcomplicated output, project reviews, and making the current result ready to share or ship. Not an AI detector.
---

# Craft

Aim for the simplest complete, usable result at the requested scope. People should quickly understand its purpose, use it, and judge whether it is right. Include maintainers and reviewers as audiences of software. Apply this lens while creating as well as reviewing; the user should not need to supply it again.

Generating more code, documentation, logs, or polished prose is cheap. Their volume is not value. Spend effort removing unnecessary concepts, arranging information where people expect it, and making important behavior visible. Reduce the complexity of the whole task, rather than moving it out of sight.

## Ground the work

Read or experience the artifact in its intended form. Identify who it serves, what they need to know or accomplish, and their likely starting point. Use the user's examples, constraints, and corrections as evidence of taste. Honor the genre and requested voice; plain explanatory writing and an expressive creative brief have different jobs. Ask only when missing context would materially change the work.

When craft is invoked without a narrower assignment, simplify and improve the active artifact or project identified by context. For a project, inspect its relevant documentation, code, architecture, and user paths together rather than polishing only the current file. If no target is identifiable, ask for it. Explicit review-only requests produce findings; explicit narrow requests keep their scope. Preserve useful conventions and avoid unrelated cleanup. Preserve supported behavior, contracts, facts, distinctions, and uncertainty. Before changing observable behavior, establish that the request and actual requirements call for it; convenience or an inferred ideal contract is insufficient.

## Investigate enough to judge

Scale investigation to uncertainty, consequence, and breadth. A clear local wording fix may need only the artifact. An unfamiliar domain, large project, disputed design, repeated workaround, or surprising result may warrant further research. Size suggests wider sampling and independent investigation; it does not prescribe a ritual.

Start with requirements, behavior, tests, history, decisions, and local conventions. If they cannot settle a consequential question, consult authoritative documentation, mature comparable implementations, original research, or relevant practitioner analysis. State the question, read enough evidence and exceptions to answer it, and apply the answer to this project's constraints. Stop once the question is resolved. When evidence is unavailable, distinguish an open question from a demonstrated defect.

Calibrate success against actual requirements and credible alternatives, not just your first draft or implementation. A large relative speedup can still leave a poor algorithm. For performance claims, inspect the approach and compare equivalent workloads and contracts, measuring where feasible. For other artifacts, use comparisons when they resolve meaningful uncertainty. Report what was actually checked; do not imply an unperformed benchmark or user study.

Treat configured quality rules as local policy. Opinionated anti-slop rules can supply examples when present; they are not universal laws or a reason to install tooling.

## Recognize recurring failures

Treat “AI slop” as a quality complaint, not a diagnosis of authorship. Investigate these patterns with evidence from the artifact:

- **Appearance without substance:** polished prose, impressive architecture labels, or finished-looking screens conceal unsupported claims or incomplete tasks.
- **Volume without hierarchy:** boilerplate, exhaustive lists, repeated caveats, or development logs bury what the person needs now.
- **Compression without understanding:** jargon, unexplained names, dense expressions, or omitted steps make the reader reconstruct meaning.
- **Generality without a present need:** interchangeable copy, speculative options, forwarding layers, or frameworks obscure the specific subject or actual behavior.
- **Parts without a coherent whole:** sections, modules, or screens disagree about terms, ownership, state, or workflow.
- **Reassurance without evidence:** confident summaries, generic comments, passing checks, or test counts replace inspectable behavior and meaningful limitations.

These also occur in human work. Familiar conventions, AI origin, or a disliked word do not establish a defect. Name the obstacle and consequence; do not fill every category or manufacture findings.

## Simplify the human's path

- **Writing and documentation:** Use plain, standard English, concrete terms, and direct sentences. Favor easy comprehension over prose flourishes or compressed jargon. Lead with what this reader needs. Make the README a user entry point: purpose, fit, prerequisites, and a meaningful first use. Keep contributor workflows, implementation walkthroughs, deep reference, and development history out of the README; link to task-oriented documentation where useful. Separate user and maintainer material even in a small project. Retain development records only when they have ongoing value; discard redundant process output within scope. Group related information serving the same task, and avoid multiple documents doing the same job. Verify instructions and examples against actual behavior.
- **Code:** Trace input through decisions, state changes, side effects, and output. Prefer direct control flow, domain names, and simple abstractions a maintainer can grasp quickly. Remove unnecessary indirection or options when their removal reduces total complexity. Keep important rules and invariants near the code that owns them. Comments should explain useful intent or constraints; tests should expose meaningful behavior and failure rather than echo implementation.
- **Architecture:** Can a contributor explain the main path, locate a rule, and predict where a change belongs? Trace responsibilities, dependencies, state ownership, and failure propagation. Simplify boundaries that scatter one decision or make callers coordinate internal stages. A layer earns its place by hiding relevant complexity or protecting a real contract; a single caller or extra file alone does not make it wasteful.
- **Interfaces and products:** Perform the primary task with realistic content and relevant states, including natural follow-ups such as investigating a surprising total. Simplify choices and hierarchy. Check whether controls, labels, feedback, and recovery help the person finish. Surface polish and a successful build do not establish usability.
- **Creative work:** Let the subject, medium, constraints, and intended experience drive specific choices. Explore alternatives when direction is uncertain, then choose for a reason. Useful conventions may stay; novelty and decoration are not substitutes for purpose.

For a project review, start at the reader's entry point and trace representative workflows across docs, implementation, and tests, including an important failure or recovery path. Compare the documented mental model with actual behavior. Locate hidden assumptions and places that require juggling unrelated files or translating inconsistent concepts. Report inspection and sampling limits.

## Improve and deliver a usable increment

Prioritize by human effort and consequence. A finding needs a location, concrete evidence, the task or judgment it obstructs, and a proportionate remedy. Connect complexity to what it obscures: a rule, ownership decision, error, or change risk. Separate verified defects, open questions, and taste preferences.

Resolve the cause rather than explaining around it. Prefer clear structure, cohesive ownership, direct logic, and specific language. Keep necessary complexity understandable. Concision means less work for the reader, not the fewest words, files, or lines. Use prose, tables, diagrams, or interaction when they reduce that work. Craft can use specialized tools when helpful but does not depend on another skill.

At each stage, leave a coherent result ready for its intended audience to use, share, or ship at the current scope. Keep development narration out of user-facing surfaces. Complete the promised slice, give it a clear entry point, remove unfinished placeholders from that slice, and state meaningful limits plainly. Resolve actual blockers; future enhancements and hypothetical completeness should not keep usable work in perpetual development. Readiness means finishing this scope, not inventing further launch requirements or stricter contracts. It does not authorize publication or deployment beyond the request.

Inspect the result as its audience encounters it: read the rendered page, follow the instructions, trace the code, or perform the task. Verify claims and behavior touched by edits with appropriate existing checks. Can a person explain the central path and recognize its important limits? Passing checks alone cannot answer that.

When uncertainty warrants independent review and delegation is available and authorized, give fresh reviewers the artifact, audience, constraints, and a focused comprehension, usability, or coherence question. Require evidence and consequences; reconcile feedback with intent and recheck affected areas.

Finish a review with actionable findings and stated coverage and verification limits. Finish improvements when the current slice is usable and understandable, identified obstacles are resolved, and further changes lack a specific benefit worth their cost. Report meaningful changes and unverified limits briefly. Leave sound work alone; do not promise universal appeal.
