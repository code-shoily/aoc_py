"""Advent of Code Year 2021, Day 2 - Dive!
Problem Link: https://adventofcode.com/2021/day/2
Difficulty: XS
Tags: command calculation
"""
from collections import defaultdict

from helpers.input import read_input_lines

InputType = list[tuple[str, int]]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    instructions = []
    for i in read_input_lines(__file__, day=2):
        (direction, x) = i.strip().split(" ")
        instructions.append((direction, int(x)))

    return instructions


def part_1(data: InputType) -> int:
    pos: dict[str, int] = defaultdict(int)

    for instruction in data:
        match instruction:
            case ("forward", x):
                pos["horizontal"] += x
            case ("backward", x):
                pos["horizontal"] -= x
            case ("up", x):
                pos["depth"] -= x
            case ("down", x):
                pos["depth"] += x

    return pos["horizontal"] * pos["depth"]


def part_2(data: InputType) -> int:
    pos: dict[str, int] = defaultdict(int)

    for instruction in data:
        match instruction:
            case ("forward", x):
                pos |= {
                    "horizontal": pos["horizontal"] + x,
                    "depth": pos["depth"] + pos["aim"] * x,
                }
            case ("backward", x):
                pos["horizontal"] -= x
            case ("up", x):
                pos["aim"] -= x
            case ("down", x):
                pos["aim"] += x

    return pos["horizontal"] * pos["depth"]


def run_21_2(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_21_2(parsed_input))
