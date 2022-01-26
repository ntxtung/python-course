import unittest
from main import is_triangle


class TestIsTriangle(unittest.TestCase):

    def test_case_01(self):
        a = (0, 0)
        b = (2, 0)
        c = (0, 3)

        expect = True
        actual = is_triangle(a, b, c)

        self.assertEqual(expect, actual)

    def test_case_02(self):
        a = (0, 0)
        b = (2, 0)
        c = (3, 0)

        expect = False
        actual = is_triangle(a, b, c)

        self.assertEqual(expect, actual)

    def test_case_03(self):
        a = (-1, -2)
        b = (1, 2)
        c = (4, -5)

        expect = True
        actual = is_triangle(a, b, c)

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
