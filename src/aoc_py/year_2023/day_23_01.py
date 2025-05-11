"""Advent of Code Year 2023, Day 1 - Trebuchet?!
Problem Link: https://adventofcode.com/2023/day/1
Difficulty: XS
Tags: regex
"""

import re

from aoc_py.helpers.input import read_input_lines

DAY = 1

InputType = list[str]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return read_input_lines(__file__, DAY)


def solve(data: InputType, regex: str) -> int:
    def digit(lst: list[int]) -> int:
        return lst[0] * 10 + lst[-1]

    nums = {str(i): i for i in range(10)}
    words = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    words_to_nums = dict(map(lambda i: (i[1], i[0] + 1), enumerate(words))) | nums

    return sum([digit([words_to_nums[i] for i in re.findall(regex, i)]) for i in data])


def run_23_1(data: InputType) -> OutputType:
    return (
        solve(data, r"\d"),
        solve(data, r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))"),
    )


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_23_1(parsed_input))
