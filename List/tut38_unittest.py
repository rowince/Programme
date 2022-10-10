import unittest
from tut38 import palindrome


class TestPalindrome(unittest.TestCase):
    def setUp(self):
        self.input1 = 'abut-1-tuba'
        self.input2 = '@allula'

    def test_palindrome_positive_response(self):
        """ Test for positive """
        output = palindrome(self.input1)
        self.assertEqual(output, 'YES')

    def test_palindrome_negative_response(self):
        """ Test for negative """
        output = palindrome(self.input2)
        self.assertEqual(output, 'NO')


unittest.main()
