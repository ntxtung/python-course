"""
Write a function is_prime that:
Input: (n: int) any integer number
Output: return True if n is a prime number, otherwise.
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
