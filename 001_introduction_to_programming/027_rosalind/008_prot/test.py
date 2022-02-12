import unittest
from example import translating_rna_into_protein


class TestPROT(unittest.TestCase):

    def test_case_01(self):
        input_data = 'AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'
        expect = 'MAMAPRTEINSTRING'
        actual = translating_rna_into_protein(input_data)

        self.assertEqual(expect, actual)


if __name__ == '__main__':
    unittest.main()
