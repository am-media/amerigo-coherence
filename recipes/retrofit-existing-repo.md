# Core-first recovery (existing repositories)

**Mission:** recover a demonstrably working core or ship the smallest production-ready MVP. Reduce active surface area aggressively. Do not preserve speculative architecture merely because time was spent building it.

## 0. Declare the mission, not a redesign

Choose exactly ONE outcome:
- **PROVE_CORE** — exercise the smallest end-to-end critical flow and stress its real failure modes.
- **SHIP_MVP** — make the smallest complete user journey deployable, including essential security/operational constraints.
- **ADD_FEATURE** — implement one requested observable behavior on the existing core.

Name the executable acceptance test, the earliest practical evidence, and the stop condition. If the core is unvalidated, do not expand features.

## 1. Establish a safe baseline

Work in a recovery branch. Record current commit, existing build/test state, real user flows, and data/migration obligations. Keep the original branch as the archive/rollback point. Never destroy data, secrets, deployment state or an established working flow.

Do not spend days cataloguing every file. Inspect entrypoints, runtime dependency edges and actual MVP requirements first. Optional read-only inventory: `python tools/retrofit.py --root /path/to/project`.

## 2. Classify by demonstrated necessity

Classify the active runtime surface into:
- **CORE** — exercised directly by the mission's acceptance path.
- **REQUIRED** — essential for the mission's functioning, security, deployment, rollback, observability or compliance.
- **DEFER** — potentially useful later, but not needed now.
- **REMOVE** — demonstrably dead, redundant or contradictory to the selected path.

Default for unproven speculative infrastructure: **DEFER**. Burden of proof is on keeping it active. Unknown critical dependencies are not presumed safe to remove: investigate the edge, then decide.

Explicitly identify speculative services, theme systems, unused abstractions, alternate pipelines and unused UI. Do not keep them wired merely because they exist.

## 3. Isolate the nonessential surface

For DEFER/REMOVE items, prefer in this order:
1. Stop referencing, importing, registering, deploying or executing them in the MVP path.
2. Remove dead integration points and unused configuration from the active build.
3. Preserve recoverable code in Git history / a dedicated archive branch or tag, rather than relocating files into an archive directory that remains importable or buildable.
4. Delete obsolete active files only after dependency verification and a passing baseline/regression path; record exact recovery ref.

A separate approved task contract authorizes the isolation batch. Do not touch unrelated active functionality or silently redefine the mission. Prefer cohesive cuts over arbitrary one-file changes; one reversible commit per logical cut.

## 4. Solid boundaries, zero architecture theater

Separate meaningful responsibilities using ordinary modules/functions where that improves replaceability or testability. An adapter can be one file with a small explicit interface: **no factory, plugin registry, generic bus, framework or provider unless current verified requirements demand it**.

Reuse an abstraction when multiple real consumers need stable shared behavior; do not build for imagined future consumers. Preserve essential input validation, errors, test seams and operational safety. Minimalism is not permission to ship insecure or unreliable behavior.

## 5. Deliver the mission

First make the critical path run. Then perform the smallest security, reliability, deployability and test work appropriate to the selected mission. Use tests that exercise the actual user journey; do not accept mock-only proof for the core. Stress the core only on risks relevant to the goal.

Do not add features or aesthetic polish outside the mission. After two attempts without progress against the same acceptance criterion, propose PIVOT rather than elaborating the structure.

## 6. Exit deliberately

- **ADOPT:** critical path demonstrated, applicable gates passed; stop.
- **FIX:** a specific failing acceptance condition remains; bounded repair.
- **PIVOT:** current approach fails; change strategy only through an explicit decision.
- **ABANDON:** stop work based on evidence.

Report: goal, tested core path, CORE/REQUIRED retained, DEFER/REMOVE disconnected, checks run, recovery ref, residual risks. Avoid an audit report longer than the actionable recovery plan.

## Hard prohibitions

No speculative layers; no premature scale-out; no feature backlog construction; no blanket rewrite; no moving code to a live `archive/` that continues loading it; no destructive data migrations without explicit authorization and rollback. Aggressive scope reduction, conservative data handling.
