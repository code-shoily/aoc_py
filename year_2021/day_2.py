"""Advent of Code Year 2021, Day 2
Problem Link: https://adventofcode.com/2021/day/2
"""
from collections import defaultdict

from helpers.input import read_input_lines


def get_input_data() -> list[tuple]:
    instructions = []
    for i in read_input_lines(__file__, day=2):
        (direction, x) = i.strip().split(" ")
        instructions.append((direction, int(x)))

    return instructions


def part_1() -> int:
    pos = defaultdict(int)

    for instruction in get_input_data():
        match instruction:
            case ("forward", x):
                pos["horizontal"] += x
            case ("backward", x):
                pos["horizontal"] -= x
            case ("up", x):
                pos["depth"] -= x
            case ("down", x):
                pos["depth"] += x

    return pos["horizontal"] * pos["depth"]


def part_2() -> int:
    pos = defaultdict(int)

    for instruction in get_input_data():
        match instruction:
            case ("forward", x):
                pos |= {"horizontal": pos["horizontal"] + x, "depth": pos["depth"] + pos["aim"] * x}
            case ("backward", x):
                pos["horizontal"] -= x
            case ("up", x):
                pos["aim"] -= x
            case ("down", x):
                pos["aim"] += x

    return pos["horizontal"] * pos["depth"]


def run() -> dict[str, int]:
    """
    Solution runner
    :return: The solutions of both parts of day 2 for year 2021

    >>> run()
    {'part_1': 1660158, 'part_2': 1604592846}

    """
    return {
        "part_1": part_1(),
        "part_2": part_2()
    }


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    print(run())
