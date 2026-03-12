import sys
import os

# Add current directory to Python path (Fix for PyCharm import issue)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import unittest
from validator import validate_email, validate_phone
from validator import InvalidEmailException, InvalidPhoneException


class TestValidation(unittest.TestCase):

    def test_valid_email(self):
        self.assertTrue(validate_email("test@gmail.com"))

    def test_invalid_email(self):
        with self.assertRaises(InvalidEmailException):
            validate_email("invalidemail.com")

    def test_valid_phone(self):
        self.assertTrue(validate_phone("9876543210"))

    def test_invalid_phone(self):
        with self.assertRaises(InvalidPhoneException):
            validate_phone("12345")


if __name__ == "__main__":
    unittest.main()
