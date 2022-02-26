from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """

    # def fun_binary(left_part, right_part):
    #
    #     middle_index = (left_part + right_part) // 2
    #     middle_value = arr[middle_index]
    #     if middle_value == elem:
    #         return middle_index
    #     elif middle_value < elem:
    #         new_left_part = middle_index + 1
    #         return fun_binary(new_left_part, right_part)
    #     else:
    #         new_right_part = middle_index - 1
    #         return fun_binary(left_part, new_right_part)
    #
    # left_part = 0
    # right_part = len(arr) - 1
    # fun_binary(left_part, right_part)

    min_index = 0
    max_index = len(arr) - 1

    while max_index >= min_index:
        middle_index = (max_index + min_index) // 2
        value = arr[middle_index]
        if value == elem:
            return middle_index
        if value > elem:
            max_index = middle_index - 1
        if value < elem:
            min_index = middle_index + 1

    return None

