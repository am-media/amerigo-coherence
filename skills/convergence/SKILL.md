---
name: convergence
description: Select the smallest viable solution for software and workflow requests; define acceptance tests, limit scope, and stop when the requested outcome is verified. Use for prototypes, features, bug fixes, and architectural changes.
---

# Convergence

1. Restate the user outcome in one sentence, not a technology choice.
2. Check whether the problem is already solved or can be addressed by an existing tool. Do not build software unless necessary.
3. Select exactly one recipe in `../../recipes/`: `use-existing-tool`, `prototype`, `add-feature`, `fix-bug`, or `architectural-change`. Record a one-line reason. Read only that recipe.
4. State observable acceptance criteria, scope, exclusions, and verification method. Use `../../templates/task.yaml` only when a persistent contract helps; for trivial tasks, a short inline contract suffices.
5. Implement the smallest complete vertical slice. Use existing patterns; apply TDD to testable behavior when useful. Do not expand scope, add infrastructure or refactor unrelated code.
6. Run appropriate verification including realistic end-to-end acceptance where possible; report unverified items explicitly.
7. If blocked twice on the same acceptance criterion, stop repeated attempts and reassess the strategy (simplify, pivot, or request a scoped decision). This is a review trigger, not automatic abandonment.
8. Once acceptance passes and no blocking risk remains, STOP. Further improvements become separately scoped tasks.

A recipe is guidance, not enforcement. Project permission boundaries, CI checks, and protected branches must enforce critical constraints independently.
