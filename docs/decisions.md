# Convergence decisions

Each iteration ends with exactly one outcome:

- **ADOPT** — all agreed acceptance checks are demonstrated, no blocking regression; stop work.
- **FIX** — a reproducible defect remains within agreed scope; make a bounded correction.
- **PIVOT** — the chosen approach fails to meet an agreed requirement; propose a different strategy before continuing.
- **ABANDON** — stop investing when further work is not justified; explain what was learned.

After **two unsuccessful attempts on the same criterion**, record the evidence and reconsider the approach; do not automatically keep coding.

## Independent evidence

The scope guard only enforces paths and protected files against a Git diff. It does not understand architectural merit, inspect real runtime behavior, enforce package additions unless manifest paths are excluded, or prove acceptance. Those require project-specific checks and/or human review.

Treat `ADOPT` as permitted only when acceptance evidence exists, not when the agent merely asserts that it works. Changes to protected policy must be handled in an explicitly approved separate change and protected by GitHub branch rules to prevent bypass.
