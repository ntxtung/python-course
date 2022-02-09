import unittest
from example import computing_gc_content


class TestREVC(unittest.TestCase):

    def test_case_01(self):
        test_input_file = open('test_input.txt', 'r')
        test_input = test_input_file.read()
        test_input_file.close()

        expect = 0.60919540
        actual = computing_gc_content(test_input)

        self.assertAlmostEqual(expect, actual[1])

    def test_case_02(self):
        test_input_file = open('test_input_02.txt', 'r')
        test_input = test_input_file.read()
        test_input_file.close()

        expect = 0.60919540
        actual = computing_gc_content(test_input)
        print(actual)

        self.assertAlmostEqual(expect, actual[1])

if __name__ == '__main__':
    unittest.main()
