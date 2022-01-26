from typing import Any, Callable
from example import linear_equation_solver


def test(test_function: Callable, input_data: Any, expect: Any, verbose=True):
    actual = test_function(*input_data)
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {}'.format(expect, actual, is_correct))
    return is_correct


"""
Test case 01: happy case
"""


def test_case_01():
    input_data = (1, 1)
    expect = 1
    test(linear_equation_solver, input_data=input_data, expect=expect)


"""
Test case 02: no solution
"""


def test_case_02():
    input_data = (0, 1)
    expect = None
    test(linear_equation_solver, input_data=input_data, expect=expect)


"""
Test case 03: Infinity solution
"""


def test_case_03():
    input_data = (0, 0)
    expect = None
    test(linear_equation_solver, input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
