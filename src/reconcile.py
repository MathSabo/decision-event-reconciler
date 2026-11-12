"""Local-only sample reconciler for synthetic credit decision events."""
from __future__ import annotations

import json
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EVENTS = ROOT / "fixtures" / "events.jsonl"
REPORT = ROOT / "reports" / "summary.json"


def reconcile(path: Path = EVENTS) -> dict[str, Any]:
    seen: set[str] = set()
    counts: Counter[str] = Counter()
    duplicates = 0
    total = 0
    for raw in path.read_text(encoding="utf-8").splitlines():
        if not raw.strip():
            continue
        item = json.loads(raw)
        total += 1
        event_id = item["event_id"]
        if event_id in seen:
            duplicates += 1
            continue
        seen.add(event_id)
        counts[item["type"]] += 1
    return {
        "environment": "staging-fixture",
        "records_read": total,
        "unique_events": len(seen),
        "duplicates_ignored": duplicates,
        "events_by_type": dict(sorted(counts.items())),
    }


if __name__ == "__main__":
    result = reconcile()
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
