from typing import Any
from main import find_first_n_prime
import time


def test(input_data: Any, expect: Any, verbose=True):
    start_time = time.time_ns()
    actual = find_first_n_prime(input_data)
    cost = time.time_ns() - start_time
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {} \t len={} \t take {} nanoseconds'.
              format(expect, actual, is_correct, len(actual), cost))
    return is_correct


"""
Test case 01:
"""


def test_case_01():
    input_data = 0
    expect = []
    test(input_data=input_data, expect=expect)


"""
Test case 02:
"""


def test_case_02():
    input_data = 5
    expect = [2, 3, 5, 7, 11]
    test(input_data=input_data, expect=expect)


"""
Test case 03:
"""


def test_case_03():
    input_data = 10
    expect = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    test(input_data=input_data, expect=expect)


"""
Test case 04:
"""


def test_case_04():
    input_data = 20
    expect = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]
    test(input_data=input_data, expect=expect)


"""
Test case 05:
"""


def test_case_05():
    input_data = 100000
    expect = None
    test(input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
test_case_04()
test_case_05()
