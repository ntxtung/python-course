"""
Write a function factorial that:
Input: (n: int)
Output: return the factorial of n
"""


def factorial(n: int):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f
