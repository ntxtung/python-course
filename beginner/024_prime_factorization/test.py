import unittest
from main import prime_factorization


class TestMaximumSubList(unittest.TestCase):

    def test_case_01(self):
        input_data = 18

        expect = [2, 3, 3]
        actual = prime_factorization(input_data)

        self.assertEqual(expect, actual)

    def test_case_02(self):
        input_data = 17

        expect = [17]
        actual = prime_factorization(input_data)

        self.assertEqual(expect, actual)

    def test_case_03(self):
        input_data = 100

        expect = [2, 2, 5, 5]
        actual = prime_factorization(input_data)

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
