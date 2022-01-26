"""
Write a function least_common_denominator that:
Input: (input_list: list[int]) which every number in that list is bigger than 0 (guaranteed)
Output: return a number that is the least common denominator of input_list
"""


def least_common_denominator(input_list: list[int]):
    i = max(input_list)
    while True:
        is_lcm = True
        for j in input_list:
            if i % j != 0 or i % j != 0:
                is_lcm = False
        if is_lcm is True:
            return i
        i += 1