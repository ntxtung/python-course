import unittest
from main import reverse_list


class TestReverseList(unittest.TestCase):

    def test_case_01(self):
        input_data = [1, 2, 3, 4, 5]

        expect = [5, 4, 3, 2, 1]
        actual = reverse_list(input_data)

        self.assertEqual(expect, actual)

    def test_case_02(self):
        input_data = [1]

        expect = [1]
        actual = reverse_list(input_data)

        self.assertEqual(expect, actual)

    def test_case_03(self):
        input_data = []

        expect = []
        actual = reverse_list(input_data)

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
