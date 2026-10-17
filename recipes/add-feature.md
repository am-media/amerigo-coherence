# Add feature
**When:** An existing system needs a bounded additional behavior.
**Decide:** Identify the existing module/API and the specific user-visible change.
**Build:** Touch only relevant code; reuse the established design; no new layer, framework or dependency without proven need and approval.
**Verify:** Targeted tests, appropriate regression checks, and a functional acceptance test.
**Stop:** The behavior works and relevant regressions are absent; separate enhancement ideas.

**Domain/contract economy:** When behaviors differ only by a tag or option, use one function with an explicit parameter, not duplicated functions or a new abstraction hierarchy. Store teacher unavailability as teacher-owned data unless independent lifecycle, rules, or relationships demonstrably require a separate domain. Review existing consumers before changing contracts.
