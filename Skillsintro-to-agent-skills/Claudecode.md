# Claude Code usage

## Adding Context

### Create memory

Firstly

```bash
> /init
```

Summarize findings in `CLAUDE.md`

### Save in memory

`Shift + Tab` for auto-accept creating/mutating of files

`CLAUDE.md` per project

`CLAUDE.local.md` -> not on GitHub, only for personal instructions

`~/.claude/CLAUDE.md` -> Global file for ALL projects.

### Memory

```bash
> /memory
```

This opens one of the files and you add your isntructions:

```txt
Use comments sparingly. Only comment complex code.
```

### Mention files

```bash
> How does the auth system work? @src/components/auth/AuthDialog.tsx? @src/hooks/use-auth.ts @...
```

```bash
/memory

> The database schema is defined in the @prisma/schema.prisma file. Reference it anytime you need to understand the structure of data stored in the database
```

### AGENTS.md

add @AGENTS.md on the first line of your CLAUDE.md, and Claude will load the contents of that file first.

## Making changes

`CTRL + V` for Screenshots!

### Planning Mode

`Shift + Tab` toggle or `/plan`

Open plan in Editor with `Ctrl + G`

### Effort level

`CTRL + O` to toggle reasoning

```bash
> /effort
```

changes thinking level

## Cotrolling context

`ESC` to escape the current response.

For example, when claude makes the same msitake again, and again.

```bash
> /memory
```

or edit `CLAUDE.md` directly, to add a note about the correct approach

### Rewinding Conversations

When conversations accumulate irrelevant context.

```bash
> /rewind
```

With this you can jump back to a previews message & continue from there.

### Context Management Commands

```bash
> /compact
```

summarizes your entire conversation history while preserving the key information Claude has learned. This is ideal when:

- Claude has gained valuable knowledge about your project
- You want to continue with related tasks
- The conversation has become long but contains important context

```bash
> /clear
```

starts a new conversation with fresh context. This is most useful when:

- You're switching to a completely different, unrelated task
- The current conversation context might confuse Claude for the new task
- You want to start over without any previous context

```bash
> /resume
```

to go back to a previous conversation. `/clear` doesn't delete conversations

### Creating Custom Commands

In `.claude` directory in project, add directory `commands` & add file `audit.md`

```md
1. Runs npm audit to find vulnerable installed packages
2. Runs npm audit fix to apply updates
3. Runs tests to verify the updates didn't break anything
```

restart claude code & run

```bash
/audit
```

### Commands with Arguments

`write_tests.md`

```md
Write comprehensive tests for: $ARGUMENTS

Testing conventions:

- Use Vitest with React Testing Library
- Place test files in a **tests** directory in the same folder as the source file
- Name test files as [filename].test.ts(x)
- Use @/ prefix for imports

Coverage:

- Test happy paths
- Test edge cases
- Test error states
```

`$ARGUMENTS` is a placeholder!

```bash
> /write_tests the use-auth.ts file in the hooks directory
```

## MCP servers

```bash
claude mcp add playwright npx @playwright/mcp@latest
```

### Managing Permissions

`.claude/settings.local.json`

```json
{
  "permissions": {
    "allow": ["mcp__playwright"],
    "deny": []
  }
}
```

`mcp__playwright`: This allows Claude to use the Playwright tools without asking for permission every time.

```bash
> Navigate to localhost:3000, generate a basic component, review the styling, and update the generation prompt at @src/lib/prompts/generation.tsx to produce better components going forward
```

## GitHub integration

```bash
> /install-github-app
```

The generated pull request adds two GitHub Actions to your repository. Once merged, you'll have the workflow files in your `.github/workflows` directory.

### Mention in GH PR

write `@claude`

## Hooks

Run command before or after claude code does sth. Optionally, block claude's action

- Global - `~/.claude/settings.json` (affects all projects)
- Project - `.claude/settings.json` (shared with team)
- Project (not committed) - `.claude/settings.local.json` (personal settings)

Write them **by hand** or by using command

```bash
> /hooks
```

PreToolUse: before a tool is called, PostToolUse: after a tool is called

`matcher`: before `Read` tool is executed, run this `command`

```json
"PreToolUse": [
  {
    "matcher": "Read",
    "hooks": [
      {
        "type": "command",
        "command": "node /home/hooks/read_hook.js"
      }
    ]
  }
],
"PostToolUse": [
  {
    "matcher": "Write|Edit",
    "hooks": [
      {
        "type": "command",
        "command": "node /home/hooks/edit_hook.js"
      }
    ]
  }
]
```

- Code formatting - Automatically format files after Claude edits them
- Testing - Run tests automatically when files are changed
- Access control - Block Claude from reading or editing specific files
- Code quality - Run linters or type checkers and provide feedback to Claude
- Logging - Track what files Claude accesses or modifies
- Validation - Check naming conventions or coding standards

## Stop claude code to read your `.env` file

```bash
> List out the names of all the tools you have access to, bullet point list.
```

`.claude/settings.local.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Read",
        "hooks": [{ "type": "command", "command": "node $PWD/hooks/read_hook.js" }]
      }
    ]
  }
}
```

`hooks/read_hook.js`

```js
process.stdin.setEncoding('utf8');
let input = '';
process.stdin.on('data', (d) => (input += d));
process.stdin.on('end', () => {
  const toolArgs = JSON.parse(input);
  const readPath = toolArgs.tool_input?.file_path || '';
  if (readPath.includes('.env')) {
    console.error('You cannot read the .env file');
    process.exit(2);
  }
  process.exit(0);
});
```

```bash
> Read my .env file!
```

In general:

```json
"PostToolUse": [ // Or "PreToolUse" or "Stop", etc
  {
    "matcher": "*",
    "hooks": [
      {
        "type": "command",
        "command": "jq . > post-log.json"
      }
    ]
  },
]
```

## Claude SDK

```zsh
npm install @anthropic-ai/claude-agent-sdk
```

`touch index.mjs`

```mjs
import { query } from '@anthropic-ai/claude-agent-sdk';

const prompt = 'List the files in the current directory';

for await (const message of query({ prompt })) {
  console.log(JSON.stringify(message, null, 2));
}
```

By default it has only `read`. You can give it more tools:

```mjs
for await (const message of query({
  prompt,
  options: { allowedTools: ['Read', 'Glob'] },
})) {
  // ...
}
```
