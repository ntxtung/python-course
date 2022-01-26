"""
Write a function find_first_n_prime that:
Input: (n: int) any integer number
Output: return first n prime
"""


def is_prime(i: int):
    if i < 2:
        return False
    if i == 2:
        return True
    if i > 2:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                return False
        return True


def find_first_n_prime(n: int):
    if n < 1:
        return []
    if n >= 1:
        result = []
        i = 2
        while len(result) < n:
            if is_prime(i) is True:
                result.append(i)
            i += 1
        return result
