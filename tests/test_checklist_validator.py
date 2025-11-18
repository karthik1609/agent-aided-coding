import json
from pathlib import Path
import tempfile

import pytest

from scripts import checklist_validator as cv


def write_yaml(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def test_valid_checklist(tmp_path: Path):
    p = tmp_path / "valid.yaml"
    content = """
id: feature-1
title: Valid
items:
  - id: plan-1
    description: ok
    status: planned
    review: null
    implemented: false
    tests:
      status: pending
      last_run: null
      artifacts: []
last_updated: 2025-01-01T00:00:00Z
"""
    write_yaml(p, content)
    count, diags = cv.validate_files([str(p)])
    assert count == 0
    assert diags == []


def test_schema_missing_fields(tmp_path: Path):
    p = tmp_path / "bad_schema.yaml"
    content = """
id: feature-2
items:
  - id: plan-1
    description: missing tests and status
"""
    write_yaml(p, content)
    count, diags = cv.validate_files([str(p)])
    assert count > 0
    assert any("missing fields" in d.lower() or "missing" in d.lower() for d in diags)


def test_gate_violation_requires_tests_and_review(tmp_path: Path):
    p = tmp_path / "gate_fail.yaml"
    content = """
id: feature-3
items:
  - id: plan-1
    description: implemented but no tests pass or review
    status: implemented
    review: null
    implemented: true
    tests:
      status: fail
      last_run: 2025-01-01T00:00:00Z
      artifacts: []
last_updated: 2025-01-01T00:00:00Z
"""
    write_yaml(p, content)
    count, diags = cv.validate_files([str(p)])
    assert count > 0
    assert any("tests.status != 'pass'" in d or "review != 'pass'" in d for d in diags)
