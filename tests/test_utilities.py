"""unittest module for testing the utilities functions"""
import unittest
import utilities


class TestUtilities(unittest.TestCase):
    """unittest class to handle utilities test cases"""

    def test_check_date_format_year_too_long(self):
        """test case to check year too long"""
        date_input = "31/11/20235768"
        self.assertFalse(utilities.check_date_format(date_input))

    def test_check_date_format_year_too_short(self):
        """test case to check year too short"""
        date_input = "31/11/2"
        self.assertFalse(utilities.check_date_format(date_input))

    def test_check_date_format_valid_year_2_digits(self):
        """test case to check valid two-digit year"""
        date_input = "31/11/23"
        self.assertTrue(utilities.check_date_format(date_input))

    def test_check_date_format_valid_year_4_digits(self):
        """test case to check valid 4 digit year"""
        date_input = "31/11/2023"
        self.assertTrue(utilities.check_date_format(date_input))

    def test_check_date_format_invalid_year_3_digits(self):
        """test case to check valid 3 digit year"""
        date_input = "31/11/202"
        self.assertFalse(utilities.check_date_format(date_input))
