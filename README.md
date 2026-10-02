# Agent skills

Personal agent skills for engineering, review, investigation, and verification.

## Repository structure

Keep `skills/` as the shared source for all agents and environments. Individual
skill installers such as `npx skills` use those folders directly. The portable
`plugin.json`, Codex compatibility manifest in `.codex-plugin/`, and marketplace
catalog in `.agents/plugins/` add distribution formats without moving or copying
the skill sources.

A future Claude Code plugin can add its own manifest and marketplace metadata
pointing to the same `skills/` directory. Keep host-specific packaging outside
the skills, preserve each skill's existing invocation metadata, and avoid forks
or generated copies of skill instructions for each host. This change packages
Codex distribution; it does not replace individual skill installation or add a
Claude Code plugin installer.

## Install as a Codex plugin

This repository is also the plugin: `inprealpha-agent-skills`, in the `inprealpha`
marketplace. The existing `skills/` directory is the single source of truth; plugin
packaging does not change skill behavior, licenses, or invocation policies.

In a current Codex CLI:

```sh
codex plugin marketplace add inprealpha/agent-skills --ref main
codex plugin add inprealpha-agent-skills@inprealpha
```

Start a new chat after installation. In the desktop Plugins Directory, select the
`inprealpha` source and install **Abir's Agent Skills** if you prefer the UI.
To refresh it later, run `codex plugin marketplace upgrade inprealpha`
and start a new chat.

### Use in Codex Cloud

Installing a local marketplace does not by itself provision cloud sessions.
Choose the route your account supports:

**Workspace plugin:** A workspace admin can open **Admin > Plugins > Add > Import
marketplace**, enter `https://github.com/inprealpha/agent-skills`, leave Path empty,
and set Branch to `main`. Import and make the plugin
available to your role. Install/enable it, then start a new cloud task and check
that its skills are available. The bundle contains no MCP servers or desktop hooks.

**Cloud project setup:** If workspace import is unavailable, ask the environment
setup agent to install the same skill folders into your target project's
`.agents/skills/`. Add this repository to the environment, then run:

```sh
python3 /path/to/agent-skills/scripts/install_cloud_skills.py --project /path/to/your-project
```

Replace those paths with the actual cloud checkout paths. Alternatively, from the
target project root, use this setup snippet (requires Python 3, Git, and GitHub
network access):

```sh
skills_checkout="$(mktemp -d)"
git clone --depth 1 --branch main https://github.com/inprealpha/agent-skills.git "$skills_checkout" &&
python3 "$skills_checkout/scripts/install_cloud_skills.py" --project "$PWD"
```

Publish/republish the prepared environment and start a new task in that project.
For reproducible environments, use a reviewed commit rather than following the
moving branch. The helper copies every supporting file and license, accepts an
identical repeat install, and refuses differing existing skills before copying
anything. It does not overwrite or remove project skills; review conflicts when
upgrading. This is repository skill discovery, not a cloud marketplace install.

### Invoke and verify

Select a skill with `@` where the UI supports it, or `$skill-name` in Codex CLI.
For a first check, ask: “Use the architect skill to propose a design for this
change; read its SKILL.md first and keep this request design-only.” Check that the
agent actually reads the installed skill. Ten skills preserve explicit-only
invocation through `agents/openai.yaml`; `craft`, `orchestrate-work`, `review-loop`,
and `simplify-code` retain automatic discovery.

The plugin supplies instructions, not capabilities: delegation, browser control,
connected services, and project runtimes must be available in the cloud session.
It does not include personal `config.toml`, credentials, conversation history, or
global `AGENTS.md`. Avoid installing duplicate standalone and plugin copies in the
same session. Cloud import and runtime behavior must be verified in your workspace.

Official references: [plugin packaging](https://developers.openai.com/plugins/build/plugins),
[workspace GitHub import](https://learn.chatgpt.com/docs/enterprise/plugin-management),
[skill discovery](https://learn.chatgpt.com/docs/build-skills), and
[cloud environments](https://learn.chatgpt.com/docs/environments/cloud-environments).

### Validate and build an uploadable ZIP

Run these commands from a repository checkout. Development dependency: Python
3.10+ and `PyYAML==6.0.2`. The cloud setup helper uses
only the Python standard library. CI validates packaging, tests the setup helper,
and publishes a ZIP artifact on each push or pull request.

```sh
python3 -m pip install PyYAML==6.0.2
python3 scripts/package_plugin.py --output dist/inprealpha-agent-skills.zip
python3 -m unittest discover -s tests -v
```

The ZIP puts manifests and `skills/` at its root, includes the cloud setup helper,
and excludes Git history, build tooling, CI files, and marketplace metadata.
Existing per-skill license notices are retained; this
package does not grant a new repository-wide license.

## Install individual skills

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
| [craft](skills/craft/SKILL.md) | Simplify writing, documentation, code, architecture, interfaces, and creative work so people can quickly understand and use it. Use for “AI slop,” confusing or overcomplicated output, project reviews, and making the current result ready to share or ship. Not an AI detector. |
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
