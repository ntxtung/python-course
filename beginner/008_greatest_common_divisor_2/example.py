"""
Write a function greatest_common_divisor that:
Input: (input_list: list[int]) which every number in that list is bigger than 0 (guaranteed)
Output: return a number that is the greatest common divisor of every member of input_list
"""


def greatest_common_divisor(input_list: list[int]):
    for i in range(min(input_list), 0, -1):
        is_divisor = True
        for j in input_list:
            if j % i != 0:
                is_divisor = False
        if is_divisor is True:
            return i
