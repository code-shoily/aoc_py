"""Advent of Code Year 2021, Day 1 - Sonar Sweep
Problem Link: https://adventofcode.com/2021/day/1
Difficulty: XS
Tags: sliding-window
"""
from helpers.input import read_input_lines


def get_input_data() -> list[int]:
    return [int(i.strip()) for i in read_input_lines(__file__, 1)]


def part_1() -> int:
    data = get_input_data()
    return len([i for i in zip(data, data[1:]) if i[0] < i[1]])


def part_2() -> int:
    data = get_input_data()
    window_sums = [sum(i) for i in zip(data, data[1:], data[2:])]
    return len([i for i in zip(window_sums, window_sums[1:]) if i[0] < i[1]])


def run() -> dict[str, int]:
    """
    Solution runner
    :return: The solutions of both parts of day 1 for year 2021

    >>> run()
    {'part_1': 1139, 'part_2': 1103}

    """
    return {"part_1": part_1(), "part_2": part_2()}


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
