"""
A DNA string is a reverse palindrome if it is equal to its reverse complement.
For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12.
You may return these pairs in any order.
"""


def parse_fasta_to_dict(fasta_str: str):
    label_dict = {}
    current_label = ''

    for line in fasta_str.split('\n'):
        if len(line) == 0:
            continue
        if line[0] == '>':
            current_label = line[1:]
            label_dict[current_label] = ''
        else:
            label_dict[current_label] += line

    return label_dict


def get_dna_reverse_complement(dna_string: str) -> str:
    result = ''
    complement_dict = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    for character in dna_string:
        result += complement_dict[character]
    return result[::-1]


def is_palindrome_reverse_complement(dna_string: str) -> bool:
    return get_dna_reverse_complement(dna_string) == dna_string


def revp(fasta_str: str):
    data_dict = parse_fasta_to_dict(fasta_str)
    result = []

    for key in data_dict.keys():
        dna_string = data_dict[key]
        for i in range(len(dna_string)):
            for j in range(len(dna_string) + 1):
                # only take substring with 4 <= length <= 12
                if j - i < 4 or j - i > 12:
                    continue
                if is_palindrome_reverse_complement(dna_string[i:j]):
                    result.append((i + 1, j - i))
                    print(i + 1, j - i)

    return result


input_file = open('./test_input_02.txt', 'r')
input_data = input_file.read()
input_file.close()

print(revp(input_data))
