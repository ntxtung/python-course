"""
Write a function is_palindrome that:
Input: (n: int)
Output: return whether n is palindrome or not
"""


def is_palindrome(n: int) -> bool:
    a = str(n)
    for i in range(0, len(a)//2):
        if a[i] != a[len(a) - i - 1]:
            return False
    return True
