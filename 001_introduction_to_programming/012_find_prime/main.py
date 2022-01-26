"""
Write a function find_prime that:
Input: (n: int) any integer number
Output: return every prime number below n
"""


def is_prime(n: int):
    if n < 2:
        return False
    for m in range(2, n):
        if n % m == 0:
            return False
    return True


def find_prime(n: int):
    if n >= 2:
        prime_list = []
        for i in range(2, n+1):
            if is_prime(i) is True:
                prime_list.append(i)
        return prime_list
    return []


