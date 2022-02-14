"""
Write a function reverse_list that:
Input: (input_list: list[int])
Output: return a list that is a reverse of input_list
"""


def reverse_list(input_list: list[int]) -> list[int]:
    reverse_list = []
    for i in range(len(input_list) - 1, -1, -1):
        reverse_list.append(input_list[i])
    return reverse_list
