"""Advent of Code Year 2020, Day 1 - Report Repair

Problem Link: https://adventofcode.com/2020/day/1
Difficulty: XS
Tags: n-sum
"""

from aoc_py.helpers.input import read_input_lines

InputType = list[int]
OutputType = tuple[int, int]


def get_input_data() -> list[int]:
    return [int(i.strip()) for i in read_input_lines(__file__, 1)]


def part_1(data: InputType) -> int:
    data_set = set(data)

    for i in data:
        rem = 2020 - i
        if rem in data_set:
            return i * rem

    raise ValueError("Unreachable Code")


def part_2(data: InputType) -> int:
    data_set = set(data)

    for i in data:
        for j in data[1:]:
            rem = 2020 - (i + j)
            if rem in data_set:
                return i * j * rem

    raise ValueError("Unreachable Code")


def run_20_1(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_20_1(parsed_input))
