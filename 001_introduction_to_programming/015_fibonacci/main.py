"""
Write a function fibonacci that:
Input: (n: int)
Output: return the number at index n in fibonacci sequence
"""


def fibonacci(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n > 2:
        return fibonacci(n-1) + fibonacci(n-2)
