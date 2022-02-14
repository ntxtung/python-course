"""
Write a function prime_factorization that:
Input: (n: int), n > 0
Output: return the list contain all the prime factorization of n

For example:
n = 18
result = [2, 3, 3]
"""


def is_prime(n: int):
    if n < 2:
        return False
    if n == 2:
        return True
    if n > 2:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
    return True


def first_n_prime(n: int):
    if n >= 2:
        result = []
        for i in range(2, n + 1):
            if is_prime(i) is True:
                result.append(i)
        return result
    return []


def prime_factorization(n: int) -> list[int]:
    if n < 1:
        return []
    prime_list = first_n_prime(n)
    result = []
    while n > 1:
        i = 0
        while n % prime_list[i] == 0:
            result.append(i)
            n = n / prime_list[i]
        i += 1
    return result
