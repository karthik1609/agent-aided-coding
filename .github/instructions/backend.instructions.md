---
applyTo:
  - src/backend_loans/**
  - tests/backend/**
---

# Backend Loan Instructions
- Keep domain models immutable and favor pure functions.
- Interact with storage via repository interfaces only; avoid direct DB or network calls.
- Keep services focused on business rules; avoid embedding API or transport concerns.
- When adding fields, update API schemas and frontend types to match.
