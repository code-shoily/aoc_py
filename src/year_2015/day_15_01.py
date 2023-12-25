"""Advent of Code Year 2015, Day 1 - Not Quite Lisp

Problem Link: https://adventofcode.com/2015/day/1
Difficulty: XS
Tags: sequence
"""
from helpers.input import read_input_lines

InputType = str
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return read_input_lines(__file__, 1)[0]


def part_1(instructions: InputType) -> int:
    floor = 0
    for instruction in instructions:
        match instruction:
            case "(":
                floor += 1
            case ")":
                floor -= 1

    return floor


def part_2(instructions: InputType) -> int:
    floor = 0
    for (position, instruction) in enumerate(instructions):
        if floor == -1:
            return position

        match instruction:
            case "(":
                floor += 1
            case ")":
                floor -= 1


def run_15_1(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_15_1(parsed_input))
