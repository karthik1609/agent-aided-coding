description: Guidance for agents modifying the FastAPI gateway under `src/api_gateway`.

# API Gateway Agent Guidance

These instructions refine the root `AGENTS.md` for FastAPI endpoints.

## Design principles
- Keep endpoints thin—delegate loan logic to `backend_loans.services`.
- Define request/response schemas with Pydantic `BaseModel` classes; specify validation constraints and default values explicitly.
- Use dependency injection (`Depends`) when introducing shared services, clients, or configuration switches.
- Maintain idempotent, descriptive routes; prefer nouns and clear resource scopes.

## Error handling & observability
- Return precise HTTP status codes. Distinguish validation errors (422), business rule failures (400), and unexpected faults (5xx).
- Provide actionable `detail` messages without exposing sensitive internals.
- Instrument new logic with structured logging hooks (if added) and ensure FastAPI exception handlers cover new error types.

## Testing & contracts
- Update OpenAPI documentation automatically through Pydantic models; add docstrings when behaviour is non-obvious.
- Mirror schema changes in TypeScript clients/tests and regenerate fixtures where required.
- Cover endpoint behaviour with integration-style tests (FastAPI `TestClient`) in `tests/` when logic extends beyond service delegation.

## Toolchain pointers
- Use `#tool:githubRepo` to inspect route handlers, models, and dependency definitions.
- Prefer `#tool:read_file` for targeted schema checks instead of downloading entire modules.
- Run `#tool:terminal` commands such as `uv run pytest tests/api/test_api_gateway.py` before handing off.
- For advanced contract validation, enable the MCP `analysis` server to call OpenAPI diffs or schema validators defined in `mcp/analysis.json`.
