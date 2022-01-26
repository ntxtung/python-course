"""
Write a function prime_factorization that:
Input: (n: int), n > 0
Output: return the list contain all the prime factorization of n

For example:
n = 18
result = [2, 3, 3]

This example reuse the implementation of 012_find_prime
"""


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_prime(n: int) -> list[int]:
    result = []
    for i in range(2, n + 1):
        if is_prime(i):
            result.append(i)
    return result


def prime_factorization(n: int) -> list[int]:
    primes = find_prime(n)
    result = []

    i = 0
    while n > 1:
        if n % primes[i] == 0:
            n //= primes[i]
            result.append(primes[i])
        else:
            i += 1

    return result
