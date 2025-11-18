# Claude Guidance

Claude-based agents should emphasize structured reasoning and cautious changes:
- Perform step-by-step analysis before proposing edits; cite inspected files and instruction sources.
- Highlight security, privacy, and compliance implications for any data handling or external calls.
- Prefer explicitness over magic—spell out preconditions, invariants, and migrations instead of hiding them in helper abstractions.
- Decompose large tasks into ordered checkpoints; recommend intermediate validations and tests at each stage.
- Summarize assumptions, open questions, and rollback strategies; request confirmation when requirements are ambiguous.
- When running in agent mode, favour review loops over aggressive automation and stop on repeated tool failures.
- Reference custom prompts (e.g. `/new-feature-plan`, `/review-pr`) to structure the conversation and reduce token churn.
- Call out when MCP tooling (defined in `mcp/`) would provide higher confidence and ask for permission before executing terminal commands.
