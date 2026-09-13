"""A local deterministic event fixture; not an actual worker platform."""
import json
import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent
PATH = ROOT / "service-state.json"
INITIAL = {"phase": "executing", "event": 0, "executor": "running", "reviewer": "idle", "checkpoint_due": False, "approval": "pending"}
s = json.loads(PATH.read_text()) if PATH.exists() else dict(INITIAL)
action = sys.argv[1]
if action == "advance":
    s["event"] += 1
    if s["phase"] == "executing" and s["event"] == 1:
        s["note"] = "Worker is reading inputs; no new output yet; checkpoint not due."
    elif s["phase"] == "executing" and s["event"] >= 2:
        (ROOT / "deliverable.md").write_text("# Introduction\nPrepared section.\n")
        s.update(phase="reported_complete", executor="completed", claimed_complete=True)
    elif s["phase"] == "repairing":
        (ROOT / "deliverable.md").write_text("# Introduction\nPrepared section.\n# Conclusion\nChecked complete.\n")
        s.update(phase="reported_complete", executor="completed", claimed_complete=True)
    elif s["phase"] == "reviewing":
        s.update(phase="reviewed", reviewer="completed", verdict="HOLD", reason="external approval pending; both required sections verified")
elif action == "resume":
    s.update(phase="repairing", executor="running", claimed_complete=False)
elif action == "review":
    s.update(phase="reviewing", reviewer="running")
elif action == "pause":
    s["paused"] = True
elif action not in ("status", "message"):
    raise SystemExit("unsupported command")
PATH.write_text(json.dumps(s, indent=2) + "\n")
with (ROOT / "events.jsonl").open("a") as f:
    f.write(json.dumps({"action": action, "state": s}) + "\n")
print(json.dumps(s))
