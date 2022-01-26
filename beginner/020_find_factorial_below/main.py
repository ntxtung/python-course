"""
Write a function find_factorial_below that:
Input: (n: int)
Output: return the list that contain factorial sequence that last number is less or equal than ns
"""


def factorial(n: int):
    p = 1
    for i in range(1, n + 1):
        p = p*i
    return p


def find_factorial_below(n: int):
    result = []
    i = 0
    while factorial(i) <= n:
        result.append(factorial(i))
        i += 1
    return result
