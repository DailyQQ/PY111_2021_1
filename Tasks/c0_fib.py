from functools import lru_cache
from typing import Iterator


@lru_cache
def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if n in (0, 1):
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """

    if n < 0:
        raise ValueError

    a, b = 0, 1
    for i in range(0, n):
        a, b = b, a + b

    return a


def fib_generator(n: int) -> Iterator[int]:
    a, b = 0, 1
    yield a
    yield b

    for i in range(0, n):
        a, b = b, a + b
        yield a

# a, b = 0, 1
# i = 0
# while i <= n:
#     a, b = b, a + b
#     res = a + b
#     i += 1
# yield res
