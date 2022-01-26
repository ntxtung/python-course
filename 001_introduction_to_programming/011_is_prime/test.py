from typing import Any
from main import is_prime


def test(input_data: Any, expect: Any, verbose=True):
    actual = is_prime(input_data)
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {}'.format(expect, actual, is_correct))
    return is_correct


"""
Test case 01:
"""


def test_case_01():
    input_data = 1
    expect = False
    test(input_data=input_data, expect=expect)


"""
Test case 02:
"""


def test_case_02():
    input_data = 2
    expect = True
    test(input_data=input_data, expect=expect)


"""
Test case 03:
"""


def test_case_03():
    input_data = 3
    expect = True
    test(input_data=input_data, expect=expect)


"""
Test case 04:
"""


def test_case_04():
    input_data = 4
    expect = False
    test(input_data=input_data, expect=expect)


"""
Test case 05:
"""


def test_case_05():
    input_data = 131
    expect = True
    test(input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
test_case_04()
test_case_05()
