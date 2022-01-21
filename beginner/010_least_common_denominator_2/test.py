from typing import Any
from main import least_common_denominator


def test(input_data: Any, expect: Any, verbose=True):
    actual = least_common_denominator(input_data)
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {}'.format(expect, actual, is_correct))
    return is_correct


"""
Test case 01:
"""


def test_case_01():
    input_data = [12, 9, 6]
    expect = 36
    test(input_data=input_data, expect=expect)


"""
Test case 02:
"""


def test_case_02():
    input_data = [8, 8, 6]
    expect = 24
    test(input_data=input_data, expect=expect)


"""
Test case 03:
"""


def test_case_03():
    input_data = [7, 11, 17]
    expect = 1309
    test(input_data=input_data, expect=expect)


"""
Test case 04:
"""


def test_case_04():
    input_data = [4, 8, 1]
    expect = 8
    test(input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
test_case_04()
