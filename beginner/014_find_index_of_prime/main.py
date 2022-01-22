"""
Write a function find_index_of_prime that:
Input: (n: int) any integer number which is a prime number (not guarantee, you have to validate)
Output: return the index of that prime number in prime number sequence, if not a prime number, return None
"""


def is_prime(n: int):
    if n < 2:
        return False
    if n == 2:
        return True
    if n > 2:
        for m in range(2, int(n**0.5) + 1):
            if n % m == 0:
                return False
        return True


def find_index_of_prime(n: int):
    if is_prime(n) is True:
        count = 0
        i = 0
        while i <= n:
            if is_prime(i) is True:
                count += 1
            i += 1
        return count
    return None
