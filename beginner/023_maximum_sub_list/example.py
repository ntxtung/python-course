"""
Fact: the sub list is the continuous part of the list
Write a function maximum_sub_list that:
Input: (input_list: list[int])
Output: find the contiguous sublist (containing at least one number) which has the largest sum and return its sum

For example:
input_list = [-2, 1, -3 , 4, -1, 2, 1, -5, 4]
output = 6
Explanation: [4, -1, 2, 1] has the largest sum = 6.

Source: https://leetcode.com/problems/maximum-subarray/
"""


def maximum_sub_list(input_list: list[int]) -> int:
    max_sums = None

    for start_index in range(0, len(input_list)):
        for end_index in range(1, len(input_list) + 1):
            if end_index > start_index:
                sub_list = input_list[start_index:end_index]
                sum_sub_list = sum(sub_list)

                if max_sums is not None:
                    max_sums = max(max_sums, sum_sub_list)
                else:
                    max_sums = sum_sub_list

    return max_sums


print(maximum_sub_list([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
