"""Advent of Code Year 2020, Day 6 - Custom Customs
Problem Link: https://adventofcode.com/2020/day/6
Difficulty: XS
Tags: section-parse set
"""

import itertools
from functools import partial, reduce
from typing import Callable

from aoc_py.helpers.input import read_input_lines

DAY = 6

InputType = list[list[str]]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return [
        list(section)
        for non_empty, section in itertools.groupby(
            read_input_lines(__file__, DAY), bool
        )
        if non_empty
    ]


def count_by(by: Callable[[set, set], set], responses: list[str]) -> int:
    return len(reduce(by, [set(i) for i in responses[1:]], set(responses[0])))


def solve_by(by: Callable[[set, set], set], responses: InputType) -> int:
    return sum(map(partial(count_by, by), responses))


def part_1(responses: InputType) -> int:
    return solve_by(set.union, responses)


def part_2(responses: InputType) -> int:
    return solve_by(set.intersection, responses)


def run_20_6(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_20_6(parsed_input))
