"""
Write a function linear_equation_solver that solve ax + b = 0:
Input: (a: float, b: float)
Output: root x, return None if no solution or infinity roots

Scope: We don't work with complex number. Not yet! 🥲
"""


def linear_equation_solver(a: float, b: float) -> float | None:
    if a != 0:
        return b/a
    return None
