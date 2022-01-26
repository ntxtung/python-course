"""
Write a function find_first_n_fibonacci that:
Input: (n: int)
Output: return the first n fibonacci sequence (index 0 exclusive)
"""


def fibonacci(n: int):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def find_first_n_fibonacci(n: int):
    result = []
    for i in range(1, n + 1):
        result.append(fibonacci(i))
    return result
