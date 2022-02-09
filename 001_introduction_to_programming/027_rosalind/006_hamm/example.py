"""
Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
is the number of corresponding symbols that differ in s and t. See Figure 2.

Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).

Return: The Hamming distance dH(s,t).
"""


def counting_point_mutations(dna_1: str, dna_2: str):
    count = 0
    for i in range(len(dna_1)):
        if dna_1[i] != dna_2[i]:
            count += 1
    return count
