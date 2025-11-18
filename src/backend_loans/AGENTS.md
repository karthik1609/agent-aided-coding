description: Guidance for agents working in `src/backend_loans`.

# Backend Loans Agent Guidance

This directory contains the domain layer for loan logic. These instructions refine the root `AGENTS.md`.

## Domain & services
- Keep API endpoints thin; all eligibility and pricing logic lives in `services/`.
- Domain models must remain immutable (Pydantic `BaseModel`, `frozen=True`) so calculations stay deterministic.
- Express business rules in pure functions where possible—inject dependencies instead of reading globals.

## Data access
- Use repository interfaces in `repositories/` exclusively. If new persistence concerns surface, add abstractions and tests before integrating.
- Mock repository interfaces in service tests; do not rely on network calls or mutable state.
- When adding fields, update request/response schemas in `api_gateway` and mirror types in the frontend.

## Quality gates
- Extend unit tests to cover new rule branches, boundary conditions, and regression scenarios.
- Document formula assumptions in code comments or accompanying docs for future audits.
- Ensure services expose clear error reasons so API and frontend layers can pass user-friendly messages through.

## Toolchain pointers
- Evaluate business logic with `#tool:githubRepo` and `#tool:read_file` before editing.
- Use `#tool:terminal` to run `uv run pytest tests/backend/test_loan_logic.py` and any new focused suites.
- The MCP `analysis` server can perform rate-calculation sanity checks or regression baselines—see `mcp/analysis.json` for configuration.
