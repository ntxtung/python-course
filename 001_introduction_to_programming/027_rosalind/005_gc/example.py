"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are 'C' or 'G'.
For example, the GC-content of "AGCTATAG" is 37.5%.
Note that the reverse complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database.
A commonly used method of string labeling is called FASTA format.
In this format, the string is introduced by a line that begins with '>', followed by some labeling information.
Subsequent lines contain the string itself; the first line to begin with '>' indicates the label of the next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID "Rosalind_xxxx",
where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content of that string.
Rosalind allows for a default error of 0.001 in all decimal answers unless otherwise stated;
"""
import re


def calculate_gc_content(dna_string: str) -> float:
    matches = re.findall('[GC]', dna_string)
    return len(matches)/len(dna_string)


def computing_gc_content(fasta_str: str):
    label_dict = {}
    current_label = ''

    for line in fasta_str.split('\n'):
        if line[0] == '>':
            current_label = line[1:]
            label_dict[current_label] = ''
        else:
            label_dict[current_label] += line

    highest_label = None
    highest_gc_content = 0

    for label in label_dict.keys():
        gc_content = calculate_gc_content(label_dict[label])
        if gc_content > highest_gc_content:
            highest_gc_content = gc_content
            highest_label = label
    return highest_label, highest_gc_content
