"""
In DNA strings, symbols 'A' and 'T' are complements of each other, as are 'C' and 'G'.

The reverse complement of a DNA string s is the string sc formed by reversing the symbols of s,
then taking the complement of each symbol (e.g., the reverse complement of "GTCA" is "TGAC").

Given: A DNA string s of length at most 1000 bp.

Return: The reverse complement sc of s.
"""


def complementing_strand_of_dna(dna_string: str) -> str:
    result = ''
    for character in dna_string:
        #
        if character == 'A':
            result += 'T'
        elif character == 'T':
            result += 'A'
        #
        elif character == 'G':
            result += 'C'
        elif character == 'C':
            result += 'G'
    return result[::-1]
