"""Advent of Code Year 2020, Day 5 - <?TITLE?>
Problem Link: https://adventofcode.com/2020/day/5
Difficulty: S
Tags: number-system
"""

import itertools

from helpers.input import read_input_lines

DAY = 5

InputType = list[int]
OutputType = tuple[int, int]


def seat_number(encoding: str) -> int:
    position = encoding.translate(str.maketrans("FLBR", "0011"))
    row, col = position[:7], position[7:]
    return int(row, 2) * 8 + int(col, 2)


def get_input_data() -> InputType:
    return sorted(seat_number(line) for line in read_input_lines(__file__, DAY))


def part_1(data: InputType) -> int:
    return data[-1]


def part_2(data: InputType) -> int:
    for a, b in itertools.pairwise(data):
        if b - a != 1:
            return a + 1
    raise ValueError("Unreachable Code")


def run_20_5(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_20_5(parsed_input))
