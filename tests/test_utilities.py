import utilities
import unittest


class TestUtilities(unittest.TestCase):
    def test_check_date_format_year_too_long(self):
        date_input = "31/11/20235768"
        self.assertFalse(utilities.check_date_format(date_input))

    def test_check_date_format_year_too_short(self):
        date_input = "31/11/2"
        self.assertFalse(utilities.check_date_format(date_input))

    def test_check_date_format_valid_year_2_digits(self):
        date_input = "31/11/23"
        self.assertTrue(utilities.check_date_format(date_input))

    def test_check_date_format_valid_year_4_digits(self):
        date_input = "31/11/2023"
        self.assertTrue(utilities.check_date_format(date_input))

    def test_check_date_format_invalid_year_3_digits(self):
        date_input = "31/11/202"
        self.assertFalse(utilities.check_date_format(date_input))
