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
    ".github/workflows/tracking-daily.yml",
    "scripts/daily_snapshot.py",
)

def validate() -> list[str]:
    errors = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            errors.append(f"Missing required file: {relative}")
    tasks = ROOT / "tracking/TASKS.md"
    if tasks.exists():
        text = tasks.read_text(encoding="utf-8")
        rows = re.findall(
            r"(?m)^\|\s*(TN-\d{3})\s*\|\s*\[#(\d+)\]\((https://github\.com/manbir6-ux/TongNet/issues/(\d+))\)",
            text,
        )
        if len(rows) < 23:
            errors.append(f"Only {len(rows)} issue-backed tasks: expected at least 23.")
        seen_ids, seen_numbers = set(), set()
        for key, number, url, tail in rows:
            if key in seen_ids or number in seen_numbers:
                errors.append(f"Duplicated task key or issue number: {key}/#{number}")
            if number != tail:
                errors.append(f"Broken mapping {key} #{number} vs {url}")
            seen_ids.add(key)
            seen_numbers.add(number)
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
