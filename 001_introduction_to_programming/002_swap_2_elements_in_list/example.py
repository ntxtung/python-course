"""
Write a function swap_2_elements_in_list that:
Input: (input_list: list of any numbers, index_1: int, number2: int)
Output: the input_list but 2 index in that list is swapped each other
        return the same input_list if the indexes is incorrect
"""


def swap_2_elements_in_list(input_list: list, index_1: int, index_2: int):
    # Validation input data
    if index_1 == index_2 or \
            index_1 < 0 or \
            index_2 < 0 or \
            index_1 >= len(input_list) or \
            index_2 >= len(input_list):
        return input_list
    # Do swap
    temp_value = input_list[index_1]
    input_list[index_1] = input_list[index_2]
    input_list[index_2] = temp_value
    return input_list

