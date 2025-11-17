---
name: write-tests
description: Generate or improve tests for a module
agent: tests
model: GPT-5
tools:
  - githubRepo
  - workspace/edit
  - search
---

Generate or refine tests for the given area, keeping them deterministic and aligned with `tests.instructions.md`.

Target module or change: ${input:target}
