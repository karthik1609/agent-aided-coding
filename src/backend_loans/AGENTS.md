# Backend Loans Agent Guidance

This directory contains the domain layer for loan logic. These instructions refine the root `AGENTS.md`.

- Keep API endpoints thin; put business logic in `services/`.
- Domain models should be immutable (`frozen=True` for Pydantic models).
- Access data only through repository interfaces in `repositories/`. No direct DB or network calls.
- Prefer pure functions and deterministic calculations for eligibility logic.
- When adding fields, update both request/response schemas in `api_gateway` and corresponding frontend types.
