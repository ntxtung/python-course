"""
Write a function find_first_n_prime that:
Input: (n: int) any integer number
Output: return first n prime
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


def find_first_n_prime(n: int):
    i = 0
    result = []
    while len(result) < n:
        if is_prime(i):
            result.append(i)
        i += 1
    return result
