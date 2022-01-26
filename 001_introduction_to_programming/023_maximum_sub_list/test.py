import unittest
from main import maximum_sub_list


class TestMaximumSubList(unittest.TestCase):

    def test_case_01(self):
        input_data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

        expect = 6
        actual = maximum_sub_list(input_data)

        self.assertEqual(expect, actual)

    def test_case_02(self):
        input_data = [1]

        expect = 1
        actual = maximum_sub_list(input_data)

        self.assertEqual(expect, actual)

    def test_case_03(self):
        input_data = [5, 4, -1, 7, 8]

        expect = 23
        actual = maximum_sub_list(input_data)

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
