---
description: Workspace-wide guardrails that every Copilot agent must honour.
---

# Agent Guidelines (Root)

Welcome! This repository is a teaching environment for GitHub Copilot instructions, path-scoped guidance, custom agents, and prompt files. **All agents and contributors must read this document first** before touching code or docs.

## How to work in this repo
- Prefer small, incremental edits with clear intent.
- Run or propose relevant tests for your changes. Use `uv run pytest` for backend code and `npm test`/`npm run lint` for frontend when applicable.
- When changing APIs, update both backend models and frontend types.
- Keep dependencies minimal; never introduce a new framework unless requested.

## Build & Run
- **Backend services:** `uv sync` then `uv run api-gateway`, `uv run backend-init`, or `uv run worker-ingestion`.
- **Frontend:** `cd frontend-app && npm install && npm run dev`.
- **Infrastructure:** illustrative only; prefer `docker compose up` for demos.

## Coding standards
- **Python:** use type hints, Pydantic models for request/response schemas, and FastAPI conventions. Avoid bare `except` and keep business logic in the service layer (`backend_loans`).
- **React:** prefer functional components and hooks. Keep styling simple and accessible.
- **Tests:** keep them deterministic and isolated; use pytest fixtures for shared setup.

## Instruction hierarchy
1. `.github/copilot-instructions.md` – repo-wide defaults.
2. `.github/instructions/*.instructions.md` – path-scoped rules.
3. Nested `AGENTS.md` files – refine guidance for subdirectories (e.g., backend and frontend). The more specific file overrides general guidance when conflicts arise. Ensure the `chat.useNestedAgentsMdFiles` setting is enabled when testing nested behaviour locally.

## Agent responsibilities
- Surface the applicable guidance you follow in responses, especially when suggesting risky edits.
- Always validate pending diffs (tests, lint, type-checks) and report command outcomes.
- Keep diffs reviewable: prefer multiple focused iterations over sweeping rewrites.

## Agent mode safety rails
- Treat each terminal command as opt-in: confirm scope, guard against destructive flags, and cancel noisy processes before moving on.
- Stop auto-iterations if tooling output indicates persistent failures and summarise remediation options.
- Request human confirmation before changing execution environments (e.g., installing packages, editing infra manifests).

## Collaboration & handoffs
- Reference relevant instruction files or prompt templates rather than duplicating prose.
- When handing work to another agent, summarise remaining risks, outstanding commands/tests, and context already gathered.
- Capture assumptions in responses so follow-up requests can challenge or refine them.

## Tools & models
- Default chat model: see `.github/agents/*.agent.md` `model` field. Override with `#model` tags or prompt frontmatter when needed.
- Available tools: `githubRepo`, `workspace/edit`, `terminal`, `read_file`, plus any MCP tools declared in `mcp/*.json`. Cite expected tools in responses (e.g. `#tool:githubRepo`).
- If a task requires additional capabilities, either update the relevant agent frontmatter or attach MCP configs in `mcp/`.

## Settings reference
- Ensure VS Code `settings.json` includes the locations for instructions, prompts, and agents (see `.github/copilot-instructions.md`).
- For workflow-specific instructions (PR descriptions, commit messages, etc.), use the `github.copilot.chat.*.instructions` settings shown in `docs/copilot-agentic-demo.md`.

Stay consistent with these documents and cite them when making decisions in reviews or plans.
