"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """

    # 1
    # minimum = min(arr)  # O(n)
    # # for i in range(len(arr)):  # O(n)
    # #     if arr[i] == minimum:
    # #         return i
    # return arr.index(minimum)

    # min_value = arr[0]
    # for value in arr:
    #     if value < min_value:
    #         min_value = value
    #
    # return arr.index(min_value)

    index_min = 0
    min_value = arr[index_min]

    for index, cur_value in enumerate(arr):
        if min_value > cur_value:
            min_value = cur_value
            index_min = index

    return index_min
