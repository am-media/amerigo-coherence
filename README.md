# Amerigo Coherence — Convergence V0

Decision recipes for outcome-first development with Codex. The goal is to **finish useful work** rather than maximize code or architectural sophistication.

## What it does

- Prompts Codex to choose an existing tool before a new application.
- Selects one of five small procedures to bound development.
- Defines observable acceptance criteria and an explicit stopping condition.
- Provides five human-reviewed test scenarios for checking the method itself.

## Use in Codex

1. Keep this repository under version control; `AGENTS.md` governs work performed **in this repository**.
2. Install `skills/convergence` as a Codex skill in your environment, or copy its folder to your Codex skills directory according to your Codex installation's supported configuration.
3. For other repositories, add a short reference in their `AGENTS.md` instructing Codex to use the Convergence skill for planning and implementation.
4. For a substantive task, copy `templates/task.yaml` into the project or use the same contract inline. Select one recipe and verify the actual behavior.
5. Run the prompts in `tests/scenarios.yaml` to check for drift. Record observed outcomes; the YAML is **not** an automated eval suite.

## Scope and limitations

V0 contains no orchestrator, database, hooks or runtime enforcement. Instructions can be ignored by a model; critical scope and architecture rules require permissions, CI, or protected branches. Ponytail is complementary but is not bundled or installed by this repository. No automatic account-wide distribution is claimed.

## Definition of done for V0

The repository is complete once the skill, five recipes, task template, five reproducible manual scenarios, and usage instructions are present and structurally validated. Behavioral effectiveness requires running the scenarios in a real Codex environment and is **not claimed** until then.

## Contribution rule

No new recipe until an existing recipe demonstrably fails on a recurring case. No new tool until manual evaluation is demonstrably insufficient.
