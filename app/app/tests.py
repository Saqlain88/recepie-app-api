"""
Sample Tests
"""


from django.test import SimpleTestCase
from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""

        res = calc.add(5, 6)
        """Test subtracting numbers."""

        res = calc.sub(5, 6)
        self.assertEqual(res, 1)
