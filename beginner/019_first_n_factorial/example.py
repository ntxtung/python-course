"""
Write a function first_n_factorial that:
Input: (n: int)
Output: return the list that
[fact(1), fact(2), ..., fact(n)]
"""


def first_n_factorial(n: int):
    f = 1
    result = []
    for i in range(1, n + 1):
        f *= i
        result.append(f)
    return result
