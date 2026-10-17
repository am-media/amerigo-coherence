# Engineering governance

Start with the smallest observable user outcome. Prefer existing tools over custom software. Use `convergence` to select an appropriate recipe and determine acceptance evidence. Stop when the outcome is verified.

For existing bloated/incomplete repositories choose **core-first recovery**: declare exactly one mission (PROVE_CORE, SHIP_MVP, ADD_FEATURE), classify current runtime components CORE / REQUIRED / DEFER / REMOVE, and disconnect speculative nonessential surface in reversible changes. Burden of proof is on retaining it in the MVP. Preserve data, essential security, existing proven flows, and rollback. Do not redesign as a substitute for delivering a usable core.

For substantive code tasks establish bounded contracts before implementation. Do not silently expand their scope. Use scope checks where integrated, plus functional and regression tests. The path guard cannot prove architectural quality or correct behavior.

Do not add infrastructure, dependencies, agents, abstraction layers, or unrelated refactoring without a concrete present requirement. Keep simple adapters separate from consumers where justified, without generalized frameworks. After two failed attempts at the same criterion, reassess the strategy. End with ADOPT, FIX, PIVOT, or ABANDON.

These rules govern this repository itself. New machinery requires observed failure of a simpler approach.

## Use established frameworks; never invent speculative internal frameworks

Use established frameworks and libraries when they are a good fit (such as React or FastAPI). We build bounded applications and small independent capabilities, not a general-purpose internal platform. Five distinct responsibilities may be five ordinary modules. Communicate through the smallest explicit contract; avoid shared infrastructure unless concrete current consumers require it. Do not invent plugin systems, registries, factories, event buses, service meshes, configurable pipelines, dependency-injection frameworks, or extensibility layers for hypothetical needs. An adapter may be a single file or function, separated from its consumer without introducing a framework. Extract shared mechanisms only from demonstrated repeated needs. Do not spend delivery time discussing hypothetical future architectures. Defer decisions not required for the current acceptance criteria. Any internal framework-like abstraction needs a current, demonstrated requirement and an approved scope change; security and reliability obligations still apply. Once acceptance passes, ship and stop.
