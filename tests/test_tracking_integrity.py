"""Tests for local task-register structure; no GitHub status is inferred."""
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_tracking", ROOT / "scripts/check_tracking.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


def row(key, number, owner="parmtech", target=None):
    target = number if target is None else target
    return f"| {key} | [#{number}](https://github.com/{owner}/TongNet/issues/{target}) | G0 |"


def fixture():
    return "\n".join([row("TN-SEC-004", 3)] + [row(f"TN-X-{n:03}", n) for n in range(24, 48)])


class TrackingStructureTests(unittest.TestCase):
    def test_current_register_and_legacy_owner_are_accepted(self):
        self.assertEqual(checker.validate_task_rows(fixture()), [])
        self.assertEqual(checker.validate_task_rows(fixture().replace("parmtech", "manbir6-ux")), [])
        self.assertEqual(checker.validate_task_rows((ROOT / "tracking/TASKS.md").read_text(encoding="utf-8")), [])

    def test_missing_and_duplicate_rows_fail(self):
        lines = fixture().splitlines()
        self.assertTrue(checker.validate_task_rows("\n".join(lines[:-1])))
        lines[-1] = lines[-2]
        self.assertTrue(checker.validate_task_rows("\n".join(lines)))

    def test_wrong_owner_or_mismatched_issue_fails(self):
        self.assertTrue(checker.validate_task_rows(fixture().replace("parmtech", "other", 1)))
        self.assertTrue(checker.validate_task_rows(fixture().replace("issues/24)", "issues/25)", 1)))

    def test_missing_required_file_is_detected(self):
        original = checker.REQUIRED
        try:
            checker.REQUIRED = original + ("definitely-missing-file",)
            self.assertTrue(any("definitely-missing-file" in e for e in checker.validate()))
        finally:
            checker.REQUIRED = original


if __name__ == "__main__":
    unittest.main()
