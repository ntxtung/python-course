from typing import Any
from main import find_index_of_prime
import time


def test(input_data: Any, expect: Any, verbose=True):
    start_time = time.time_ns()
    actual = find_index_of_prime(input_data)
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
    input_data = 2
    expect = 1
    test(input_data=input_data, expect=expect)


"""
Test case 02:
"""


def test_case_02():
    input_data = 5
    expect = 3
    test(input_data=input_data, expect=expect)


"""
Test case 03:
"""


def test_case_03():
    input_data = 10
    expect = None
    test(input_data=input_data, expect=expect)


"""
Test case 04:
"""


def test_case_04():
    input_data = 29
    expect = 10
    test(input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
test_case_04()
