#!/usr/bin/env python3
"""
Simple checklist validator for docs/checklists YAML files.

Usage:
  python3 scripts/checklist_validator.py docs/checklists
  python3 scripts/checklist_validator.py path/to/file.yaml
  (CI) export ADVISORY=true to run in advisory mode (non-failing).
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

import yaml

REQUIRED_ITEM_FIELDS = {"id", "description", "status", "tests"}
GATING_STATUSES = {"implemented", "tested", "done"}


def load_yaml(path: Path) -> Dict[str, Any]:
    raw = path.read_text(encoding="utf-8")
    return yaml.safe_load(raw) or {}


def validate_schema(doc: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    if "id" not in doc:
        errors.append("Missing top-level 'id' field.")
    if "items" not in doc or not isinstance(doc["items"], list):
        errors.append("Missing or invalid top-level 'items' list.")
        return errors

    for idx, item in enumerate(doc.get("items", []), start=1):
        if not isinstance(item, dict):
            errors.append(f"Item #{idx} is not a mapping.")
            continue
        missing = REQUIRED_ITEM_FIELDS - item.keys()
        if missing:
            errors.append(f"Item '{item.get('id', f'#{idx}')}' missing fields: {', '.join(sorted(missing))}.")
        tests = item.get("tests")
        if tests is None or not isinstance(tests, dict):
            errors.append(f"Item '{item.get('id', f'#{idx}')}' has invalid or missing 'tests' block.")
        else:
            if "status" not in tests:
                errors.append(f"Item '{item.get('id', f'#{idx}')}' tests block missing 'status'.")
    return errors


def validate_gates(doc: Dict[str, Any]) -> List[str]:
    errors: List[str] = []
    for item in doc.get("items", []):
        status = item.get("status")
        if status in GATING_STATUSES:
            tests_status = item.get("tests", {}).get("status")
            review_status = item.get("review")
            if tests_status != "pass":
                errors.append(
                    f"Item '{item.get('id')}' has status '{status}' but tests.status != 'pass' (found: {tests_status})."
                )
            if review_status != "pass":
                errors.append(
                    f"Item '{item.get('id')}' has status '{status}' but review != 'pass' (found: {review_status})."
                )
    return errors


def find_checklist_files(paths: List[str]) -> List[Path]:
    ret: List[Path] = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            for f in sorted(path.glob("*.yaml")):
                ret.append(f)
        elif path.is_file():
            ret.append(path)
        else:
            # glob maybe pattern
            for f in sorted(Path('.').glob(p)):
                ret.append(f)
    return ret


def validate_files(paths: List[str]) -> Tuple[int, List[str]]:
    files = find_checklist_files(paths)
    overall_errors: List[str] = []
    for f in files:
        try:
            doc = load_yaml(f)
        except Exception as exc:
            overall_errors.append(f"{f}: failed to parse YAML: {exc}")
            continue
        schema_errs = validate_schema(doc)
        gate_errs = validate_gates(doc)
        if not schema_errs and not gate_errs:
            print(f"[OK] {f}")
        else:
            overall_errors.append(f"--- {f} ---")
            overall_errors.extend(schema_errs)
            overall_errors.extend(gate_errs)
    return (len(overall_errors), overall_errors)


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", help="Files or directories to validate (e.g. docs/checklists).")
    parser.add_argument(
        "--files-list",
        help="Optional newline-separated file list (useful for CI).",
    )
    args = parser.parse_args(argv)

    paths = args.paths[:]
    if args.files_list:
        listed = Path(args.files_list).read_text(encoding="utf-8").splitlines()
        paths.extend([p for p in listed if p.strip()])

    failure_count, diagnostics = validate_files(paths)
    if diagnostics:
        print("\n".join(diagnostics))

    advisory = os.getenv("ADVISORY", "true").lower() in ("1", "true", "yes")
    if failure_count:
        msg = f"Checklist validation found {failure_count} problem(s)."
        if advisory:
            print("WARNING (advisory mode):", msg)
            return 0
        else:
            print("ERROR:", msg)
            return 2
    print("All checklists validated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
