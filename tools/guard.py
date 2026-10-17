#!/usr/bin/env python3
"""Minimal, dependency-free scope guard. Run from the target Git repository."""
import argparse
import json
import pathlib
import subprocess
import sys


def changed_paths(base):
    output = subprocess.check_output(
        ["git", "diff", "--name-only", "--diff-filter=ACDMRT", f"{base}...HEAD"],
        text=True,
    )
    return [path for path in output.splitlines() if path]


def check(contract, changed):
    errors = []
    allowed = contract.get("allowed_paths", [])
    if not allowed or not isinstance(allowed, list):
        return ["allowed_paths must contain at least one exact file or directory ending in /"]
    if not contract.get("goal") or not contract.get("acceptance"):
        errors.append("goal and acceptance must be present")
    for path in changed:
        if not any(path == item or (item.endswith("/") and path.startswith(item))
                   for item in allowed if isinstance(item, str)):
            errors.append(f"outside scope: {path}")
    for path in contract.get("protected_paths", []):
        if path in changed:
            errors.append(f"protected contract/policy changed: {path}")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("contract", type=pathlib.Path)
    parser.add_argument("--base", required=True, help="trusted base ref, e.g. origin/main")
    args = parser.parse_args()
    data = json.loads(args.contract.read_text(encoding="utf-8"))
    failures = check(data, changed_paths(args.base))
    if failures:
        print("\n".join(f"FAIL: {item}" for item in failures))
        return 1
    print("PASS: modified paths within contract. Acceptance tests are NOT verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
