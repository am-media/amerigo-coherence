# Amerigo Coherence — constitutional development governance

**Start with [CONSTITUTION.md](CONSTITUTION.md).** Its six technology-agnostic principles govern every recipe and technical choice. Recipes are applications, not additional constitutions.

Outcome-first decision recipes for Codex. Prefer the smallest useful tool, finish observable tasks, and prevent unnecessary architectural drift.

## Contents

- `AGENTS.md` — repository behavior rules
- `skills/convergence/SKILL.md` — decision procedure and stopping rules
- `recipes/` — decision recipes, including recovery of existing repositories
- `templates/task.yaml` — human-readable planning example
- `templates/task.json` — machine-checkable scope contract example
- `tools/guard.py` — dependency-free **path-scope** check
- `tests/test_guard.py` — automated unit tests of guard decisions
- `tools/retrofit.py` — **read-only** Git-tracked-file inventory for existing repositories
- `tests/test_retrofit.py` — tests of the non-destructive report
- `templates/retrofit-review.md` — evidence and rollback checklist for recovery
- `tests/scenarios.yaml` — five **manual** behavioral evaluations
- `docs/decisions.md` — ADOPT / FIX / PIVOT / ABANDON outcomes

## Running it

Install or reference the `skills/convergence` skill in Codex according to your environment; project-local `AGENTS.md` instructions only affect the repository in which they reside.

For code tasks, copy `templates/task.json` to `.coherence/task.json` in the **target project**, and edit goal, acceptance, and exact allowed paths before coding. Keep the approved contract on a trusted base branch or outside the executor's edit permissions. Copy `tools/guard.py` into that project or invoke it from its installed shared location.

From the target project's root:

```sh
python tools/guard.py .coherence/task.json --base origin/main
```

This examines the diff from the merge base of `origin/main` to `HEAD`. **Uncommitted changes are not included**: commit to a working branch before running, and ensure your trusted base exists. Guard output is only evidence of path compliance, never a substitute for acceptance tests. For strict policy enforcement, protect the base branch and require this command in project CI with an approved baseline contract.

Self-tests for the guard:

```sh
python -m unittest discover -s tests -v
```

## Recover an existing project

Start with `recipes/retrofit-existing-repo.md`. From this repository (or a copy of the script) run:

```sh
python tools/retrofit.py --root /path/to/existing/project --output /tmp/retrofit-report.json
```

This writes only the explicitly requested report, never alters the inspected repository, and inventories Git-tracked files rather than detecting true unused code. Record a known-working baseline, verify actual user flows, choose **KEEP / REPAIR / SIMPLIFY / REPLACE_WITH_TOOL**, and approve one reversible change at a time. Large files and TODOs are not automatically defects.

## Limits

This repository does not claim automatic, account-level installation or complete architectural governance. It does not run Codex automatically, verify behavior of deployed applications, or enforce policy in other projects without integration. The tests in `tests/scenarios.yaml` have not been run against live Codex sessions. Do not add an agent manager, service, database, or further dependencies without observed need.

## V1 acceptance

1. Guard permits an authorized file modification.
2. Guard rejects changes outside the allowlist and changes to protected contract paths.
3. Automated unit tests pass.
4. GitHub contents and reviewable PR are present.

Behavioral improvement in real Codex tasks remains a separate evaluation.
