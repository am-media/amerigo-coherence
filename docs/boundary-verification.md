# Boundary-first verification

A software boundary is not validated because the author believes it should work. Every meaningful stage must be exercisable with a controlled input and an objectively checkable output, **without requiring the production environment**.

## Before implementing a stage
1. Specify the input contract (shape, units, ordering, timestamps, tolerances), the output contract, and the failure the test must expose.
2. Build the **smallest fit-for-purpose deterministic fixture or generator** that can feed the stage, and an independent checker/assertion for its output. A function, fixture file, fake clock or mock callback may be enough. Do **not** create a global simulator.
3. Start with nominal behavior; exercise material edge cases and failure modes (late packets, missing samples, reordering, restart, etc.) according to the actual risk.
4. Make it repeatable: fixed seed if random, explicit virtual clock when timing matters, known baseline and expected result. Preserve evidence of the test and why it exists.
5. Test component boundaries before relying on end-to-end hardware. Then verify adjacent real interfaces and the production environment. **Synthetic tests do not establish that a real device, OS driver, codec or network behaves identically.**
6. If production uncovers an unmodeled fault, capture a sanitized reproduction, update the fixture/generator and test, then repair the implementation. Do not silently alter the generator to make a failing implementation pass; expected behavior derives from the contract or a justified approved change.

## Risk-guided experimentation
For cheap, reversible, low-impact trials, run a small empirical experiment early rather than prolong speculative discussion. Raise test depth for consequential data loss, security, safety, or time-critical operations. Keep failure injection local and controlled; do not deliberately disrupt live production as a default.

## Example boundaries (not required infrastructure)
- Vosk text -> rolling context: give a known recognized string; assert the consumer receives the expected normalized text and ordering.
- SRT video + 3D camera samples: generate timestamped identifiable video frames and pose samples with known offset/delay/jitter; assert alignment by capture timestamps and declared tolerance, not arrival order.
- Autopilot: first feed a recorded sequence of camera scores/events without any video; then labeled still frames for computer vision; then slide-state fixtures; finally full real streams and stress.

## Retrofit rule
An existing active boundary with no testable input/output contract is **UNVERIFIED**, not automatically broken. Before adding more features across it, provide the smallest representative generator/fixture and output assertion, or explain why it cannot run locally and define an alternative validation gate. Prioritize the critical user journey; do not build simulators for archived/deferred branches. The PM must not approve ADOPT based solely on unverified critical boundaries.

## Acceptance
The correct fixture triggers pass on known good output and fail on deliberately bad output. At least one applicable integration scenario exercises real adjacent components before production release. Production is for last-mile integration and tuning, not first discovery of fundamental logic errors.
