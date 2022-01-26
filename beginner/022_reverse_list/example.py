"""
Write a function reverse_list that:
Input: (input_list: list[int])
Output: return a list that is a reverse of input_list
"""


def reverse_list_with_list_manipulation(input_list: list[int]) -> list[int]:
    return input_list[::-1]


def reverse_list_with_algorithm(input_list: list[int]) -> list[int]:
    reverse = []

    for i in range(len(input_list) - 1, -1, -1):
        reverse.append(input_list[i])
    return reverse


def reverse_list(input_list: list[int]) -> list[int]:
    # return reverse_list_with_list_manipulation(input_list)
    return reverse_list_with_algorithm(input_list)
