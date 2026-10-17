---
name: convergence
description: Select the smallest usable solution, define evidence-based acceptance criteria, limit implementation scope, and stop when the goal is verified. For prototypes, features, bugs, or architectural changes.
---

# Convergence

1. Restate the desired user outcome without presuming a technology. Consider a spreadsheet, existing tool, or no code.
2. Choose exactly one recipe from `../../recipes/` and record why. Read only that recipe.
3. Before coding, specify the outcome, acceptance evidence, allowed file paths, exclusions, and stopping condition. Small tasks can use a short inline contract. For substantive code changes use `../../templates/task.json` and keep it outside the agent's editable paths; the YAML template remains a human planning example.
4. Implement one small working vertical slice. Prefer the existing stack and TDD for suitable behavior. Do not rewrite unrelated files.
5. If the project is Git-backed and the JSON contract applies, run `python tools/guard.py .coherence/task.json --base origin/main` from the target repository (adapt the guard location and trusted base). Treat a failed guard as a blocked task, not permission to widen the contract.
6. Run actual acceptance and regression checks separately: passing the scope guard proves **only scope compliance**.
7. After two unsuccessful attempts against the same criterion, trigger a strategy review; do not continue cycling blindly.
8. Report one of four outcomes: ADOPT (verified, stop), FIX (bounded work), PIVOT (requires strategic decision), ABANDON (stop with reasons). See `../../docs/decisions.md`. Never claim verification without evidence.

This skill cannot prevent all agent deviations. Use independently configured CI, permissions and protected branches for essential controls. Do not allow an agent to approve its own expansion of scope.
