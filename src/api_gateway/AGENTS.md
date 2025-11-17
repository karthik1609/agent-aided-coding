# API Gateway Agent Guidance

These instructions refine the root `AGENTS.md` for FastAPI endpoints.

- Keep endpoints thin and delegate business rules to `backend_loans` services.
- Validate inputs with Pydantic models and return typed responses.
- Use dependency injection for shared services when expanding; avoid global mutable state beyond lightweight demos.
- Prefer clear HTTP status codes and concise error messages.
