import unittest
from main import is_palindrome


class TestIsPalindrome(unittest.TestCase):

    def test_case_01(self):
        input_data = 12345

        expect = False
        actual = is_palindrome(input_data)

        self.assertEqual(expect, actual)

    def test_case_02(self):
        input_data = 12321

        expect = True
        actual = is_palindrome(input_data)

        self.assertEqual(expect, actual)

    def test_case_03(self):
        input_data = 1

        expect = True
        actual = is_palindrome(input_data)

        self.assertEqual(expect, actual)

    def test_case_04(self):
        input_data = 1234567654321

        expect = True
        actual = is_palindrome(input_data)

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
