# Concision

Concision is an agent skill for clear writing and explanations. It helps an AI assistant find the real question, write for the intended audience, and keep the detail needed to understand or act.

Concision is the outcome of understanding, not a word-count contest.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Validate package](https://github.com/franciscoh017/concision/actions/workflows/validate.yml/badge.svg)](https://github.com/franciscoh017/concision/actions/workflows/validate.yml)
[![Install on skills.sh](https://img.shields.io/badge/skills.sh-install-000000.svg)](https://skills.sh/franciscoh017/concision/concision)

## Example

**Before**

> I just wanted to reach out to provide a quick update regarding the current status of the launch. At this point in time, we are still waiting for the security review to be completed, which means that we will need to move the launch from Tuesday to Thursday. Could you please let me know whether this revised timing works for you by Monday?

**After**

> We're moving the launch from Tuesday to Thursday while we wait for the security review. Please confirm by Monday whether Thursday works for you.

The change, reason, and requested action remain. In explanations and technical documentation, Concision keeps definitions, causal reasoning, examples, and prerequisites when readers need them.

## Installation

### Skills CLI

Install with the [Skills CLI](https://github.com/vercel-labs/skills). Its [current package requirements](https://github.com/vercel-labs/skills/blob/main/package.json) specify Node.js 22.20.0 or newer. You also need npm (for `npx`) and Git to install from this repository.

```bash
npx skills add franciscoh017/concision
```

The CLI detects installed agents and may prompt you to choose one. Use `--agent` to select a specific agent:

```bash
# Codex
npx skills add franciscoh017/concision --agent codex

# Claude Code
npx skills add franciscoh017/concision --agent claude-code

# Cursor
npx skills add franciscoh017/concision --agent cursor
```

These commands install in the current project. Add `--global` to install for your user account instead. Add `--skill concision` to select the skill explicitly.

### Claude Code plugin

Run these commands inside Claude Code:

```text
/plugin marketplace add franciscoh017/concision
/plugin install concision@concision
```

Invoke the plugin skill as `/concision:concision`. If your Claude Code version cannot load the plugin, use the Skills CLI installation above.

### Other agents and manual installation

For other supported agents, use the appropriate `--agent` value from the [CLI's supported-agent list](https://github.com/vercel-labs/skills#supported-agents). For a runtime without CLI support, download or clone this repository and copy the whole skill directory into that runtime's documented skill location. Name the installed directory `concision`; a GitHub ZIP may extract as `concision-main`. Keep `SKILL.md`, `references/`, and `agents/` together.

Using the skill itself requires no APIs, tools, connectors, or external skills. It can also be loaded manually as prompt context. The plugin manifests and `agents/openai.yaml` provide optional host metadata; the instructions in `SKILL.md` are portable.

## Usage

Ask in plain language:

```text
Use Concision to rewrite this update for my team. Keep the dates and blockers:
[paste your draft]
```

```text
Use Concision to explain how this works to a new developer.
Include the causal steps and one example:
[paste the topic or code]
```

```text
Use Concision to critique this email, then rewrite it in my voice:
[paste your draft]
```

Codex supports explicit invocation with `$concision`; a direct Claude Code skill installation uses `/concision`. Invocation syntax depends on your host.

Specify the audience, purpose, tone, and required detail when they matter. Concision preserves facts, uncertainty, and the writer's intent; detailed requests receive detailed answers.

## Modes

| Mode | When to use it | What you receive |
| --- | --- | --- |
| Editor | Write or rewrite a communication | A finished draft |
| Explainer | Understand a concept, mechanism, or decision | A direct answer with enough reasoning and examples |
| Coach | Ask for critique or editorial guidance | An assessment, or a rewrite with the key editorial choices |
| Collaborative | Draft or brainstorm together | Focused iterations |

The skill selects a mode from your request. You do not need to name one.

## How it works

Concision uses four checks adapted from Harsha Perera's [The Art of Being Concise](https://medium.com/@harshacoach/the-art-of-being-concise-3706c96f383f): the real question, the audience, curiosity, and knowing where you stand.

It identifies the essential message, puts the point early, and removes repetition while keeping the reasoning and nuance that matter. Complementary resources, such as a Humanizer skill or research tools, are optional and used only when available and useful.

See [SKILL.md](SKILL.md) for the instructions, [examples](references/examples.md) for sample requests, and [resource orchestration](references/resource-orchestration.md) for guidance on combining capabilities.

## Development

No build step is required. Python 3 and PyYAML are used only to validate the distribution package. From the repository root on macOS or Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python scripts/validate-package.py
npx skills add . --list
```

On Windows, use `.venv\Scripts\python.exe` in place of `.venv/bin/python`.

GitHub Actions runs both checks on pushes and pull requests. Keep the version in `SKILL.md`, both plugin manifests, and [CHANGELOG.md](CHANGELOG.md) in sync. Report problems or propose improvements through [GitHub issues](https://github.com/franciscoh017/concision/issues).

## skills.sh

Concision has a public [repository page on skills.sh](https://skills.sh/franciscoh017/concision) and an [individual skill page](https://skills.sh/franciscoh017/concision/concision) with instructions and installation details. A live page does not guarantee immediate inclusion in search results; skills.sh does not publish a guaranteed search-indexing timeframe in its FAQ.

According to the [skills.sh FAQ](https://skills.sh/docs/faq), skills are listed automatically through installation telemetry from `npx skills add <owner/repo>`. There is no separate submission requirement. A public repository and valid package make installation possible; listing and ranking depend on recorded installations.

Install with `npx skills add franciscoh017/concision`. To check available skills without installing, use `npx skills add franciscoh017/concision --list`.

## License

[MIT](LICENSE). Harsha Perera's article is credited as an influence; this license covers the material in this repository.
