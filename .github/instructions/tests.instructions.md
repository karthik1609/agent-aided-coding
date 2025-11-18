---
name: tests-guidance
description: Expectations for automated tests across the repository.
applyTo:
  - tests/**
---

# Test Instructions
- Use descriptive test names that capture behaviour and expected outcome.
- Prefer fixtures for shared setup; isolate tests from network calls, file system writes, and real clocks.
- Mock external dependencies; keep tests fast, deterministic, and idempotent under parallel execution.
- Assert both success and failure modes (validation errors, edge-case scores, empty datasets).
- Record any manual verification steps in PR descriptions when automated coverage is impractical.
- For pytest suites, run `uv run pytest -q` via `#tool:terminal`; for frontend suites, execute `npm test -- --runInBand`.
- Coordinate with the `tests` agent and `/write-tests` prompt when expanding coverage or building regression suites.
