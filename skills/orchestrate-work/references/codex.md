# Codex execution

This reference describes the Codex tools available during this adaptation. Inspect the current tool descriptions before using them; availability and arguments can differ between environments. This is an execution reference, not a claim that the skill has been tested in every Codex interface.

- Use the collaboration subagent tools for workers belonging to the current task. Give each worker its concrete assignment and relevant references; include the engineering reference for engineering work. A child working in another Git worktree still needs the absolute worktree path in its assignment; delegation alone does not isolate files.
- Use `spawn_agent` for a new bounded assignment, `send_message` for updates to a running worker, and `followup_task` to resume an idle worker. Use `interrupt_agent` when dependent edits must stop, then inspect and reconcile its result. Follow the current tool documentation for status and waiting.
- For engineering work, use `exec_command` for Git worktree operations and repository checks. Pin the base commit before creating worker branches. Keep a single writer for integration.
- Use `request_user_input_async` for missing information when available, and continue independent work while waiting. Respect the tool's limits and the current environment's authorization rules.
- Keep the work record in a shared local directory outside worker working copies. Give workers its absolute path and require them to send proposed updates to the coordinator.

Use the configured model and reasoning settings unless the user or applicable instructions specify an override. Do not create sidebar tasks as a substitute for subagents unless the user asks for separate tasks.

If a required capability is unavailable, state the limitation and perform the work sequentially when that still meets the request. Installation, plugin activation, hooks, publishing, and deployment require their own task authorization; loading this authoring skill does not request them.
