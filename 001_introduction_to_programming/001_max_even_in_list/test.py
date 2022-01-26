from typing import Any
from main import max_even_in_list


def test(test_function, input_data: Any, expect: Any, verbose=True):
    actual = test_function(input_data)
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {}'.format(expect, actual, is_correct))
    return is_correct

"""
Test case 01: happy case
"""


def test_case_01():
    input_data = [1, 2, 3, 4, 5]
    expect = 4
    test(max_even_in_list, input_data=input_data, expect=expect)


"""
Test case 02: 2 equivalent maximum value
"""


def test_case_02():
    input_data = [1, 4, 3, 4, 5]
    expect = 4
    test(max_even_in_list, input_data=input_data, expect=expect)


"""
Test case 03: no even
"""


def test_case_03():
    input_data = [1, 3, 5, 7]
    expect = None
    test(max_even_in_list, input_data=input_data, expect=expect)


"""
Test case 04: empty list
"""


def test_case_04():
    input_data = []
    expect = None
    test(max_even_in_list, input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
test_case_04()
