import csv
import unittest
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / 'data' / '演练资料.csv'

class SourceFixtureTests(unittest.TestCase):
    def test_synthetic_records_follow_declared_table(self):
        with DATA.open(encoding='utf-8-sig', newline='') as handle:
            reader = csv.DictReader(handle)
            rows = list(reader)
        self.assertGreaterEqual(len(rows), 3)
        self.assertEqual(len(reader.fieldnames), len(set(reader.fieldnames)))
        self.assertTrue(all(any(value.strip() for value in row.values()) for row in rows))
        self.assertTrue(all(row.get(reader.fieldnames[0], '').strip() for row in rows))

if __name__ == '__main__':
    unittest.main()
