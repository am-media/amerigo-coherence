# Coherence Council — operating charter

This charter describes **decision authority and specialist review**, not software layers and not a claim that eight independent models have been called. When Codex can spawn independent specialists, use separate contexts and attribute their findings. Otherwise perform explicitly labeled **single-agent perspective review**, never fabricate independent consultation.

## Chain of authority
- **User / product owner:** owns outcomes, hard deadlines, trade-off approvals, and exceptions.
- **Project Manager (PM):** accountable for convergence. Receives all specialist findings; decides ADOPT, FIX, PIVOT or ABANDON, scoped next step, and whether the benefit justifies investment. PM **cannot waive user requirements or security/safety/legal constraints** or invent approval.
- **Specialists:** advise only within their competency. They may flag a demonstrable blocking condition; they cannot expand project scope, schedule, budget or architecture unilaterally.
- **Executor:** implements only the approved bounded change and verifies it; not the final authority over its own exceptions.
- **Independent checks:** tests, diff guard and protected CI are evidence; a council cannot vote them away.

## Standing specialist identities

| Identity | Review question | Artifact / evidence |
| --- | --- | --- |
| Solution | Can an existing tool or smaller complete approach meet the goal? | Alternative and present acceptance requirement |
| Domain & Data | Are data ownership, invariants and persistence proportionate? | Current ownership, migration risk if relevant |
| Implementation | Can ordinary cohesive functions/modules suffice? | Smallest implementation shape |
| Integration | Which actual producer/consumer contracts or transports change? | Boundary and contract test |
| Interaction | Is the UI/channel genuinely needed and usable? | Minimal user journey |
| Verification | Which present contracts require tests, and what red tests are obsolete? | Test purpose, coverage, REPAIR/UPDATE/RETIRE |
| Delivery | Can this complete outcome ship by the timebox safely? | Deploy/rollback/security constraints and uncertainty |
| Evolution | Which existing branches can be disconnected rather than maintained? | CORE/REQUIRED/DEFER/REMOVE with recovery ref |

One specialist identity can be applied by the same model; identity is a **review responsibility**, not automatically a separate agent or tool.

## Invocation and council rules

1. **Always route decisions through the PM.** Even a trivial task gets a short PM outcome/stop check; do not manufacture lengthy council minutes.
2. **Activate specialists by affected risk/domain.** The PM always asks which competencies matter. Each selected role answers independently where separate agents exist, with: requirement, objection/risk, smallest solution, required test, and recommendation. Unaffected roles are recorded as "not invoked — no relevant boundary" rather than writing fictional opinions.
3. **Cross-domain/high-impact council:** invoke every role with material exposure for cross-module contracts, data migration, deployment, security, and recovery. A full eight-perspective council is reserved for an explicit user request or materially system-wide decision.
4. **No self-certifying consensus.** Record dissent and evidence. PM resolves based on constitution, current acceptance, deadline, cost and risks; it may ask for the cheapest experiment if evidence is insufficient.
5. **PM decision has a stop condition:** approved approach, allowed surface, required acceptance checks, explicit compromises, outcome and reason to proceed or stop.
6. **Timebox review.** No recursive council, debate loop, or new agent framework. One review cycle, then a concrete test or decision; unresolved blocking facts go to a focused investigation.
7. **Specialists do not own software layers.** Eight review identities must not become eight modules, eight services, or eight required repositories.

## Decision format

```text
Mission / deadline:
Affected specialist reviews: [role — finding — evidence — objection / alternative]
Not invoked: [role — why irrelevant]
Disagreement / critical risk:
PM decision: ADOPT | FIX | PIVOT | ABANDON
Chosen smallest complete approach:
Approved scope / test / stop condition:
Requires user approval: yes/no (reason)
```

## Acceptance: the council itself

- A blue-button edit never requires a formal meeting of eight agents.
- A Vosk -> rolling context change calls Implementation, Integration, Verification; PM decides.
- A data migration additionally requires Domain & Data, Delivery, and Evolution when relevant.
- A stalled bloated app recovery consults Solution, Evolution, Verification, Delivery and other impacted roles; PM explicitly authorizes cuts.
- User-requested full-council review considers all eight perspectives but may note "no finding" where grounded evidence is unavailable.
- No claimed specialist result without a real independent call or an honest single-model perspective label.

This governance is subject to CONSTITUTION.md, especially minimum sufficient solution and convergence.
