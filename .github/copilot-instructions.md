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

## Guidance for Copilot code review and coding agents
- Always run or propose tests relevant to your changes.
- Do not introduce new frameworks without explicit request.
- When changing APIs, update backend models, frontend types, and tests together.
- Respect path-specific `.instructions.md` files and nested `AGENTS.md` guidance.
