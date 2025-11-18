---
name: frontend-guidance
description: UI development constraints for the React client.
applyTo:
  - frontend-app/**
---

# Frontend Instructions
- Use functional components with hooks; avoid class components and legacy lifecycle APIs.
- Keep UI simple (native elements or minimal CSS). Do not add large UI frameworks or heavy icon packs.
- Co-locate state with components, keep forms controlled, and persist cross-route state via URL/query params where viable.
- Align TypeScript types with backend schemas—regenerate shared DTOs or update Zod validators whenever the API changes.
- Handle loading/error/empty states explicitly and ensure user input is validated before calling the API.
- Extend test coverage with React Testing Library; mock network calls using MSW or local stubs.
- Run `npm run lint` / `npm test` via `#tool:terminal` before completing tasks.
- Use prompt `/refactor-service` for structural updates and `/write-tests` with `target=frontend` for coverage improvements.
