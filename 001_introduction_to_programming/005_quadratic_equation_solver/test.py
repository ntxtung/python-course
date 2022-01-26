from main import quadratic_equation_solver


def test(input_data: tuple[float, float, float] | None,
         expect: tuple[float, float] | None,
         verbose=True):
    actual = quadratic_equation_solver(*input_data)
    if type(actual) == tuple:
        is_correct_inverse = (expect[0] - actual[0] < 0.001) and (expect[1] - actual[1] < 0.001)
        is_correct_reverse = (expect[1] - actual[0] < 0.001) and (expect[0] - actual[1] < 0.001)
        is_correct = is_correct_reverse or is_correct_inverse
    else:
        is_correct = actual == expect

    if verbose is True:
        print('Expect: {} \t Actual: {} \t is_correct: {}'.format(expect, actual, is_correct))
    return is_correct


"""
Test case 01
"""


def test_case_01():
    input_data = (4, -1, -2)
    expect = (0.84307033081725, -0.59307033081725)
    test(input_data=input_data, expect=expect)


"""
Test case 02
"""


def test_case_02():
    input_data = (1, -1, -2)
    expect = (2, -1)
    test(input_data=input_data, expect=expect)


"""
Test case 03
"""


def test_case_03():
    input_data = (0, -1, -2)
    expect = None
    test(input_data=input_data, expect=expect)


test_case_01()
test_case_02()
test_case_03()
