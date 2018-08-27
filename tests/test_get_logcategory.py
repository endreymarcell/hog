import unittest

from utils.get_logcategory import get_logcategory
from .data import mock_logcategories


class GetLogcategoryTestCase(unittest.TestCase):
    def test_exact_match(self) -> None:
        result = get_logcategory("cheeseshop", mock_logcategories)
        self.assertEqual(result, "cheeseshop")

    def test_intelligent_match(self) -> None:
        result = get_logcategory("cheeseshop-d-b", mock_logcategories)
        self.assertEqual(result, "cheeseshop_danish_blue")
