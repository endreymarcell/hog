import unittest

from utils.get_filenames import select_filenames_for_interval


class SelectFilenamesForIntervalTestCase(unittest.TestCase):
    def test_default_get_last_single(self) -> None:
        filenames = select_filenames_for_interval(["a", "b", "c"], "-1")
        self.assertEqual(filenames, ["c"])

    def test_get_single(self) -> None:
        filenames = select_filenames_for_interval(["a", "b", "c"], "-2")
        self.assertEqual(filenames, ["b"])

    def test_get_single_out_of_range(self) -> None:
        with self.assertRaises(Exception):
            select_filenames_for_interval(["a", "b", "c"], "-4")

    def test_get_interval_fully_specified(self) -> None:
        filenames = select_filenames_for_interval(["a", "b", "c", "d", "e"], "-3:-2")
        self.assertEqual(filenames, ["c", "d"])

    def test_interval_edge_case(self) -> None:
        filenames = select_filenames_for_interval(["a", "b", "c", "d", "e"], "-3:-1")
        self.assertEqual(filenames, ["c", "d", "e"])

    def test_get_interval_open_left(self) -> None:
        filenames = select_filenames_for_interval(["a", "b", "c", "d", "e"], ":-2")
        self.assertEqual(filenames, ["a", "b", "c", "d"])

    def test_get_interval_open_right(self) -> None:
        filenames = select_filenames_for_interval(["a", "b", "c", "d", "e"], "-3:")
        self.assertEqual(filenames, ["c", "d", "e"])
