import unittest
from tut39 import password
import string

class TestPassword(unittest.TestCase):
    def setUp(self):
        self.Character_length = 10
        self.upper_case_length = 2
        self.digits_length = 3
        self.special_length = 1
        self.upper_letter = string.ascii_uppercase
        self.digit = string.digits
        self.special = string.punctuation

    def test_password_positive_response(self):
        pass_test = password(self.Character_length, self.upper_case_length,
                             self.digits_length, self.special_length)
        upper_case = ''.join(i for i in pass_test if i in self.upper_letter)
        digit_case = ''.join(i for i in pass_test if i in self.digit)
        special_case = ''.join(i for i in pass_test if i in self.special)
        self.assertEqual(len(pass_test), self.Character_length)
        self.assertGreaterEqual(len(upper_case), self.upper_case_length)
        self.assertGreaterEqual(len(digit_case), self.digits_length)
        self.assertGreaterEqual(len(special_case), self.special_length)

unittest.main()
