import unittest
from example import finding_a_motif_in_dna


class TestSUBS(unittest.TestCase):

    def test_case_01(self):
        s = 'GATATATGCATATACTT'
        sub_s = 'ATAT'
        expect = (2, 4, 10)
        actual = finding_a_motif_in_dna(s, sub_s)

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
