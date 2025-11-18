Purpose
-------
This folder stores per-feature, machine-friendly checklists used by planner → implement → tests → review agent flows.

Location
--------
`docs/checklists/<feature-id>.yaml`

Schema (minimal)
----------------
- `id` : string — feature identifier (use ticket id if available).
- `title` : string — short human title.
- `items` : list of items with:
  - `id` : string — item id (plan-1, plan-2, ...).
  - `description` : string.
  - `status` : string — one of `planned`, `in-review`, `implemented`, `tested`, `done`, `removed`, `rework`.
  - `review` : `null` | `pass` | `fail`.
  - `implemented` : boolean.
  - `implemented_by` : string | null (agent or author).
  - `pr_number` : string | null (e.g., `#123`).
  - `tests` :
    - `status` : `pending` | `pass` | `fail`.
    - `last_run` : ISO8601 timestamp | null.
    - `artifacts` : list of artifact paths or CI URLs.
  - `notes` : list of short strings for context or remediation.
- `last_updated` : ISO8601 timestamp.

Agent update rules (IMPORTANT)
-----------------------------
- Agents must not push direct commits to `main` to update checklist files. Update the checklist by opening a focused PR that only changes the relevant feature checklist file(s).
- Planner: create the initial checklist YAML and include it in the plan output.
- Implement: when implementation begins, update `items[].status` and set `implemented_by` and `pr_number` in the PR body.
- Tests: after running tests, update `items[].tests.status`, `items[].tests.last_run`, and attach artifacts.
- Review: run the checklist validator and set `items[].review` to `pass` or `fail`. Do not mark pass unless validator + tests pass.

Gating rules
------------
The validator enforces: any item with `status` in `implemented|tested|done` must have `tests.status == pass` and `review == pass` (configurable in the validator). CI initially runs the validator in advisory mode; maintainers will promote it to blocking after baselining.

Conflict handling
-----------------
- Prefer one checklist per feature to reduce conflicts.
- If multiple PRs update the same file, resolve merge conflicts in small follow-up PRs and document the resolution in `notes`.

Rollout
-------
1. Add validator and CI job in advisory mode.
2. Baseline `main` with the validator and fix/whitelist outstanding issues.
3. Promote CI job to required once baseline is clean.

Contact
-------
If you have questions about checklist format or CI gating, open an issue and reference `infra` or `devops` maintainers.
