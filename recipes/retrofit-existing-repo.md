# Retrofit an existing repository

**When:** A project already exists, iterations have accumulated complexity, and progress is unclear. This is a recovery procedure, not permission to rewrite.

**Phase 1 — Preserve:** work in a separate branch; do not delete files, upgrade dependencies, change architecture or reformat the whole repository. Identify the currently working user journeys and run the existing build/tests. Record actual failures.

**Phase 2 — Inspect:** run the optional read-only inventory with `python tools/retrofit.py --root /path/to/project`. Review reports and architecture manually. File size, TODOs and dependency count are **signals, never proof** of bad design. Investigate duplication, unreachable code, abandoned experiments, needless layers and inconsistent entrypoints using source references and reproducible evidence.

**Phase 3 — Decide:** compare four options: keep as is, repair targeted behavior, simplify a small slice, or replace with an existing tool. Choose the smallest option that restores an observable outcome. Label each proposed removal with evidence, affected paths, behavior at risk, rollback plan and acceptance tests.

**Phase 4 — Sanitize incrementally:** establish an approved bounded contract for each change. Before removing code, prove with usage search and applicable tests that it is unused or safely replaceable; preserve data and migration paths. No bulk automatic deletion. Prefer one independently reversible change per commit.

**Phase 5 — Verify and stop:** run regression and acceptance checks on the real user journey. ADOPT when the project is usable with no blocking regressions; FIX if a scoped repair remains; PIVOT only on documented failure of the approach; ABANDON if continued investment is unjustified.

**Explicit non-goals:** comprehensive rewrite, generic platform migration, cosmetic architecture cleanup, or producing a massive audit backlog without shipping a working outcome.
