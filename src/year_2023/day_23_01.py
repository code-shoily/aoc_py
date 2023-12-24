"""Advent of Code Year 2023, Day 1 - Trebuchet?!
Problem Link: https://adventofcode.com/2023/day/1
Difficulty: XS
Tags: regex
"""
import re

from helpers.input import read_input_lines

DAY = 1


def get_input_data() -> list[str]:
    return read_input_lines(__file__, DAY)


def solve(data, regex) -> int:
    def digit(lst: list[int]) -> int:
        return lst[0] * 10 + lst[-1]

    nums = {str(i): i for i in range(10)}
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    words_to_nums = dict(map(lambda i: (i[1], i[0] + 1), enumerate(words))) | nums

    return sum([digit([words_to_nums[i] for i in re.findall(regex, i)]) for i in data])


def run() -> dict[str, int]:
    """
    Solution runner
    :return: The solutions of both parts of day 1 for year 2023

    >>> run()
    {'part_1': 53194, 'part_2': 54249}

    """
    data = get_input_data()
    return {
        "part_1": solve(data, r"\d"),
        "part_2": solve(data, r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"),
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
