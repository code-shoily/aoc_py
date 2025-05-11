"""Advent of Code Year 2017, Day 1 - Inverse Captcha

Problem Link: https://adventofcode.com/2017/day/1
Difficulty: XS
Tags: string
"""

import itertools

from aoc_py.helpers.input import read_input_lines


def repeats_next_value(digits: list[int]) -> list[int]:
    """Finds numbers that are equal to their next in the list

    >>> list(repeats_next_value([1, 1, 2, 2]))
    [1, 2]

    >>> list(repeats_next_value([1, 1, 1, 1]))
    [1, 1, 1, 1]

    >>> list(repeats_next_value([9, 1, 2, 1, 2, 1, 2, 9]))
    [9]

    """
    digits.append(digits[0])
    return list(
        map(lambda i: i[0], filter(lambda i: i[0] == i[1], itertools.pairwise(digits)))
    )


def half_half(digits: list[int]) -> tuple[list[int], list[int]]:
    """Splits a string into half, each containing list of ints

    >>> half_half([1, 2, 3, 4, 5, 6])
    ([1, 2, 3], [4, 5, 6])

    """
    mid_point = len(digits) // 2
    return digits[:mid_point], digits[mid_point:]


def solve_captcha(digits: list[int]) -> int:
    """
    Solves captcha version 2
    :param digits:
    :return:

    >>> solve_captcha([1, 2, 1, 2])
    6

    >>> solve_captcha([1, 2, 2, 1])
    0

    >>> solve_captcha([1, 2, 3, 4, 2, 5])
    4

    >>> solve_captcha([1, 2, 3, 1, 2, 3])
    12

    >>> solve_captcha([1, 2, 1, 3, 1, 4, 1, 5])
    4
    """
    a, b = half_half(digits)
    return 2 * sum([x for (x, y) in zip(a, b) if x == y])


InputType = list[int]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return [int(i) for i in read_input_lines(__file__, 1)[0]]


def part_1(data: InputType) -> int:
    return sum(repeats_next_value(data))


def part_2(data: InputType) -> int:
    return solve_captcha(data)


def run_17_1(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_17_1(parsed_input))
