"""
Write a function fibonacci_below_n that:
Input: (n: int)
Output: return the fibonacci sequence until it greater or equal than n

For example:
n = 20
result = 1, 1, 2, 3, 5, 8, 13
"""


def fibonacci(n: int):
    if n < 0:
        return None
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_below_n(n: int):
    result = []
    f = 1
    i = 1
    while f <= n:
        result.append(f)
        i += 1
        f = fibonacci(i)
    return result
