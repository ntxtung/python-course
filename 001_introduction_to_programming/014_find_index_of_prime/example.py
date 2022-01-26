"""
Write a function find_index_of_prime that:
Input: (n: int) any integer number which is a prime number (not guarantee, you have to validate)
Output: return the index of that prime number in prime number sequence, if a prime number, return None
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


def find_index_of_prime(n: int):
    if is_prime(n) is not True:
        return None

    primes = find_prime(n)

    return len(primes)
