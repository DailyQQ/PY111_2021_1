def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    a = 0
    for i in brackets_row:
        if i == "(":
            a += 1
        elif i == ")":
            a -= 1
        if a < 0:
            return False
    if a == 0:
        return True
    return False

    # if brackets_row != '' and (brackets_row[0] == ')' or brackets_row[-1] == '('
    #                            or brackets_row.count('(') != brackets_row.count(')')):
    #     return False  # Уже проходит все тесты.
    # return True

    # brackets_open = "("
    # brackets_closed = ")"
    # stack = []  # стэк для входа-выхода скобок
    # for index, elem in enumerate(brackets_row):
    #     if elem in brackets_open:
    #         stack.append(elem)
    #         # print(f"Вход: {len(stack)}")
    #     if elem in brackets_closed:
    #         # print(f"Выходят: {len(stack)}")
    #         if len(stack) == 0:
    #             return False
    #         stack.pop()
    #
    #     # print(f"Прошли шаг - длина: {len(stack)}")
    #     if index == len(brackets_row) - 1:
    #         if len(stack) > 0:
    #             return False
    # return True


