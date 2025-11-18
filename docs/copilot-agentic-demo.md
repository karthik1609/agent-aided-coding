# Copilot Agentic Demo Guide

This guide shows how every configuration file in this repository fits together to deliver a fully-instrumented Copilot experience for planning, coding, testing, documentation, and review workflows.

## File inventory

| Path | Purpose | Key fields demonstrated |
| --- | --- | --- |
| `.github/copilot-instructions.md` | Global guardrails for every Copilot session. | Frontmatter `description`, layered instruction strategy, VS Code settings checklist, MCP overview. |
| `.github/instructions/*.instructions.md` | Path-scoped guidance for backend, frontend, infra, and test directories. | Frontmatter `name`, `description`, `applyTo`, `#tool:` references, cross-prompt guidance. |
| `AGENTS.md` | Repository-wide agent responsibilities and safety rails. | Frontmatter `description`, tooling/model references. |
| `frontend-app/AGENTS.md`, `src/*/AGENTS.md` | Directory-specific agent expectations. | Frontmatter metadata, tool usage patterns, MCP references. |
| `.github/agents/*.agent.md` | Custom agent definitions (planner, implementer, reviewer, tester, docs). | `name`, `description`, `target`, `model`, `tools`, `mcp-servers`, `argument-hint`, `handoffs`, `tags`. |
| `.github/prompts/*.prompt.md` | Slash commands for common workflows. | `name`, `description`, `agent`, `model`, `tools`, `argument-hint`, multi-input variables. |
| `CLAUDE.md`, `GEMINI.md` | Model-specific reasoning guidance. | Integration tips for prompts, MCP, and cross-language checks. |
| `mcp/analysis.json` | Sample MCP server configuration powering analysis tools. | `$schema`, `binary`, `args`, `env`, `tools` definitions. |

## VS Code settings

Add the following snippet to your workspace `settings.json` (or adapt for user settings) so Copilot can discover the custom instructions, agents, prompts, and MCP server:

```json
{
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "chat.instructionsFilesLocations": [
    ".github/instructions"
  ],
  "chat.agentsFilesLocations": [
    ".github/agents"
  ],
  "chat.promptFilesLocations": [
    ".github/prompts"
  ],
  "chat.useAgentsMdFile": true,
  "chat.useNestedAgentsMdFiles": true,
  "chat.promptFilesRecommendations": true,
  "chat.mcpServers": [
    "${workspaceFolder}/mcp/analysis.json"
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    {
      "file": ".github/agents/review.agent.md"
    },
    {
      "file": ".github/instructions/tests.instructions.md"
    }
  ],
  "github.copilot.chat.commitMessageGeneration.instructions": [
    {
      "text": "Reference the related ticket ID, summarise risk, and mention test evidence."
    }
  ],
  "github.copilot.chat.pullRequestDescriptionGeneration.instructions": [
    {
      "text": "Output a PR template with context, changes, risks, validation, and follow-up tasks."
    }
  ]
}
```

> Tip: enable Settings Sync for “Prompts and Instructions” so the workspace setup travels with you.

## Workflow example

1. **Plan** – Select the `planner` agent in Copilot Chat (or run `/new-feature-plan`). Attach relevant files with `#file` and include optional `${input:context}` data. Review handoff suggestions when the plan finishes.
2. **Implement** – Switch via the handoff button or run `/implement-from-plan`. Approve terminal commands before execution, and cite instructions followed in your summary.
3. **Test** – Use `/write-tests` with coverage goals. The `tests` agent can call the MCP `test_heuristics` tool for additional cases.
4. **Review** – Trigger `/review-pr` (with `${input:pr_url}` if applicable). The `review` agent may run MCP `openapi_diff` or `a11y_audit` as part of the assessment.
5. **Docs & Handoffs** – `/refactor-service` or the `docs` agent keep architecture notes and README sections updated; cite `docs/copilot-agentic-demo.md` for onboarding.

## MCP server bootstrap

1. Ensure Python tooling for `analysis.server` is installed (or replace the `binary`/`args` with your own executable).
2. Export `ANALYSIS_API_KEY` if the analysis server requires credentials.
3. Restart VS Code or reload the Copilot Chat view to pick up the MCP config.
4. The tools `openapi_diff`, `a11y_audit`, and `test_heuristics` become available to agents that declare `mcp/analysis.json`.

## Extending the demo

- Add more MCP manifests (for observability, design linting, data fixtures) and reference them from agent frontmatter.
- Create additional prompts (for migrations, triaging bug reports, etc.) using the same metadata structure.
- Layer in user-level instructions (outside the repo) for personal preferences while keeping workspace defaults intact.
- Experiment with different models per agent (`GPT-4o`, `Claude 3.7 Sonnet`, `Gemini 2.0 Flash`) to compare behaviour and document best-fit scenarios in the model guidance files.

