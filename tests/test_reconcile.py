import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from reconcile import reconcile


class ReconcileTest(unittest.TestCase):
    def test_deduplication(self):
        result = reconcile()
        self.assertEqual(result["records_read"], 5)
        self.assertEqual(result["unique_events"], 4)
        self.assertEqual(result["duplicates_ignored"], 1)
        self.assertEqual(result["events_by_type"]["decision.published"], 2)


if __name__ == "__main__":
    unittest.main()
