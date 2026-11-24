import csv
import unittest
from pathlib import Path

DATA = Path(__file__).resolve().parents[1] / 'data'

class SourceFixtureTests(unittest.TestCase):
    def test_linked_source_tables_are_readable(self):
        files = sorted(DATA.glob('*.csv'))
        self.assertGreaterEqual(len(files), 3)
        for path in files:
            with path.open(encoding='utf-8-sig', newline='') as handle:
                reader = csv.DictReader(handle)
                rows = list(reader)
            self.assertGreaterEqual(len(rows), 3, path.name)
            self.assertTrue(reader.fieldnames, path.name)
            self.assertEqual(len(reader.fieldnames), len(set(reader.fieldnames)), path.name)
            self.assertTrue(all(any(value.strip() for value in row.values()) for row in rows), path.name)

if __name__ == '__main__':
    unittest.main()
