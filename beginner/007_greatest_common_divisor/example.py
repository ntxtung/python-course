"""
Write a function greatest_common_divisor that:
Input: (x: int, y: int) which x > 0 and y > 0 (guaranteed)
Output: return a number that is the greatest common divisor of x and y

Definition (wiki): In mathematics, the greatest common divisor (GCD) of two or more integers,
which are not all zero, is the largest positive integer that divides each of the integers.
For two integers x, y, the greatest common divisor of x and y is denoted gcd(x,y).
For example, the GCD of 8 and 12 is 4, that is, gcd(8,12)=4
"""


def greatest_common_divisor(x: int, y: int):
    for i in range(min(x, y), 0, -1):
        if x % i == 0 and y % i == 0:
            return i
