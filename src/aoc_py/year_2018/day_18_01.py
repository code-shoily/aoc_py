"""Advent of Code Year 2018, Day 1 - Chronal Calibration

Problem Link: https://adventofcode.com/2018/day/1
Difficulty: XS
Tags: sequence
"""

from functools import reduce
from itertools import cycle
from operator import add

from aoc_py.helpers.input import read_input_lines

DAY = 1


InputType = list[int]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return [int(i.strip()) for i in read_input_lines(__file__, DAY)]


def part_1(data: InputType) -> int:
    return reduce(add, data)


def part_2(data: InputType) -> int:
    visits = set([])
    total = 0
    for i in cycle(data):
        total += i
        if total in visits:
            break
        visits.add(total)

    return total


def run_18_1(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_18_1(parsed_input))
