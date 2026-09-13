"""Regression tests that corrupt saved evidence to challenge the checker."""
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from check_artifact_trial import check

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "evals/fixtures/artifact-task"
TRIAL = ROOT / "evals/results/artifact-smoke/candidate"


class TrialCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "trial"
        shutil.copytree(TRIAL, self.root)

    def test_valid_saved_output(self):
        self.assertTrue(all(check(self.root, FIXTURE).values()))

    def test_empty_deliverable_is_rejected_even_with_success_report(self):
        (self.root / "outputs/summary.md").write_text("")
        result = check(self.root, FIXTURE)
        self.assertFalse(result["complete_reconciled_table"])
        self.assertFalse(result["written_total_reconciles"])

    def test_changed_total_is_rejected(self):
        p = self.root / "outputs/summary.md"
        p.write_text(p.read_text().replace("670.00", "510.00"))
        self.assertFalse(check(self.root, FIXTURE)["written_total_reconciles"])

    def test_invented_release_readiness_is_rejected(self):
        p = self.root / "outputs/decision.json"
        d = json.loads(p.read_text()); d["external_release_ready"] = True
        p.write_text(json.dumps(d))
        self.assertFalse(check(self.root, FIXTURE)["external_dependency_preserved"])

    def test_changed_approval_input_is_rejected(self):
        (self.root / "inputs/approval.json").write_text('{"status":"approved"}')
        self.assertFalse(check(self.root, FIXTURE)["inputs_preserved"])


if __name__ == "__main__":
    unittest.main()
