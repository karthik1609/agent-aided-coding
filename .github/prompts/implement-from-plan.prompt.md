---
name: implement-from-plan
description: Implement a previously generated plan
agent: implement
model: GPT-5
tools:
  - githubRepo
  - terminal
  - workspace/edit
---

Take the plan from prior messages and apply it carefully. Make small, incremental edits and update tests. Confirm alignment with `.github/copilot-instructions.md`, path-specific instructions, and AGENTS files.
