#!/usr/bin/env python3
"""Fail-fast structural check of TongNet's evidence-first, issue-backed project control.

This script does NOT verify blockchain correctness or query issue state;
GitHub Issues remain authoritative. Python standard library only.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md",
    "tracking/README.md",
    "tracking/TASKS.md",
    "tracking/HANDOFF.md",
    "tracking/CURRENT_STATUS.md",
    "tracking/DAILY_LOG.md",
    "tracking/DECISIONS.md",
    "tracking/RISKS.md",
    "docs/WHITEPAPER_MASTER_V1_1_SECURITY_REVIEW.md",
    "docs/LONG_HORIZON_RISK_AUDIT.md",
    "docs/LONG_HORIZON_AUDIT_SUPPLEMENT.md",
    "docs/BUILD_EXECUTION_PLAN.md",
    "docs/DECISION_REGISTER_CURRENT.md",
    ".github/workflows/project-tracking.yml",
    ".github/workflows/status-sync.yml",
    ".github/scripts/build_status.py",
)

EXPECTED_TASKS = {
    "TN-GOV-001": 24, "TN-ARC-001": 25, "TN-SEC-001": 26, "TN-SEC-002": 27,
    "TN-SEC-003": 28, "TN-SEC-004": 3, "TN-SPEC-001": 29, "TN-SPEC-002": 30,
    "TN-SPEC-003": 31, "TN-SPEC-004": 32, "TN-SPEC-005": 33, "TN-MONEY-001": 34,
    "TN-ENG-001": 35, "TN-TEST-001": 36, "TN-CONS-001": 37, "TN-CONS-002": 38,
    "TN-ECON-001": 39, "TN-ENG-002": 40, "TN-ENG-003": 41, "TN-OPS-001": 42,
    "TN-TEST-002": 43, "TN-NET-001": 44, "TN-LEGAL-001": 45, "TN-LAUNCH-001": 46,
    "TN-MAINT-001": 47,
}

def validate_task_rows(text: str) -> list[str]:
    """Validate local register structure, not the live state of GitHub issues."""
    errors: list[str] = []
    rows = re.findall(
        r"(?m)^\|\s*(TN-[A-Z]+-\d{3})\s*\|\s*\[#(\d+)\]\(https://github\.com/([^/]+)/TongNet/issues/(\d+)\)",
        text,
    )
    if len(rows) != 25:
        errors.append(f"Expected 25 canonical task rows, found {len(rows)}.")
    seen_ids: set[str] = set()
    seen_numbers: set[int] = set()
    for key, number, owner, tail in rows:
        if owner not in {"parmtech", "manbir6-ux"}:
            errors.append(f"Unexpected issue owner for {key}: {owner}")
        if key in seen_ids or int(number) in seen_numbers:
            errors.append(f"Duplicated task key or issue number: {key}/#{number}")
        if EXPECTED_TASKS.get(key) != int(number):
            errors.append(f"Unexpected canonical mapping for {key}: #{number}")
        if number != tail:
            errors.append(f"Broken issue number mapping for {key}: #{number} vs #{tail}")
        seen_ids.add(key)
        seen_numbers.add(int(number))
    expected_numbers = set(EXPECTED_TASKS.values())
    if seen_numbers != expected_numbers:
        errors.append("Canonical issue numbers must be #3 and #24â€“#47.")
    return errors


def validate() -> list[str]:
    errors = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    tasks = ROOT / "tracking/TASKS.md"
    if tasks.exists():
        text = tasks.read_text(encoding="utf-8")
        errors.extend(validate_task_rows(text))
    for relative in ("tracking/HANDOFF.md", "tracking/DAILY_LOG.md"):
        p = ROOT / relative
        if p.exists():
            t = p.read_text(encoding="utf-8")
            if "2026-10-25" not in t:
                errors.append(f"Missing dated project kickoff entry: {relative}")
    for relative in ("tracking/DECISIONS.md", "tracking/RISKS.md"):
        p = ROOT / relative
        if p.exists() and len(p.read_text(encoding="utf-8")) < 400:
            errors.append(f"Risk/decision register suspiciously short: {relative}")
    return errors


if __name__ == "__main__":
    errors = validate()
    if errors:
        print("Tracking consistency FAILED:")
        for e in errors:
            print(f"ERROR: {e}")
        sys.exit(1)
    print("Tracking consistency PASS: core files, task links and journals present.")
    print("NOTE: This is structural validation only, NOT smart-contract, crypto, or issue-acceptance testing.")
