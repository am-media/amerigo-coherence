#!/usr/bin/env python3
"""Read-only reconnaissance for an existing Git repository. No dependencies."""
import argparse
import json
import pathlib
import subprocess
from collections import Counter

IGNORED = ("node_modules/", "vendor/", "dist/", "build/", ".next/", ".git/")
MANIFESTS = {"package.json", "pyproject.toml", "requirements.txt", "Cargo.toml",
             "go.mod", "pom.xml", "composer.json"}
MARKERS = ("TODO", "FIXME", "HACK")


def inventory(root, paths, limit=12):
    items, markers, manifests = [], [], []
    for name in paths:
        if any(name == prefix.rstrip("/") or name.startswith(prefix) for prefix in IGNORED):
            continue
        path = root / name
        if not path.is_file() or path.is_symlink():
            continue
        size = path.stat().st_size
        items.append({"path": name, "bytes": size})
        if path.name in MANIFESTS:
            manifests.append(name)
        if size <= 128000 and path.suffix in {".py", ".js", ".jsx", ".ts", ".tsx", ".go", ".rs"}:
            try:
                for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    if any(marker in line for marker in MARKERS):
                        markers.append({"path": name, "line": lineno, "marker": line.strip()[:100]})
                        if len(markers) >= 40:
                            break
            except UnicodeError:
                pass
    suffixes = Counter(pathlib.PurePosixPath(x["path"]).suffix or "[no extension]" for x in items)
    return {
        "status": "evidence_only_not_an_unused_code_detector",
        "tracked_files": len(items),
        "largest_files": sorted(items, key=lambda x: x["bytes"], reverse=True)[:limit],
        "file_types": dict(suffixes.most_common(10)),
        "dependency_manifests": sorted(manifests),
        "maintenance_markers": markers[:40],
        "next_steps": [
            "Identify a working baseline and critical user journeys",
            "Run existing build/tests and document failures",
            "Review large files, manifests and markers as hypotheses, not defects",
            "Propose one scoped reversible cleanup with regression evidence",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=pathlib.Path, default=pathlib.Path("."))
    parser.add_argument("--output", type=pathlib.Path)
    args = parser.parse_args()
    root = args.root.resolve()
    result = subprocess.run(["git", "-C", str(root), "ls-files", "-z"],
                            capture_output=True, check=True)
    paths = [x.decode("utf-8") for x in result.stdout.split(b"\0") if x]
    report = json.dumps(inventory(root, paths), indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.write_text(report, encoding="utf-8")
    else:
        print(report, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
