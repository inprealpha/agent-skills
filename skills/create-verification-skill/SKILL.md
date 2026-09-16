---
name: create-verification-skill
description: "Create executable project verification instructions with a feature map and retained evidence."
disable-model-invocation: true
---

# Create a verification skill

Build a project-specific skill that a fresh agent can use to launch the app,
exercise observable behavior, capture evidence, and clean up. Requires repository
access and the tools needed to run and drive the project.

1. **Discover the real workflow.** Inspect project commands, existing tests, routes,
   CLI help, and setup documentation. Identify the user surface, launch command,
   readiness signal, authentication, fixtures, and isolation options. Prefer an
   existing driver over adding a new stack. Resolve only setup issues within the
   requested scope; report unavailable prerequisites precisely.
2. **Choose an authoring destination.** Use the requested location, or a repository
   skill-authoring directory outside harness discovery paths. Generation does not
   install or activate a skill. Record required tools by capability and the actual
   commands or selectors available in this project.
3. **Write the runnable instructions.** Produce a SKILL.md with name and description
   frontmatter and these operational parts:
   - Launch and readiness, including isolated data, ports, or sessions.
   - A read-only health check that confirms the expected build, instance, and auth.
   - Driving steps using real commands, routes, or stable UI handles.
   - Evidence: action, resulting state, relevant side effects, and durable paths.
   - Cleanup of only processes and scratch state created by this run. Keep evidence
     outside cleanup targets. Track process ownership rather than killing by name.
   Document helper invocations and required dependencies. Add the user-only
   invocation metadata below to the generated authoring files.
4. **Map features.** Add a features/README.md index and one file per selected feature.
   Start with a small representative set, normally three to five if that many exist.
   For each, record prerequisites, user entry points, driving steps, literal expected
   observations, evidence, and known limits. Label unexercised recipes unverified.
5. **Execute one complete path.** Follow the generated instructions cold: launch,
   health-check, drive one mapped feature through its real user interface, assert
   its expected outcome, capture evidence, clean up, and confirm evidence survives.
   Capture side effects as well as visible output. Check what a dry run actually
   skips before relying on it. Use test resources for external effects. Clean failed
   attempts before retrying and re-exercise any corrected helper.

Deliver the generated paths, the command or action tested, observed result, and
coverage limits. If setup or execution is blocked, deliver a clearly marked draft
and name the missing prerequisite. One passing feature validates that path; it
does not mark the entire feature map verified.

## Generated invocation metadata

Preserve user-only invocation in both supported packaging formats: add
`disable-model-invocation: true` to the generated SKILL.md frontmatter for Claude
Code, and create `agents/openai.yaml` containing
`policy: {allow_implicit_invocation: false}` for Codex. Keep these settings separate
from the generated operational instructions. If the user requests a different
invocation policy, honor that explicitly. Other harnesses may ignore these fields;
record their enforcement as untested rather than promising universal suppression.
