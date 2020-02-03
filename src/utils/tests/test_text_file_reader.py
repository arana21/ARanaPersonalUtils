"""
Tests for text readers
"""

import io

from unittest import TestCase

from src.utils.file_io import CsvReader, TsvReader


class TestBaseFileReader(TestCase):
    def test_csv_file_reader(self):
        csv_test_file_reader = CsvReader().read_file(file_path=".test_csv.csv")

        line_1 = next(csv_test_file_reader)
        line_2 = next(csv_test_file_reader)

        self.assertTrue(isinstance(line_1, list))
        self.assertTrue(isinstance(line_2, list))

        self.assertEqual(line_1, ["this", "is", "a", "test", "csv", "file"])
        self.assertEqual(
            line_2, ["this", "is", "another", "test", "csv", "file"]
        )

    def test_tsv_file_reader(self):
        tsv_test_file_reader = TsvReader().read_file(file_path=".test_tsv.tsv")

        line_1 = next(tsv_test_file_reader)
        line_2 = next(tsv_test_file_reader)

        self.assertTrue(isinstance(line_1, list))
        self.assertTrue(isinstance(line_2, list))

        self.assertEqual(line_1, ["this", "is", "a", "test", "csv", "file"])
        self.assertEqual(
            line_2, ["this", "is", "another", "test", "csv", "file"]
        )
