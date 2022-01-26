from typing import Any
from main import greeting


def test(input_data: Any, expect: Any, verbose=True):
    actual = greeting(*input_data)
    is_correct = expect == actual
    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {}'.format(expect, actual, is_correct))
    return is_correct


"""
Test case 01:
"""


def test_case_01():
    input_data = ('Tung', 23, 'Vietnam')
    expect = "Hello everyone, my name is Tung, i'm 23 year old, i'm from Vietnam"
    test(input_data=input_data, expect=expect)


"""
Test case 02:
"""


def test_case_02():
    input_data = ('Chao', 23, 'Vietnam')
    expect = "Hello everyone, my name is Chao, i'm 23 year old, i'm from Vietnam"
    test(input_data=input_data, expect=expect)


test_case_01()
test_case_02()
