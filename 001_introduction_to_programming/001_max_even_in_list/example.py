"""
Write a function max_even_in_list that:
Input: a list of number (int)
Output: a number which is the maximum even number in list, return None if not found any

Lazy Idea: Find all even numbers in list, then return the max number in that list
"""


def max_even_in_list(input_list: list[int]):
    if len(input_list) > 0:
        evens = []
        for i in input_list:
            if i % 2 == 0:
                evens.append(i)

        if len(evens) > 0:
            return max(evens)
    return None
