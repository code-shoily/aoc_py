"""Advent of Code Year 2018, Day 2 - Inventory Management System

Problem Link: https://adventofcode.com/2018/day/2
Difficulty: S
Tags: string set checksum
"""
from collections import Counter
from functools import reduce

from helpers.input import read_input_lines


def get_input_data() -> list[str]:
    return [i.strip() for i in read_input_lines(__file__, 2)]


def has_two_or_three_times(line: str) -> tuple[bool, bool]:
    """Returns if line has two or three items and returns them as (two_items, three_items)

    >>> has_two_or_three_times('abcdef')
    (False, False)

    >>> has_two_or_three_times('bababc')
    (True, True)

    >>> has_two_or_three_times('abbcde')
    (True, False)

    >>> has_two_or_three_times('abcccd')
    (False, True)

    >>> has_two_or_three_times('aabcdd')
    (True, False)

    >>> has_two_or_three_times('abcdee')
    (True, False)

    >>> has_two_or_three_times('ababab')
    (False, True)

    """
    has_two = False
    has_three = False

    for _, v in Counter(line).items():
        if v == 2:
            has_two = True
        if v == 3:
            has_three = True

    return has_two, has_three


def checksum_1(lines: list[str]) -> int:
    """Computes checksum based on product on two and three repetitions

    >>> checksum_1(['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab'])
    12

    """
    a, b = reduce(
        lambda acc, x: (acc[0] + x[0], acc[1] + x[1]),
        map(has_two_or_three_times, lines),
    )

    return a * b


def has_single_differing_char(a: str, b: str) -> int | None:
    """Checks if difference between a and b is only 1 in the same position.

    >>> has_single_differing_char('abcde', 'axcye') is None
    True

    >>> has_single_differing_char('abcde', 'abcye')
    3

    """
    idx = None
    diffs = 0
    for (i, (a, b)) in enumerate(zip(a, b)):
        if a != b:
            if diffs:
                return None
            diffs += 1
            idx = i

    return idx


def correct_box_id(lines: list[str]) -> str:
    """Finds the common letters of the correct box IDs

    >>> ids = ['abcde', 'fghij', 'klmno', 'pqrst', 'fguij', 'axcye', 'wvxyz']
    >>> correct_box_id(ids)
    'fgij'

    """
    for line_1 in lines:
        for line_2 in lines:
            if d := has_single_differing_char(line_1, line_2):  # My first walrus ;)
                return f"{line_1[:d]}{line_1[d + 1:]}"


def part_1():
    return checksum_1(get_input_data())


def part_2():
    return correct_box_id(get_input_data())


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 2 for year 2018

    >>> run()
    {'part_1': 7221, 'part_2': 'mkcdflathzwsvjxrevymbdpoq'}

    """
    return {"part_1": part_1(), "part_2": part_2()}


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
