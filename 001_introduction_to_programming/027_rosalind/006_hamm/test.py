import unittest
from example import counting_point_mutations


class TestHAMM(unittest.TestCase):

    def test_case_01(self):
        expect = 7
        actual = counting_point_mutations('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT')

        self.assertAlmostEqual(expect, actual)

    def test_case_02(self):
        expect = 458
        str1 = 'TGCGCGAGCATTGGCTGTAACACCTTTCGTAGCTCAAAGGTCCTTTTGCAGATTATACAACCAATATACTAGGGGCGCGAACTCTAACCACACGAGGTTCCTGTCCAGCGGACCGCATCTTAGAACACGATACTTGAACTCTTTTTGCAGGAGACATCAAGGGGGGTAACGGCATTCGAGAGGTTGGAGCGGGAATCCCAGACCCCAGCTTCGCACCTTCCGGGATATGCCGTGCGGCCGGGCTGGCATAGTATGAGCCGGAACCGGTGTTAATACCTGAGCGCTTATGTTTAGCAGCTACCCATTATGGACGGAGTGAGGTAAACAACGCAGGTTCTTGTATGGACATGTAATATTTTAAGTAGCGCGTTGATAGGTGCACGCCGTGCGTGAGTGGTGACTCGTAGCCTCCTGTGTGTCGACTCCTTACCACCACCAAGATTTTCGTCTGGTCCACGAGCCCTGCGCGAGGTCGGAGTTATTGAAACCACAATTGTTTAGTCGTGTCCTAAATGACACCATCCCCCTCGTCACGGCTCATCCATAACAGTCAGAAAGGGCAAGCACAGAAAGTCATCTACTTCAAAGGACTCTTGAACGGCGATATCGGATAAAGGGCAGTTCATGCGGTAGCTGTCCAAAGCGCAATCGTCGCATCCCAAGGCCCAGCGTCAGGTAGTGCCTAGGCGAAGTGATTTGGTGTCGTTTCAATTTCCAGTAGTCCTTAGGACCGGCACAAACAAGGCAAACCGCCCCTTCGTTAGCCCGCACCTAATCGGTCGCTGTACGTCTAGGGGCCCGCTGCACGGGAACTTGCCGTACTAACCTGACATCCTGCTACGTCTACTCGTTAGATTAACATCTCCTACGCGTTCGTCCGCACGCAAATTCATTACCTCGAGTCTTCGATTATTAGCCTGGCGGGGATGAGGCAAGGCAAGGCGGG'
        str2 = 'TCCATTTCACTTGGCGGTAATACCTAGTGTAGTACAAATCTTGTACTGCCTTCTACACGAACTATTTAGCGGGTACTCCGCGTTCCCACAAAGGAATGTCCAATCTAACCGACCTTTTTACGCAGCAGGAGTCGAGTTCGCCACTGAAATGAACCGCGAACAGGCCTGAGGTCTTGTAATACGTTTGGGCGGTACACGCACGCCCCAGCCTCGTGATTTCCCGTAAAAGTTATTTGAGCGAGCAGGCGTAGTTTCGGTCGGATCGGTTGTTCAATGCCTCGGCTCATTCCTTCTCATTTGCCGATGGACGAAGGCGGGCGAACAACCACGCGCTAGGGTGTAAGAGGTTGTGTTGAGTTTCTCAACGAATGGGTTTGAGCACGACTTGCCCATTTGGGGACTAGTAGCAGTAGAGCTGCCGAATCGGTATCAGCACCAGGAGTTTAATCGGAGCTCGGAGCTTGGAGAGTGCCGTGAGTAAAACGATGTTCATTCGCTTAGTCGTGTCCGAAGCCCCGCTACCGGTATCTTCACGGCACGCACATTTGGATCCGACAGGCGAAGAAAACGGAGTGGTATGTATCAACGGATGCGTGAACTTGGATGCAGGTTAAAGCGGACTGCCCTTGGGGACTGTACAATGCAGTCCCTGATTATGACATGCTGTAACCGCAGGTTACGGCTAGGCGCAGTGACAGCCATTAGTTTCAGACTTCTGTAGTCCTGACAATTCGCTAATTCAAGTCTTACCGAACGTTACTTCACCTACACCTCATGCAGCTCTGTACTTGTCAGTGCTAATTTCAATCGGAAGAAGCGAAAAGACCTCTCAGCTTGCCAGGCCTAATCCTTGTTTTGAAGTAGCTTACCAAGTCACGCGCCCGCCCATTATTTTCCCGATTCCTTCAAAGGTTAGCTCGAGCTAGTCGAGTGCACACTAGTGAGA'
        actual = counting_point_mutations(str1, str2)

        self.assertAlmostEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()