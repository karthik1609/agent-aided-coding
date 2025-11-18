---
description: Global Copilot guidance for the agent-aided-coding-1 workspace.
---

# Copilot Repository Instructions

## Project summary
Demo monorepo for an LLM-assisted loan platform. The repo showcases Copilot custom instructions, nested AGENTS.md guidance, custom agents, and reusable prompt files.

## Build & test
- Backend: `uv sync` then `uv run api-gateway` or `uv run worker-ingestion`
- Tests: `uv run pytest`
- Frontend: `cd frontend-app && npm install && npm run dev`
- Infra: `docker compose -f infra/docker-compose.yml up`

## Coding standards
- **Python**: FastAPI, type hints everywhere, Pydantic models for I/O. Avoid bare `except`. Keep endpoints thin; business logic lives in `backend_loans`.
- **Frontend**: Functional React components with hooks. Prefer TypeScript. Keep styling minimal and accessible.
- **Tests**: Use pytest. Keep tests small and deterministic.

## Instruction layering
- This file applies to every Copilot request. Path-scoped `.instructions.md` and nested `AGENTS.md` content augments (or tightens) these rules; avoid duplicating guidance across files.
- When drafting new guidance, include `description`/`name` metadata and `#tool:` references where relevant so Copilot can reason about available capabilities.
- Link to shared guidance instead of pasting large snippets; prompts and agents can reference instructions directly via Markdown links.
- Use `.github/instructions/*.instructions.md` for path-specific rules, nested `AGENTS.md` for directory-scoped agent behaviour, and `.github/agents/*.agent.md` / `.github/prompts/*.prompt.md` for task workflows.

## Agent mode expectations
- Agent mode may run multi-step workflows. Keep scopes tight, prefer incremental commits, and intervene when output diverges.
- Terminal commands require your explicit approval—review each one, cancel unexpected mutations, and kill long-running jobs before switching tasks.
- Monitor tool output for errors, especially install/test commands, and iterate until the working tree is green.

## Prompting best practices
- Provide concrete context (files, symbols, specs) and break work into verifiable steps.
- Ask for implementation plus validation: require updated tests, logging, or docs when functionality changes.
- Favour deterministic solutions over “clever” ones and request follow-up hardening (error handling, performance, security) when appropriate.
- Reference context with `#file`, `#codebase`, or drag-and-drop attachments; cite instructions (e.g. `[Backend Rules](instructions/backend.instructions.md)`) when relevant.
- Use prompt files (type `/` in chat) for reproducible workflows and select specialised agents from the chat picker.

## Customisation map
- **Global instructions**: this file.
- **Scoped rules**: `.github/instructions/*.instructions.md` (see `name`/`description` frontmatter for purpose).
- **Agent personas**: `.github/agents/*.agent.md` with tool lists, MCP servers, and handoffs.
- **Reusable prompts**: `.github/prompts/*.prompt.md` for planning, implementation, refactors, reviews, and testing.
- **Model-specific tips**: `CLAUDE.md`, `GEMINI.md`.
- **MCP tooling**: JSON manifests in `mcp/` describing external capabilities available to agents.

## Guidance for Copilot code review and coding agents
- Always run or propose tests relevant to your changes.
- Do not introduce new frameworks without explicit request.
- When changing APIs, update backend models, frontend types, and tests together.
- Respect path-specific `.instructions.md` files and nested `AGENTS.md` guidance.

## VS Code configuration checklist
- Enable instruction files: `"github.copilot.chat.codeGeneration.useInstructionFiles": true`.
- Register locations:
  - `"chat.instructionsFilesLocations": [".github/instructions"]`
  - `"chat.agentsFilesLocations": [".github/agents"]`
  - `"chat.promptFilesLocations": [".github/prompts"]`
- Allow nested agents: `"chat.useAgentsMdFile": true`, `"chat.useNestedAgentsMdFiles": true`.
- Surface prompt hints: `"chat.promptFilesRecommendations": true`.
- Configure MCP servers referenced in agent frontmatter via `"chat.mcpServers"`.

## MCP tooling quick start
- Working MCP manifests live under `mcp/*.json`.
- Add entries to `mcp-servers` frontmatter in agent files to pre-load capabilities.
- Ensure required credentials live in environment variables before invoking MCP-backed tools.
