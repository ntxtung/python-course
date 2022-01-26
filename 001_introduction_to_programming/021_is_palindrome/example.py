"""
Write a function is_palindrome that:
Input: (n: int), n > 0
Output: return whether n is palindrome or not
"""


def is_palindrome_reverse_string_method(n: int):
    reverse = int(str(n)[::-1])
    return reverse == n


def is_palindrome_calculation_method(n: int):
    reverse = 0
    clone_n = n
    while clone_n > 0:
        reverse = (reverse * 10) + (clone_n % 10)
        clone_n //= 10
    return reverse == n


def is_palindrome(n: int) -> bool:
    # return is_palindrome_reverse_string_method(n)
    return is_palindrome_calculation_method(n)


print(is_palindrome(121))
