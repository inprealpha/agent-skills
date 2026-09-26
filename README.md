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
| [craft](skills/craft/SKILL.md) | Improve writing, design, products, or creative work that feels generic, low-effort, hard to parse, or like “AI slop,” grounding choices in the audience's needs. Not an AI detector or a general code-cleanup workflow. |
| [create-verification-skill](skills/create-verification-skill/SKILL.md) | Create executable project verification instructions with a feature map and retained evidence. |
| [hillclimb](skills/hillclimb/SKILL.md) | Improve one measurable outcome through isolated hypotheses, repeated measurements, and regression checks. |
| [how](skills/how/SKILL.md) | Explain a subsystem through traced runtime flow, data ownership, and concrete code references. |
| [interrogate](skills/interrogate/SKILL.md) | Adversarially review a change and deliver a prioritized verdict grounded in reachable failures. |
| [maintain-verification-skill](skills/maintain-verification-skill/SKILL.md) | Audit a project verification skill against current source and observed application behavior. |
| [orchestrate-work](skills/orchestrate-work/SKILL.md) | Coordinate substantial work through decomposition, parallel execution, and fresh perspectives. Use for separable workstreams, research/design informing implementation, or requested team workflows. |
| [reflect](skills/reflect/SKILL.md) | Extract durable lessons from a work session and route them to focused skill or tooling improvements. |
| [review-loop](skills/review-loop/SKILL.md) | Finish work through repeated fresh-context reviews and fixes. Use when the user wants an autonomous review loop after a brief alignment on the outcome and review perspectives. |
| [simplify-code](skills/simplify-code/SKILL.md) | Simplify code when asked to review over-engineering or apply cleanup, including redundant tests and avoidable dependencies. Preserve behavior; keep unrelated feature work and general correctness reviews outside this skill's scope. |
| [skill-evaluation](skills/skill-evaluation/SKILL.md) | Compare skill variants on realistic tasks with controlled inputs and evidence-based scoring. |
| [why](skills/why/SKILL.md) | Investigate the history and rationale behind code, with cited facts and explicit uncertainty. |

Skill instructions and required supporting files are in `skills/`. Harness support depends on the tools available in the current agent environment; cross-harness behavior has not been comprehensively tested.

## Attribution

Adapted upstream material retains its MIT license notices within each skill directory:

- `architect`, `blast-radius`, `create-verification-skill`, `hillclimb`, `how`, `interrogate`, `maintain-verification-skill`, `reflect`, `skill-evaluation`, and `why`: [pstack by Lauren Tan](https://github.com/cursor/plugins/tree/f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d/pstack), revision `f5bdd6826fd0a0d9cbc4347134c3a74a200b9d9d`.
- `orchestrate-work` and `review-loop`: selected procedures and writing guidance from [Matt Pocock skills](https://github.com/mattpocock/skills/tree/3cca18b368ae95cdbdebbff572ccafa662551015/skills), revision `3cca18b368ae95cdbdebbff572ccafa662551015`.
- `simplify-code`: [Ponytail by DietrichGebert](https://github.com/dietrichgebert/ponytail/tree/356918eba965ee1eac64bd3a7f0dd02108350de5), revision `356918eba965ee1eac64bd3a7f0dd02108350de5`.

`craft` is original work and includes a notice preserving the existing policy: no additional license is granted. No additional repository-wide license is specified for original contributions.
