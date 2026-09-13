"""Portable structure checks; does not claim model behavior validation."""
from pathlib import Path
import json
import re


def validate(root):
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError("missing frontmatter")
    metadata = dict(line.split(":", 1) for line in parts[1].splitlines() if ":" in line)
    if metadata.get("name", "").strip() != "coordinator-executor-reviewer-workflow":
        raise ValueError("unexpected skill name")
    if not metadata.get("description", "").strip():
        raise ValueError("missing description")
    for file in root.rglob("*.md"):
        body = file.read_text(encoding="utf-8")
        if sum(line.startswith("```") for line in body.splitlines()) % 2:
            raise ValueError(f"unclosed code fence: {file}")
        for target in re.findall(r"\]\(([^)]+)\)", body):
            if "://" in target or target.startswith("#"):
                continue
            path = target.split("#", 1)[0]
            if not (file.parent / path).is_file():
                raise ValueError(f"missing reference: {file}: {target}")
    spec = json.loads((root / "evals/evals.json").read_text(encoding="utf-8"))
    cases = spec["evals"]
    if not cases or len({c["id"] for c in cases}) != len(cases):
        raise ValueError("empty or duplicate evaluation IDs")
    if len({c["name"] for c in cases}) != len(cases):
        raise ValueError("duplicate evaluation names")
    for case in cases:
        if not all(case.get(key) for key in ("prompt", "expected_output", "assertions")):
            raise ValueError("incomplete evaluation")
    return {"structure": "PASS", "scenario_specs": len(cases),
            "runtime_lines": len(text.splitlines()), "behavior_tested": False}


if __name__ == "__main__":
    print(json.dumps(validate(Path(__file__).resolve().parents[1]), indent=2))
