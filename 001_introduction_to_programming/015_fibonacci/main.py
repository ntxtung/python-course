"""
Write a function fibonacci that:
Input: (n: int)
Output: return the number at index n in fibonacci sequence
"""


def fibonacci(n: int):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return n
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(24))