"""
Write a function fibonacci that:
Input: (n: int) n is greater than 0 (guaranteed)
Output: return the number at index n in fibonacci sequence
"""


def fibonacci(n: int):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
