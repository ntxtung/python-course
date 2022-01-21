from typing import Any
from example import fibonacci
import time


def test(input_data: Any, expect: Any, verbose=True):
    start_time = time.time_ns()
    actual = fibonacci(input_data)
    cost = time.time_ns() - start_time
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {} \t take {} nanoseconds'.
              format(expect, actual, is_correct, cost))
    return is_correct


"""
Test case 01:
"""


def test_case_01():
    input_data = 1
    expect = 1
    test(input_data=input_data, expect=expect)


"""
Test case 02:
"""


def test_case_02():
    input_data = 2
    expect = 1
    test(input_data=input_data, expect=expect)


"""
Test case 03:
"""


def test_case_03():
    input_data = 10
    expect = 55
    test(input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
