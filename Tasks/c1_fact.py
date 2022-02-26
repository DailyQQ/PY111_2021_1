def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """

    if n < 0:
        raise ValueError
    if n in (0, 1):
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    # if n < 0:
    #     raise ValueError
    # result = 1
    # while n > 1:
    #     result *= n
    #     n -= 1
    # return result

    # if n < 0:
    #     raise ValueError
    # a = 1
    # if n == a:
    #     return a
    # for i in range(2, n + 1):
    #     a *= i
    # return a

    # if n < 0:
    #     raise ValueError
    # if n in range(0, 1):
    #     return 1
    # for a in range(0, n):
    #     return n * (n - a)
    if n < 0:
        raise ValueError
    fact = 1
    if n == 0:
        return fact
    if n > 0:
        # yield 1
        for i in range(1, n + 1):
            fact *= i
            print(fact)
    return fact



def factorial_generator(n: int):
    # if n < 0:
    #     raise ValueError
    # f = 1
    # for _ in range(1, n + 1):
    #     f *= _
    # yield f

    # if n < 0:
    #     raise ValueError
    # if n in (0, 1):
    #     return 1
    # else:
    #     result = 1
    #
    #     for a in range(1, n+1):
    #         result *= a
    #         yield result

    # if n < 0:
    #     raise ValueError
    #
    # res = 1
    # for i in range(1, n+1):
    #     res *= i
    #     yield res

    # if n < 0:
    #     raise ValueError
    #
    # result = 1
    #
    # if n == result:
    #     return result
    # for i in range(2, n + 1):
    #     result *= i
    #     yield result

    if n < 0:
        raise ValueError
    fact = 1
    if n == 0:
        yield fact
    if n > 0:
        yield 1
        for i in range(1, n + 1):
            fact *= i
            yield fact


if __name__ == '__main__':
    # вывести список чисел факториала N!
    # f_gen = factorial_generator(6)
    #
    # print(next(f_gen))  # 0!  1
    # print(next(f_gen))  # 1!  1
    # print(next(f_gen))  # 2!  2
    # print(next(f_gen))  # 3!  6
    # print(next(f_gen))
    # print(next(f_gen))

    factorial_iterative(6)
