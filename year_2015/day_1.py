"""Advent of Code Year 2015, Day 1 - Not Quite Lisp

Problem Link: https://adventofcode.com/2015/day/1
"""
from helpers.input import read_input_lines


def get_input_data() -> str:
    return read_input_lines(__file__, 1)[0]


def get_floor(instructions: str) -> int:
    floor = 0
    for instruction in instructions:
        match instruction:
            case "(":
                floor += 1
            case ")":
                floor -= 1

    return floor


def part_1() -> int:
    return get_floor(get_input_data())


def get_basement_position(instructions: str) -> int:
    floor = 0
    for (position, instruction) in enumerate(instructions):
        match floor:
            case "(":
                floor += 1
            case ")":
                floor -= 1
            case -1:
                return position


def part_2() -> int:
    return get_basement_position(get_input_data())


def run() -> dict[str, int]:
    return {
        "part_1": part_1(),
        "part_2": part_2()
    }


if __name__ == "__main__":
    print(run())
