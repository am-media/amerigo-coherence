# Core-first recovery decision

Mission (choose one): PROVE_CORE / SHIP_MVP / ADD_FEATURE
One-sentence user outcome:
Critical end-to-end acceptance path:
Evidence required:
Stop condition:
Baseline Git ref and recovery ref:
Data/security/operational invariants:

## Active surface
| Component/path | CORE / REQUIRED / DEFER / REMOVE | Evidence for keeping active | Isolation action |
| --- | --- | --- | --- |

## First reversible cut
Allowed paths:
What is disconnected:
Regression and acceptance commands:
Rollback:
Outcome: ADOPT / FIX / PIVOT / ABANDON

Rule: a component without present necessity must justify remaining connected; never assume an unknown runtime dependency is safe to cut.
