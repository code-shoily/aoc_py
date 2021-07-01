"""Advent of Code Year 2015, Day 1 - Not Quite Lisp

Problem Link: https://adventofcode.com/2015/day/1
"""
from helpers.input import read_input_lines


def get_input_data() -> str:
    return read_input_lines(__file__, 1)[0]


def repeats_next_value(digits: str) -> list[int]:
    """Finds numbers that are equal to their next in the list

    >>> list(repeats_next_value('1122'))
    [1, 2]

    >>> list(repeats_next_value('1111'))
    [1, 1, 1, 1]

    >>> list(repeats_next_value('91212129'))
    [9]

    """
    first, *_ = digits
    pairs = []
    for i in range(len(digits)):
        a = digits[i]
        b = first if i == len(digits) - 1 else digits[i + 1]

        if a == b:
            pairs.append(a)

    return [int(i) for i in pairs]


def part_1() -> int:
    return sum(repeats_next_value(get_input_data()))


def to_numlist(digits: str) -> list[int]:
    """Converts a string digit into a list of numbers

    >>> to_numlist('123')
    [1, 2, 3]

    >>> to_numlist('1')
    [1]

    """
    return [int(i) for i in digits]


def half_half(digits: str) -> tuple[list[int], list[int]]:
    """Splits a string into half, each containing list of ints

    >>> half_half('123456')
    ([1, 2, 3], [4, 5, 6])

    """
    mid_point = len(digits) // 2
    return to_numlist(digits[:mid_point]), to_numlist(digits[mid_point:])


def solve_captcha(digits: str) -> int:
    """
    Solves captcha version 2
    :param digits:
    :return:

    >>> solve_captcha('1212')
    6

    >>> solve_captcha('1221')
    0

    >>> solve_captcha('123425')
    4

    >>> solve_captcha('123123')
    12

    >>> solve_captcha('12131415')
    4
    """
    a, b = half_half(digits)
    return 2 * sum([x for (x, y) in zip(a, b) if x == y])


def part_2():
    data = get_input_data()
    return solve_captcha(data)


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 1 for year 2017

    >>> run()
    {'part_1': 1089, 'part_2': 1156}

    """
    return {
        "part_1": part_1(),
        "part_2": part_2()
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
