description: Frontend-specific guardrails for Copilot agents working inside `frontend-app`.

# Frontend Agent Guidance

These instructions refine the root `AGENTS.md` for the React app.

## Architectural guardrails
- Ship functional components with hooks; colocate state and favour derived data over duplicated stores.
- Keep styling lightweight (utility classes or scoped CSS). Do not add UI frameworks without explicit approval.
- Prefer declarative data fetching with `fetch`/`React Query`-style hooks you implement locally; avoid global state managers for this demo.
- Model all client types from the API gateway responses; keep them in sync when backend contracts change.

## Accessibility & UX
- Default to semantic HTML elements and labelled inputs. Provide keyboard focus handling for interactive components.
- Error surfaces should be human-readable and avoid leaking implementation details.
- Internationalisation is out of scope, but keep copy in constants to simplify future localisation.

## Testing expectations
- Extend existing React Testing Library patterns; tests should validate rendered output and key interactions.
- Use MSW or lightweight mocks for network calls—no live HTTP requests.
- Document manual QA steps (browser/device, commands) in PR summaries when visual changes occur.

## Tooling hooks
- Prefer `#tool:githubRepo` for reading component files and `#tool:workspace/edit` for JSX/TSS edits.
- Invoke `#tool:terminal` with `npm run lint` / `npm test -- --watch=false` when verifying changes.
- MCP UI linters are available through the shared `analysis` server (see `mcp/analysis.json`) if enabled.
