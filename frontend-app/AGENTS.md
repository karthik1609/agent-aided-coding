# Frontend Agent Guidance

These instructions refine the root `AGENTS.md` for the React app.

- Use functional components with hooks; keep state minimal and colocated.
- Keep styling simple (utility classes or basic CSS). Avoid adding UI frameworks without approval.
- Align TypeScript types with backend schemas returned by the API gateway.
- Prefer declarative data fetching with `fetch` or a lightweight wrapper; no global state libraries for this demo.
