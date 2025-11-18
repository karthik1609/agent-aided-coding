---
name: infra-guidance
description: Deployment and infrastructure guardrails for demo manifests.
applyTo:
  - infra/**
---

# Infra Instructions
- Keep manifests minimal and demo-focused—avoid introducing managed services or vendor-specific features.
- Expose only necessary ports, prefer environment variables for configuration, and document default values in README.
- Never commit secrets or credentials; use placeholders and reference `.env.example` if needed.
- Ensure docker-compose scenarios map to documented commands in `README.md`; keep them aligned with backend/frontend startup instructions.
- When changing services, update health checks and networking to match FastAPI/worker ports.
- Use `#tool:githubRepo` for YAML manifests and `#tool:terminal` with `docker compose config` to validate syntax.
- The `/new-feature-plan` prompt should capture infra impacts; `/review-pr` enforces these constraints during reviews.
