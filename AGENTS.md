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
3. Nested `AGENTS.md` files – refine guidance for subdirectories (e.g., backend and frontend). The more specific file overrides general guidance when conflicts arise.

Stay consistent with these documents and cite them when making decisions in reviews or plans.
