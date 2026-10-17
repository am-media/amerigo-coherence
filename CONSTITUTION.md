# Coherence Constitution

This document governs **every technical decision**, independent of technology, domain or project phase. Recipes and skills implement these principles; they cannot override them.

## I. Outcome sovereignty
Define the smallest observable outcome and how to prove it before choosing technology. Functioning software is the deliverable, not architecture.

## II. Minimum sufficient solution
Among solutions that meet current functional, security, reliability and operational needs, prefer the one with the lowest *total* implementation, integration and maintenance burden. An existing tool or a small local UI may beat a web stack. More lines are justified only when they reduce real overall risk/cost.

## III. Burden of proof
Every nontrivial component, framework-like layer, service or abstraction must point to a **present requirement** it satisfies. A technically plausible rationale alone is insufficient if a simpler alternative meets the same requirement. Ask:
1. Which current acceptance criterion needs this?
2. What verifiably breaks without it?
3. What simpler existing alternative satisfies the same criterion?
If a simpler adequate alternative exists, choose it.

## IV. No speculative engineering
Do not pay today for hypothetical future extensibility, scalability, migrations or integrations. Refactor or migrate when a real requirement arrives. Keep present data integrity and safety intact. Use established frameworks when they are the simplest fit; do not create internal frameworks.

## V. Understand before changing
Read the entire relevant human-authored source file, trace consumers and side effects, locate or add focused tests where feasible, edit minimally, verify the requested path and regressions. Search results are pointers, not comprehension.

## VI. Convergence is mandatory
Stop when the acceptance evidence is met and no blocking risk remains. After two unsuccessful attempts at the same criterion, reassess the approach rather than adding layers. Future enhancements are separate tasks.


## VII. Deadline sovereignty
A user-declared deadline is an architectural constraint, not a target to ignore. Estimate from inspected existing code, a complete user journey, actual integration needs and observed uncertainty—not speculative architecture or arbitrary safety padding. When time is bounded, find the smallest **complete** solution that meets acceptance criteria within it; do not deliver a fraction of an overbuilt plan. Explicitly propose trade-offs in scope, polish and extensibility, but do not silently remove essential behavior, security, correctness or verification. If no viable solution fits, say so promptly and identify the blocking requirement. State confidence and assumptions; never present uninspected guesses as objective estimates.

## Conflict and exceptions
Present correctness, security, legal requirements and operational reliability are **requirements**, not optional complexity. If two approaches are genuinely tied or uncertain, run the cheapest reversible experiment. Exceptions to these principles need a named present requirement and explicit scope approval, not a hypothetical possibility.

## Constitutional self-application
These same rules govern Coherence. Do not add rules for each technology or create a decision framework to enforce this constitution when a concise checklist and existing tests suffice.
