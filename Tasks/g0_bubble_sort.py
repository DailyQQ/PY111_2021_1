from random import randint
from typing import List

from Tasks.utils import benchmark


@benchmark(10)
def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """

    n = len(container)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]

    # for _ in range(len(container)):
    #     for i in range(len(container) - 1):
    #         if container[i] > container[i + 1]:
    #             container[i], container[i + 1] = container[i + 1], container[i]

    return container


arr = [randint(-1000, 1000) for _ in range(1000)]
sort(arr)

