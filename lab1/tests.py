import unittest
from functions import Add

class StringCalculator(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(Add(""), 0)

    def test_single_number(self):
        self.assertEqual(Add("1"), 1)

    def test_two_numbers(self):
        self.assertEqual(Add("1,5"), 6)

    def test_multiple_numbers(self):
        self.assertEqual(Add("0,1,3,8,15"), 27)

    def test_newline(self):
        self.assertEqual(Add("1\n2,3"), 6)

    def test_bad_start_and_end(self):
        self.assertEqual(Add(",1\n2,3"), -1)
        self.assertEqual(Add("1\n2,3,"), -1)

    def test_invalid_newline(self):
        self.assertEqual(Add(",1\n2,3"), -1)
        self.assertEqual(Add("1\n2,3,"), -1)

