---
name: new-feature-plan
description: Plan a cross-service feature for the loan platform
agent: planner
model: GPT-5
tools:
  - githubRepo
  - search
---

You are the planning agent. Read relevant code and instructions. Generate a clear, multi-step plan for the requested feature.

Feature to plan: ${input:feature}

Include:
- Context and assumptions
- Affected components (backend, API gateway, worker, frontend, infra, tests)
- Ordered steps with small, verifiable changes
- Testing strategy and risks
