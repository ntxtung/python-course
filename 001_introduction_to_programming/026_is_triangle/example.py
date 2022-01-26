"""
Write a function is_triangle that:
Input: (a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) are 3 points of the triangle in 2D dimension
Output: return whether if a, b, c can really make a triangle

Hint: According to Triangle Inequality Theorem
The triangle inequality states that for any triangle,
the sum of the lengths of any two sides must be greater than or equal to the length of the remaining side

if x, y, and z are the lengths of the sides of the triangle:
z < x + y
x < z + y
y < x + z

Another hint:
The formula of distance between two points is P(x1, y1) and Q(x2, y2) is given by:
d(P, Q) = √((x2 – x1) + (y2 – y1) ** 2)
"""


def distance(a: tuple[int, int], b: tuple[int, int]) -> float:
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def is_triangle(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    dab = distance(a, b)
    dac = distance(a, c)
    dbc = distance(b, c)
    if dab < dac + dbc and dbc < dab + dac and dac < dab + dbc:
        return True
    return False
