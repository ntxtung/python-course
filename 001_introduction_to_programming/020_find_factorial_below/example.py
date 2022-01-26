"""
Write a function find_factorial_below that:
Input: (n: int)
Output: return the list that contain factorial sequence that last number is less or equal than ns
"""


def find_factorial_below(n: int):
    f = 1
    result = []
    i = 1
    while f <= n:
        result.append(f)
        f *= i
        i += 1
    return result
