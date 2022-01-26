from typing import Any, Callable
from main import remove_duplicates


def test(test_function: Callable, input_data: Any, expect: Any, verbose=True):
    actual = test_function(input_data)
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {}'.format(expect, actual, is_correct))
    return is_correct


"""
Test case 01: happy case
"""


def test_case_01():
    input_data = [1, 1, 2, 2, 4, 4, 5]
    expect = [1, 2, 4, 5]
    test(remove_duplicates, input_data=sorted(input_data), expect=sorted(expect))


"""
Test case 02: no duplicates
"""


def test_case_02():
    input_data = [1, 2, 4, 5]
    expect = [1, 2, 4, 5]
    test(remove_duplicates, input_data=sorted(input_data), expect=sorted(expect))


"""
Test case 03: all duplicates
"""


def test_case_03():
    input_data = [1, 1, 1, 1, 1]
    expect = [1]
    test(remove_duplicates, input_data=sorted(input_data), expect=sorted(expect))


"""
Test case 04: empty list
"""


def test_case_04():
    input_data = []
    expect = []
    test(remove_duplicates, input_data=sorted(input_data), expect=sorted(expect))


test_case_01()
test_case_02()
test_case_03()
test_case_04()
