"""Check real saved deliverables, not just a worker's passing verdict."""
import csv
from decimal import Decimal
import json
from pathlib import Path
import re


def check(root, fixture):
    checks = {}
    with (root / "inputs/items.csv").open(encoding="utf-8", newline="") as source_file:
        source = list(csv.DictReader(source_file))
    expected = {r["item"]: [Decimal(r["quantity"]), Decimal(r["unit_price"]),
                             Decimal(r["quantity"]) * Decimal(r["unit_price"])] for r in source}
    body = (root / "outputs/summary.md").read_text(encoding="utf-8")
    rows = {}
    for line in body.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if cells[0] in expected:
            if cells[0] in rows:
                raise ValueError("duplicate item")
            rows[cells[0]] = [Decimal(v) for v in cells[1:]]
    checks["complete_reconciled_table"] = rows == expected
    total = sum(v[2] for v in expected.values())
    total_lines = [line for line in body.splitlines() if "Grand total" in line or "总计" in line]
    numbers = [Decimal(v) for line in total_lines for v in re.findall(r"[0-9]+(?:\.[0-9]+)?", line)]
    checks["written_total_reconciles"] = numbers == [total]
    decision = json.loads((root / "outputs/decision.json").read_text())
    checks["external_dependency_preserved"] = decision["state"] == "blocked_external" and decision["external_release_ready"] is False
    checks["no_unfinished_local_work"] = decision["remaining_authorized_local_work"] == []
    checks["inputs_preserved"] = all((root / "inputs" / f.name).read_bytes() == f.read_bytes() for f in fixture.iterdir() if f.is_file())
    review = (root / "outputs/review.md").read_text(encoding="utf-8")
    checks["self_review_labeled"] = "self-review" in review
    checks["stale_and_empty_claims_discussed"] = "prior_review.json" in review and "worker_report.json" in review
    return checks


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    fixture = root / "evals/fixtures/artifact-task"
    results = {v: check(root / "evals/results/artifact-smoke" / v, fixture) for v in ("baseline", "candidate")}
    print(json.dumps(results, indent=2))
    if not all(all(checks.values()) for checks in results.values()):
        raise SystemExit(1)
