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
    max_sums = 1
    for i in range(0, len(input_list)):
        for k in range(0, len(input_list)):
            sum_sublist = sum(input_list[i:k+1])
            if max_sums < sum_sublist:
                max_sums = sum_sublist
    return max_sums

