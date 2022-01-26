"""
Write a function least_common_denominator that:
Input: (x: int, y: int)
Output: return a number that is the least common denominator of x and y
"""


def least_common_denominator(x: int, y: int):
    i = max(x, y)
    while True:
        if i % x == 0 and i % y == 0:
            return i
        i += 1

