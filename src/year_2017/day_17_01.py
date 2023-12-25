"""Advent of Code Year 2017, Day 1 - Inverse Captcha

Problem Link: https://adventofcode.com/2017/day/1
Difficulty: XS
Tags: string
"""
from helpers.input import read_input_lines


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


type InputType = str
type OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return read_input_lines(__file__, 1)[0]


def part_1(data: InputType) -> int:
    return sum(repeats_next_value(data))


def part_2(data: InputType) -> int:
    return solve_captcha(data)


def run_17_1(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_17_1(parsed_input))
