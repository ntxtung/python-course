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
"""


def distance_of_two_point(a: tuple[int, int], b: tuple[int, int]):
    return ((b[0]-a[0])**2 + (b[1] - a[1])**2)**0.5


def is_triangle(a: tuple[int, int], b: tuple[int, int], c: tuple[int, int]) -> bool:
    ab = distance_of_two_point(a, b)
    ac = distance_of_two_point(a, c)
    bc = distance_of_two_point(b, c)
    if ab < ac + bc and ac < ab + bc and bc < ac + ab:
        return True
    return False