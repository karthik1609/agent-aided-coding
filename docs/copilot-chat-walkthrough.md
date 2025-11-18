# GitHub Copilot Chat Walkthrough

This playbook shows how to re-create the demo project *entirely through GitHub Copilot Chat* in VS Code, using the custom instructions, agents, prompts, and MCP tooling that live in this repository. Keep a copy of this markdown open while you present or rehearse.

---

## 0. Prerequisites

- VS Code `1.106+` with GitHub Copilot and Copilot Chat enabled.
- Access to the Copilot Agents preview (agent mode) and MCP support.
- Python tooling for the `analysis.server` (or adjust the MCP manifest to point to your own executable).
- Optional: GitHub account with Copilot subscription for collaborators.

---

## 1. Prepare the Workspace

1. **Clone this repo** (or create a new workspace and copy the `.github/`, `mcp/`, and `docs/` folders).
2. **Clean out previous demo artifacts**:
   - Remove generated source files if you plan to rebuild them live (keep empty placeholder directories that are referenced by instructions).
   - Commit or stash anything you want to restore later.
3. **Install dependencies** if you intend to execute commands locally during the demo:
   ```bash
   uv sync
   npm install --prefix frontend-app
   ```

---

## 2. Apply VS Code Settings

Add the following snippet to your *workspace* `settings.json` and reload Copilot Chat:

```jsonc
{
  "github.copilot.chat.codeGeneration.useInstructionFiles": true,
  "chat.instructionsFilesLocations": [
    ".github/instructions"
  ],
  "chat.agentsFilesLocations": [
    ".github/agents"
  ],
  "chat.promptFilesLocations": [
    ".github/prompts"
  ],
  "chat.useAgentsMdFile": true,
  "chat.useNestedAgentsMdFiles": true,
  "chat.promptFilesRecommendations": true,
  "chat.mcpServers": [
    "${workspaceFolder}/mcp/analysis.json"
  ],
  "github.copilot.chat.reviewSelection.instructions": [
    { "file": ".github/agents/review.agent.md" },
    { "file": ".github/instructions/tests.instructions.md" }
  ],
  "github.copilot.chat.commitMessageGeneration.instructions": [
    { "text": "Reference the related ticket ID, summarise risk, and mention test evidence." }
  ],
  "github.copilot.chat.pullRequestDescriptionGeneration.instructions": [
    { "text": "Output a PR template with context, changes, risks, validation, and follow-up tasks." }
  ]
}
```

> ✅ Optional: enable Settings Sync (Prompts & Instructions) so the same configuration follows you to other machines.

---

## 3. Verify the Instruction Hierarchy

Ensure the following files are present (they drive Copilot’s behaviour):

| Area | Path | Purpose |
| --- | --- | --- |
| Global defaults | `.github/copilot-instructions.md` | Repository-wide guardrails, VS Code checklist, MCP overview. |
| Scoped rules | `.github/instructions/*.instructions.md` | Backend, frontend, infra, and test-specific expectations (with `applyTo` globs). |
| Agent hierarchy | `AGENTS.md`, `frontend-app/AGENTS.md`, `src/api_gateway/AGENTS.md`, `src/backend_loans/AGENTS.md` | Responsibilities and tooling pointers for each sub-tree. |
| Custom agents | `.github/agents/*.agent.md` | Planner, implementer, reviewer, tester, docs (with tools, MCP servers, handoffs, tags). |
| Prompt files | `.github/prompts/*.prompt.md` | Slash commands (`/new-feature-plan`, `/implement-from-plan`, etc.) with optional inputs. |
| Model guides | `CLAUDE.md`, `GEMINI.md` | Reasoning tips for specific LLMs. |
| MCP manifest | `mcp/analysis.json` | Demo server exposing `openapi_diff`, `a11y_audit`, `test_heuristics`. |
| Walkthrough | `docs/copilot-agentic-demo.md`, **this file** | High-level overview + this step-by-step guide. |

No changes are required if these files already exist; just keep them synced in version control.

---

## 4. Start VS Code Copilot Chat

1. Open the **Copilot Chat view** (⌃⌘I / Ctrl+Shift+I).
2. Select the **Planner** agent from the drop-down (or use the `/new-feature-plan` prompt).
3. Attach context using:
   - `#file` for specific placeholders (e.g. `#frontend-app/src`).
   - `#codebase` for cross-repo discovery (use sparingly; respects your instructions).
   - Links or ticket IDs via `${input:context}` when the prompt requests them.

---

## 5. Demo Workflow (Live Generation)

Use the following chat sequence to rebuild the project during the demo:

1. **Plan**  
   - Command: `/new-feature-plan feature="Scaffold the loan API Gateway and frontend shell"`  
   - Include optional context (e.g. `${input:context}` with design notes).  
   - The planner will cite relevant instruction files and produce a multi-step plan plus suggested handoffs.

2. **Implement**  
   - Click the handoff button “Implement this plan” or run `/implement-from-plan plan_url="<copied output>"`.  
   - Approve each terminal command suggestion (`uv run ...`, `npm run ...`).  
   - Watch the implementer agent use `githubRepo`/`workspace/edit` to create files under `src/` and `frontend-app/`.

3. **Generate Tests**  
   - Run `/write-tests target="backend loans eligibility"` with optional `${input:coverage}`.  
   - Allow the agent to use MCP `test_heuristics` if you enabled it.  
   - Tests go in `tests/backend/` or `tests/api/` per instructions.

4. **Review**  
   - Run `/review-pr pr_url="local-change"` (for local diffs) or handoff via the implementer agent.  
   - Ask follow-up questions using the `review` agent to inspect severity-tagged issues and suggested fixes.  
   - Trigger MCP analyses (e.g., `openapi_diff`) by confirming the agent’s proposals.

5. **Documentation**  
   - Switch to the `docs` agent or run `/refactor-service` / `/write-tests` with documentation focus.  
   - Have it update `docs/copilot-agentic-demo.md`, architectural notes, or CHANGELOG entries summarising the session.

6. **Wrap-up (optional)**  
   - Use the built-in **Commit Message** and **PR Description** Copilot actions; the settings snippet above sends them to instruction files for consistency.

---

## 6. MCP Server Tips

1. Confirm the manifest path in `chat.mcpServers` matches your workspace.
2. Export any credentials before starting VS Code (e.g. `export ANALYSIS_API_KEY=...` on macOS/Linux, or set them in your shell profile).
3. If you replace the demo server, update:
   - `mcp/analysis.json` (or add new manifests).
   - The `mcp-servers` arrays inside the agent frontmatter.

---

## 7. Optional Enhancements

- **Additional agents/prompts**: Copy existing `.agent.md` or `.prompt.md` files and adjust names to create new personas (e.g., security auditor, refactor coach).
- **User-level instructions**: Add personal preferences in your VS Code profile so they apply across workspaces without touching repository files.
- **Workspace reset script**: Create a simple shell script that removes generated code files so you can run the demo repeatedly.
- **Recordings**: Use VS Code’s “Chat: Export Session” command to share transcripts that show instruction adherence.

---

## 8. Troubleshooting Checklist

- Instructions not applying? → Re-run `Chat: Configure Instructions` and confirm `useInstructionFiles` is enabled.
- Custom agents missing? → Verify `chat.agentsFilesLocations` path and that frontmatter `target: vscode` is set.
- Prompt commands not showing? → Check `chat.promptFiles` / `chat.promptFilesLocations` and reload the chat view.
- MCP tools unavailable? → Ensure `chat.mcpServers` points to a valid manifest and the underlying binary exists.
- Agent outputs ignoring guidance? → Mention the specific instruction file in your prompt (e.g., “follow `.github/instructions/backend.instructions.md`”)—this reminds Copilot of priority.

---

## 9. After the Demo

- Commit the generated source code if you want to keep it, or run your reset script to return to a clean slate for the next run.
- Update this walkthrough with lessons learned, new prompt ideas, or tooling tweaks.
- Share the repository with attendees so they can clone it and replay the workflow on their own machines.

Happy demoing! With these steps in place, your entire application scaffold can come to life through GitHub Copilot Chat, showcasing the full spectrum of custom instructions, agents, prompt files, and MCP integrations.

