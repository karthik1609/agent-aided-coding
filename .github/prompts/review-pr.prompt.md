---
name: review-pr
description: Structured review against project instructions
agent: review
model: Claude-Sonnet-4.5
tools:
  - githubRepo
  - fetch
  - usages
---

Review the provided branch or diff. Enforce `.github/copilot-instructions.md`, path-scoped instructions, and AGENTS files. Respond with summary, strengths, issues (with severity), and recommended actions.
