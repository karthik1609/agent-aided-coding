---
name: refactor-service
description: Refactor a selected service while respecting path instructions
agent: implement
model: GPT-5
tools:
  - githubRepo
  - workspace/edit
---

Refactor the chosen service to improve clarity and maintainability while keeping behavior stable.

Service: ${input:service}

Follow relevant `.instructions.md` rules and nested `AGENTS.md` guidance. Describe tests to run after changes.
