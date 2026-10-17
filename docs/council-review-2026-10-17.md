# Council review — governance consolidation (2026-10-17)

This is a **structured single-model review across specialist perspectives**, not eight independently executed agents. It reviews the Coherence rules and their proposed council governance, not the live behavior of Codex on production repositories.

| Specialist | Verdict | Objection or lesson | Required change |
| --- | --- | --- | --- |
| Solution | Support with condition | Full council on every task defeats minimalism | PM routes only impacted skills |
| Domain & Data | Support | A specialist must not turn every noun into a domain | Keep domain economy and present ownership |
| Implementation | Support | Eight job titles must not become eight architecture layers | Identity refers to review responsibility only |
| Integration | Support | Overformalized contracts lead to buses, adapters and framework bloat | Small typed boundary + contract test |
| Interaction | Support | UI-specialist preference could bias toward web stacks | Compare local and existing UI first |
| Verification | Support with condition | Review consensus cannot prove runtime correctness | Tests and evidence independent of opinions |
| Delivery | Support with condition | Council latency can violate one-day delivery | Review timebox and PM go/no-go |
| Evolution | Support | Existing infrastructure will otherwise be defended by its owner | DEFER / REMOVE actively with rollback |

## Dissent and resolution

**Dissent:** A literal nine-person meeting for every code change conflicts with the constitution's minimum-sufficient solution and deadline rules.

**PM verdict: ADOPT WITH BOUNDED GOVERNANCE.** Every task gets a PM investment and stop decision. Specialists have named, attributable perspectives; only those relevant to the changed boundaries are convened for routine tasks. When the user explicitly requests a full council, all eight perspectives are reviewed. Specialist advice is not a veto except when the evidence reveals an unaddressed hard user, safety, security or correctness constraint. Protected verification remains external to the council.

**Scope:** documentation, skill routing, manual evaluation scenarios. No agent framework, scheduler, database, service, plugin registry or new test runner.

**Acceptance evidence:** documents in repository and existing CI unit tests. Eight genuinely independent Codex subagents and the council's behavior on real user tasks are **not yet validated**.

**Stop condition:** publish a reviewable PR and do not extend scope to build orchestration until a Codex integration test establishes a real gap.
