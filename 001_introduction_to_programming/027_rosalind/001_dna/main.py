"""
A string is simply an ordered collection of symbols selected from some alphabet and formed into a word;
the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is
"ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times
that the symbols 'A', 'C', 'G', and 'T' occur in s.
"""


def counting_dna_nucleotides(dna_string: str) -> str:
    count_a = 0
    count_c = 0
    count_g = 0
    count_t = 0
    for i in dna_string:
        if i == 'A':
            count_a += 1
        if i == 'C':
            count_c += 1
        if i == 'G':
            count_g += 1
        if i == 'T':
            count_t += 1
    return '{} {} {} {}'.format(count_a, count_c, count_g, count_t)
