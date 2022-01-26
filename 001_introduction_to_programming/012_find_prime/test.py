from typing import Any
from main import find_prime
import time


def test(input_data: Any, expect: Any, verbose=True):
    start_time = time.time()
    actual = find_prime(input_data)
    cost = time.time() - start_time
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {} \t len={} \t take {} second'.
              format(expect, actual, is_correct, len(actual), cost))
    return is_correct


"""
Test case 01:
"""


def test_case_01():
    input_data = 1
    expect = []
    test(input_data=input_data, expect=expect)


"""
Test case 02:
"""


def test_case_02():
    input_data = 2
    expect = [2]
    test(input_data=input_data, expect=expect)


"""
Test case 03:
"""


def test_case_03():
    input_data = 3
    expect = [2, 3]
    test(input_data=input_data, expect=expect)


"""
Test case 04:
"""


def test_case_04():
    input_data = 131
    expect = [2, 3]
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
