"""
Write a function first_n_factorial that:
Input: (n: int)
Output: return the list that
[fact(1), fact(2), ..., fact(n)]
"""


def factorial(n: int):
    p = 1
    for i in range(1, n + 1):
        p = p*i
    return p


def first_n_factorial(n: int):
    result = []
    for i in range(1, n + 1):
        result.append(factorial(i))
    return result
