from typing import Any
from main import least_common_denominator


def test(input_data: Any, expect: Any, verbose=True):
    actual = least_common_denominator(*input_data)
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {}'.format(expect, actual, is_correct))
    return is_correct


"""
Test case 01:
"""


def test_case_01():
    input_data = (12, 5)
    expect = 60
    test(input_data=input_data, expect=expect)


"""
Test case 02:
"""


def test_case_02():
    input_data = (12, 4)
    expect = 12
    test(input_data=input_data, expect=expect)


"""
Test case 03:
"""


def test_case_03():
    input_data = (12, 20)
    expect = 60
    test(input_data=input_data, expect=expect)


"""
Test case 04:
"""


def test_case_04():
    input_data = (13, 17)
    expect = 221
    test(input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
test_case_04()
