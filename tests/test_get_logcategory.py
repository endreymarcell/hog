import unittest

from .data import mock_logcategories
from utils import get_logcategory


class GetLogcategoryTestCase(unittest.TestCase):
    def test_exact_match(self) -> None:
        result = get_logcategory("cheeseshop", mock_logcategories)
        self.assertEqual(result, "cheeseshop")

    def test_intelligent_match(self) -> None:
        result = get_logcategory("cheeseshop-d-b", mock_logcategories)
        self.assertEqual(result, "cheeseshop_danish_blue")
