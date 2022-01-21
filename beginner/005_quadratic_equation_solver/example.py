"""
Write a function quadratic_equation_solver that solve ax^2 + bx + c = 0:
Input: (a: float, b: float, c: float)
Output: solution x1, x2 (in tuple), return None if no solution or infinity solution

Scope: We don't work with complex number. Not yet! 🥲
"""
import math


def quadratic_equation_solver(a: float, b: float, c: float) -> tuple[float, float] | None:
    if a > 0:
        d = (b ** 2) - (4 * a * c)
        if d >= 0:
            s1 = (-b - math.sqrt(d)) / (2 * a)
            s2 = (-b + math.sqrt(d)) / (2 * a)
            return s1, s2
    return None
