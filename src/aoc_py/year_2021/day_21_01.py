"""Advent of Code Year 2021, Day 1 - Sonar Sweep
Problem Link: https://adventofcode.com/2021/day/1
Difficulty: XS
Tags: sliding-window
"""

from aoc_py.helpers.input import read_input_lines

InputType = list[int]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return [int(i.strip()) for i in read_input_lines(__file__, 1)]


def part_1(data: InputType) -> int:
    return len([i for i in zip(data, data[1:]) if i[0] < i[1]])


def part_2(data: InputType) -> int:
    window_sums = [sum(i) for i in zip(data, data[1:], data[2:])]
    return len([i for i in zip(window_sums, window_sums[1:]) if i[0] < i[1]])


def run_21_1(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_21_1(parsed_input))
