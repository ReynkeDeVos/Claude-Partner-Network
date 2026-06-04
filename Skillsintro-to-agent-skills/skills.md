# Skills

## What are skills?

- Personal skills go in `~/.claude/skills` and follow you across all projects. Project skills go in `.claude/skills` inside a repository and are shared with anyone who clones it.
- Skills load automatically. no need for the `/` command.
- format:

```md
---
name: pr-review
description: Reviews pull requests for code quality. Use when reviewing PRs or checking code changes.
---
```

## Creating your first skill

Priority for name conflicts: Enterprise → Personal → Project → Plugins

1. Enterprise — managed settings, highest priority (`managed-settings.json`)
2. Personal — your home directory (`~/.claude/skills`)
3. Project — the `.claude/skills` directory inside a repository
4. Plugins — installed plugins, lowest priority (`project/.claude=plugin/plugin.json`)

```bash
mkdir -p ~/.claude/skills/pr-description && touch ~/.claude/skills/pr-description/SKILL.md
```

## Configuration and multi-file skills

### Fields

name & description are required. The other ones are optional.

- name: max. 64ch
- description: What does the skill do? When should Claude use it? Max 1024ch
- allowed-tools `Read, Grep, Glob, Bash`: Restricting useage of tool.s Like only **reading** files.
- model: Specifies which Claude model to use for the skill.

### Progressive disclosure

**SKILL.md should be >= 500 lines!**

Then reference the sub-md files in your main file via `[]()`

- SKILL.md
  - assets/: Images, templates, or other data files
  - scripts/: Executable code - Scripts execute without loading their contents into context
  - references/: Additional documentation

## Skills vs. other Claude Code features

When CLAUDE.md? always-on project standards

- Project-wide standards that always apply
- Constraints like "never modify the database schema"
- Framework preferences and coding style

When SKILL.md? task-specific expertise that loads on demand

- Task-specific expertise
- Knowledge that's only relevant sometimes
- Detailed procedures that would clutter every conversation
- You want to enhance Claude's knowledge for the current task
- The expertise applies throughout a conversation
- Knowledge that informs how Claude handles requests
- Guidelines that affect Claude's reasoning

When subagents? isolated execution contexts for delegated work

- You want to delegate a task to a separate execution context
- You need different tool access than the main conversation
- You want isolation between delegated work and your main context

When hooks? automated operations triggered by events

- Operations that should run on every file save
- Validation before specific tool calls
- Automated side effects of Claude's actions

When MCP? external tools and integration

## Sharing Skills

- git/GitHub - greate for teams/projects
- plugins
- enterprise settings
- build-in subagents (Explorer, Plan, Verify) do not see skills, but custom created ones can do.
  - Add to name, description, etc also `skills: xxx` Then the skill gets always loaded in thsi subagent, not on demand
  - `~/.claude/agents` or `/agents`

## Troubleshooting skills
