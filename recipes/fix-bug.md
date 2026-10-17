# Fix bug
**When:** Existing documented or observed behavior is wrong.
**Decide:** Reproduce the defect, define the expected behavior, identify the smallest root cause.
**Build:** Prefer a failing regression test before changing code; repair the cause without adjacent redesign.
**Verify:** Regression test passes; relevant surrounding behavior remains intact.
**Stop:** Original reproduction no longer fails and the fix is verified.
