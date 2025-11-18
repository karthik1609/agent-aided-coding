---
name: backend-guidance
description: Domain and service-layer rules for backend loans code.
applyTo: "src/backend_loans/**,tests/backend/**"
---

# Backend Loan Instructions
- Keep domain models immutable and favour pure functions; ensure calculations remain deterministic across runs.
- Interact with storage via repository interfaces only; add abstractions instead of calling external systems directly.
- Keep services focused on business rules; record side effects (logging/metrics) at composition boundaries.
- Document eligibility formulas inline and cover risk edges (max/min scores, debt-to-income triggers) with tests.
- When adding fields or changing behaviour, update FastAPI schemas, repository contracts, fixtures, and TypeScript types together.
- Prefer pytest fixtures for repeated setup and isolate tests from global state.
- Use `#tool:githubRepo` to inspect models/services before modifying them and `#tool:runCommands` with `uv run pytest` to validate logic.
- Reference the `implement` and `tests` agents for coordinated code/test updates; see `/implement-from-plan` and `/write-tests` prompts.
