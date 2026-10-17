# Engineering governance

Before development, identify the smallest observable outcome. Prefer using or configuring an existing tool to writing software. Use the `convergence` skill to choose a recipe and define acceptance evidence.

For substantive code tasks: establish a bounded task contract **before implementation**. Do not broaden its allowed paths, acceptance criteria, or goal to justify work already performed. If scope must change, propose a separately reviewed contract change. Use the guard in `tools/guard.py` where the target repository has a JSON contract; project CI and branch protection must keep its policy independently enforceable.

Respect existing module boundaries. Do not add dependencies, architecture, or unrelated refactoring without explicit approval. After two failed attempts at the same criterion, reconsider strategy rather than growing the solution. At every stopping point choose ADOPT, FIX, PIVOT, or ABANDON based on evidence; stop on ADOPT.

These rules apply to this repository. Add no new agent, service, dependency, or recipe without a recurring demonstrated need. Ponytail may complement implementation, but is not bundled.
