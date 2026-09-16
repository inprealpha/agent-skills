# Agent skills

Personal agent skills for engineering, review, investigation, and verification.

## Install

Use the [skills CLI](https://github.com/vercel-labs/skills):

```sh
npx skills add inprealpha/agent-skills
```

List the available skills without installing:

```sh
npx skills add inprealpha/agent-skills --list
```

Install one skill:

```sh
npx skills add inprealpha/agent-skills --skill simplify-code
```

## Skills

| Skill | Description |
| --- | --- |
| [architect](skills/architect/SKILL.md) | Design caller usage, interfaces, data types, and module ownership before implementing a change. |
| [blast-radius](skills/blast-radius/SKILL.md) | Assess what a change could break beyond its diff and test the assumptions its safety depends on. |
| [create-verification-skill](skills/create-verification-skill/SKILL.md) | Create executable project verification instructions with a feature map and retained evidence. |
| [hillclimb](skills/hillclimb/SKILL.md) | Improve one measurable outcome through isolated hypotheses, repeated measurements, and regression checks. |
| [how](skills/how/SKILL.md) | Explain a subsystem through traced runtime flow, data ownership, and concrete code references. |
| [interrogate](skills/interrogate/SKILL.md) | Adversarially review a change and deliver a prioritized verdict grounded in reachable failures. |
| [maintain-verification-skill](skills/maintain-verification-skill/SKILL.md) | Audit a project verification skill against current source and observed application behavior. |
| [orchestrate-work](skills/orchestrate-work/SKILL.md) | Coordinate delegated engineering work from a request through implementation, integration, and review. Use when managing several related tasks or workers, especially when they share decisions or code. Handle small changes directly when delegation adds no useful independence. |
| [reflect](skills/reflect/SKILL.md) | Extract durable lessons from a work session and route them to focused skill or tooling improvements. |
| [review-loop](skills/review-loop/SKILL.md) | Iterate on a deliverable through fresh-context subagent reviews and fixes until no material findings remain. Use when the user wants repeated independent review, with autonomous progress or user checkpoints tailored to their preference. |
| [simplify-code](skills/simplify-code/SKILL.md) | Simplify code when asked to review over-engineering or apply cleanup, including redundant tests and avoidable dependencies. Preserve behavior; keep unrelated feature work and general correctness reviews outside this skill's scope. |
| [skill-evaluation](skills/skill-evaluation/SKILL.md) | Compare skill variants on realistic tasks with controlled inputs and evidence-based scoring. |
| [why](skills/why/SKILL.md) | Investigate the history and rationale behind code, with cited facts and explicit uncertainty. |

Skill instructions and required supporting files are in `skills/`. Harness support depends on the tools available in the current agent environment; cross-harness behavior has not been comprehensively tested.

## Attribution

Adapted upstream material retains its MIT license notices within each skill directory:

- `architect`, `blast-radius`, `create-verification-skill`, `hillclimb`, `how`, `interrogate`, `maintain-verification-skill`, `reflect`, `skill-evaluation`, and `why`: [pstack by Lauren Tan](https://github.com/cursor/plugins/tree/f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d/pstack), revision `f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d`.
- `orchestrate-work` and `review-loop`: selected procedures and writing guidance from [Matt Pocock skills](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills), revision `3cca18b368ae95cdbdebbff572ccafa662551015`.
- `simplify-code`: [Ponytail by DietrichGebert](https://github.com/dietrichgebert/ponytail/tree/356918eba965ee1eac64bd3a7f0dd02108350de5), revision `356918eba965ee1eac64bd3a7f0dd02108350de5`.

No additional repository-wide license is specified for original contributions.
