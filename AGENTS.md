# Constitutional authority

Read and follow `CONSTITUTION.md` before making technical decisions. It is technology-agnostic and takes precedence over recipes; select the smallest sufficient solution, and demand evidence for extra complexity. Do not multiply rules for examples of the same principle.

# Council authority

Follow `COUNCIL.md`: a PM decision is required for every task; invoke only impacted specialist perspectives for routine changes, all eight for an expressly requested full review. Specialists advise, PM resolves trade-offs and stop conditions, without overriding user approval or hard safety requirements. Do not assert independent subagent review unless separate agents actually ran. Avoid architecture theater in the orchestration itself.

# Engineering governance

Start with the smallest observable user outcome. Prefer existing tools over custom software. Use `convergence` to select an appropriate recipe and determine acceptance evidence. Stop when the outcome is verified.

For existing bloated/incomplete repositories choose **core-first recovery**: declare exactly one mission (PROVE_CORE, SHIP_MVP, ADD_FEATURE), classify current runtime components CORE / REQUIRED / DEFER / REMOVE, and disconnect speculative nonessential surface in reversible changes. Burden of proof is on retaining it in the MVP. Preserve data, essential security, existing proven flows, and rollback. Do not redesign as a substitute for delivering a usable core.

For substantive code tasks establish bounded contracts before implementation. Do not silently expand their scope. Use scope checks where integrated, plus functional and regression tests. The path guard cannot prove architectural quality or correct behavior.

Do not add infrastructure, dependencies, agents, abstraction layers, or unrelated refactoring without a concrete present requirement. Keep simple adapters separate from consumers where justified, without generalized frameworks. After two failed attempts at the same criterion, reassess the strategy. End with ADOPT, FIX, PIVOT, or ABANDON.

These rules govern this repository itself. New machinery requires observed failure of a simpler approach.

## Use established frameworks; never invent speculative internal frameworks

Use established frameworks and libraries when they are a good fit (such as React or FastAPI). We build bounded applications and small independent capabilities, not a general-purpose internal platform. Five distinct responsibilities may be five ordinary modules. Communicate through the smallest explicit contract; avoid shared infrastructure unless concrete current consumers require it. Do not invent plugin systems, registries, factories, event buses, service meshes, configurable pipelines, dependency-injection frameworks, or extensibility layers for hypothetical needs. An adapter may be a single file or function, separated from its consumer without introducing a framework. Extract shared mechanisms only from demonstrated repeated needs. Do not spend delivery time discussing hypothetical future architectures. Defer decisions not required for the current acceptance criteria. Any internal framework-like abstraction needs a current, demonstrated requirement and an approved scope change; security and reliability obligations still apply. Once acceptance passes, ship and stop.

## Read → Map → Test → Change → Verify (mandatory for code edits)

Before editing existing source, read the **entire relevant file** (in manageable contiguous chunks if needed), including imports, exports, side effects and callers. Do not substitute grep, regex, symbol search, or snippets for understanding the file. Search is for locating candidates and references **after** establishing context, not proof of behavior. For huge/generated/binary files, read the relevant hand-written source and contracts instead; state any coverage limits. Do not dump irrelevant files just to satisfy this rule.

Map the change's dependencies and consumers, then identify which existing tests protect the behavior. If none exists, add the smallest meaningful regression/acceptance test before changing behavior (when technically feasible). Reproduce failures when fixing bugs. Make the smallest scoped modification, exercise the requested behavior, run relevant regression tests, fix introduced regressions, and report what was actually verified. If tests cannot run, report the blocker; never silently label the change complete. No speculative tests for imaginary requirements.

## Model the domain, do not multiply it

Before adding a domain, entity, service, function, or contract, check whether the behavior is simply data or a parameter of an existing owner. Prefer one existing operation with explicit parameters/variants over duplicated functions or a new abstraction layer. An absence period belonging to a teacher is ordinarily teacher-owned data, not automatically an independent "Unavailability domain" with its own service and identity. Use a separate entity only when its independent identity, lifecycle, cross-owner relations, permission boundary, or other concrete requirements justify it. Keep domain boundaries about real responsibilities, not every noun in the requirements. Never conflate database row IDs with a need for a separate domain.

## Defer the abstraction; accept the migration

Model today's demonstrated requirements, not hypothetical tomorrow requirements. Do not create an independent entity, service, domain, adapter hierarchy or migration framework solely to avoid the possibility of future migration. If future needs establish independent identity, lifecycle or ownership, introduce that structure **then**, with a scoped and tested migration. A future migration is not automatically technical debt. Preserve accurate data and current invariants today; do not sacrifice current correctness or security for minimalism.

## Deadline-driven convergence

When the user sets a deadline, inspect the existing code before estimating. Design the smallest complete acceptance path fitting the timebox, state concrete assumptions and acceptable trade-offs, and avoid padding estimates with hypothetical architecture. Preserve essential safety and functional tests. A partial oversized solution is not a substitute for a complete bounded solution; flag genuine infeasibility promptly.

## Contract-driven testing and deliberate test retirement

Every meaningful behavior change needs a focused executable test with a short explanation of the contract protected and the failure it detects. For a transport-to-consumer boundary, a small mock producer and asserted consumer output is enough. Do not build a generic testing infrastructure. On any red test, decide REPAIR (contract still valid), UPDATE (approved changed requirement, new coverage), or RETIRE (obsolete feature explicitly disconnected). Never blindly repair a test for abandoned functionality or suppress a failing assertion without retiring its contract and checking surviving regressions. All applicable tests must pass before ADOPT.

## Independently test every active boundary

Before changing or adding a stage, define observable input/output behavior and create the smallest deterministic fixture/generator plus checker that catches wrong output. Test that stage locally without production hardware where feasible, then run relevant integration and real-world checks. Include failure modes proportional to risk. On retrofit, mark untested critical edges UNVERIFIED and backfill the smallest boundary test before feature expansion. Simulated success does not equal validated production hardware. Read `docs/boundary-verification.md`; no global simulator.
