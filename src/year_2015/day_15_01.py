"""Advent of Code Year 2015, Day 1 - Not Quite Lisp

Problem Link: https://adventofcode.com/2015/day/1
Difficulty: XS
Tags: sequence
"""
from helpers.input import read_input_lines

InputType = list[int]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return [(1 if i == "(" else -1) for i in read_input_lines(__file__, 1)[0]]


def part_1(instructions: InputType) -> int:
    return sum(i for i in instructions)


def part_2(instructions: InputType) -> int:
    floor, step = 0, 0
    while floor != -1:
        floor, step = floor + instructions[step], step + 1

    return step


def run_15_1(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_15_1(parsed_input))
