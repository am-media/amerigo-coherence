# Engineering governance

Before development, identify the smallest observable outcome. Prefer using or configuring an existing tool to writing software. Use the `convergence` skill to select a recipe and define acceptance criteria. Keep changes confined to the task; do not introduce dependencies, architecture or unrelated refactoring without explicit approval. Verify behavior before declaring completion. Stop when acceptance criteria are met; report anything not verified. Do not treat passing unit tests as proof of end-to-end acceptance.

These principles also govern changes to this repository: add no agent, service, dependency, or recipe without a recurring demonstrated need. Ponytail can guide implementation if installed; it is not required to run this repository.
