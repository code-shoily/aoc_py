"""Advent of Code Year 2015, Day 1 - Not Quite Lisp

Problem Link: https://adventofcode.com/2015/day/1
"""
from helpers.input import read_input_lines


def get_input_data() -> list[int]:
    return [int(i.strip()) for i in read_input_lines(__file__, 1)]


def part_1() -> int:
    data = get_input_data()
    data_set = set(data)

    for i in data:
        rem = 2020 - i
        if rem in data_set:
            return i * rem


def part_2() -> int:
    data = get_input_data()
    data_set = set(data)

    for i in data:
        for j in data[1:]:
            rem = 2020 - (i + j)
            if rem in data_set:
                return i * j * rem


def run() -> dict[str, int]:
    """
    Solution runner
    :return: The solutions of both parts of day 1 for year 2020

    >>> run()
    {'part_1': 1014624, 'part_2': 80072256}

    """
    return {
        "part_1": part_1(),
        "part_2": part_2()
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
