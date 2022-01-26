from typing import Any
from main import first_n_factorial
import time


def test(input_data: Any, expect: Any, verbose=True):
    start_time = time.time_ns()
    actual = first_n_factorial(input_data)
    cost = time.time_ns() - start_time
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {} \t take {} nanoseconds'.
              format(expect, actual, is_correct, cost))
    return is_correct


"""
First 20
1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181
"""

"""
Test case 01:
"""


def test_case_01():
    input_data = 3
    expect = [1, 2, 6]
    test(input_data=input_data, expect=expect)


"""
Test case 02:
"""


def test_case_02():
    input_data = 5
    expect = [1, 2, 6, 24, 120]
    test(input_data=input_data, expect=expect)


"""
Test case 03:
"""


def test_case_03():
    input_data = 10
    expect = [1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800]
    test(input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
