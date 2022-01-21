"""
Write a function find_prime that:
Input: (n: int) any integer number
Output: return every prime number less or equal than n
"""


def is_prime(n: int):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_prime(n: int):
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
    return result
