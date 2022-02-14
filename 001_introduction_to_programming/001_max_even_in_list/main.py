"""
Write a function max_even_in_list that:
Input: a list of number (int)
Output: a number which is the maximum even number in list, return None if not found any
"""


def max_even_in_list(input_list: list[int]):
    even_l = []
    for i in input_list:
        if i % 2 == 0:
            even_l.append(i)
    if len(even_l) == 0:
        return None
    max_even = even_l[0]
    for i in even_l:
        if max_even < i:
            max_even = i
    return max_even

