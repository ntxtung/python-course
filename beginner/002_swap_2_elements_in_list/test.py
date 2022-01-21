from typing import Any, Callable
from main import swap_2_elements_in_list


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
    input_data = ([1, 2, 3, 4, 5], 1, 3)
    expect = [1, 4, 3, 2, 5]
    test(swap_2_elements_in_list, input_data=input_data, expect=expect)


"""
Test case 02: same indexes
"""


def test_case_02():
    input_data = ([1, 2, 3, 4, 5], 1, 1)
    expect = [1, 2, 3, 4, 5]
    test(swap_2_elements_in_list, input_data=input_data, expect=expect)


"""
Test case 03: invalid indexes
"""


def test_case_03():
    input_data = ([1, 2, 3, 4, 5], -2, 1)
    expect = [1, 2, 3, 4, 5]
    test(swap_2_elements_in_list, input_data=input_data, expect=expect)


"""
Test case 04: invalid indexes
"""


def test_case_04():
    input_data = ([1, 2, 3, 4, 5], 1, 10)
    expect = [1, 2, 3, 4, 5]
    test(swap_2_elements_in_list, input_data=input_data, expect=expect)


"""
Test case 05: Empty list
"""


def test_case_05():
    input_data = ([], 1, 10)
    expect = []
    test(swap_2_elements_in_list, input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
test_case_04()
test_case_05()
