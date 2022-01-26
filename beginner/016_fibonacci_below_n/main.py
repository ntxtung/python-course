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
    if n == 0 or n == 1:
        return n
    if n > 1:
        return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_below_n(n: int):
    fibonacci_list = []
    i = 1
    while fibonacci(i) <= n:
        fibonacci_list.append(fibonacci(i))
        i += 1
    return fibonacci_list



