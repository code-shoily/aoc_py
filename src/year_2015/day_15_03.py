"""Advent of Code Year 2015, Day 3 - Perfectly Spherical Houses in a Vacuum

Problem Link: https://adventofcode.com/2015/day/3
Difficulty: XS
Tags: cartesian set-operations navigation
"""
from dataclasses import dataclass

from helpers.input import read_input_lines


@dataclass
class Houses:
    STARTING_POSITION = (0, 0)
    visited: set[tuple[int, int]]
    current: tuple[int, int] | None

    def __init__(self, visited=None):
        self.current = self.STARTING_POSITION
        self.visited = visited or {self.STARTING_POSITION}

    def visit(self, direction):
        x, y = self.current

        match direction:
            case "^":
                self.current = (x, y + 1)
            case "v":
                self.current = (x, y - 1)
            case "<":
                self.current = (x - 1, y)
            case ">":
                self.current = (x + 1, y)

        self.visited.add(self.current)

    def __len__(self):
        return len(self.visited)

    def __and__(self, other):
        return Houses(self.visited | other.visited)


InputType = list[str]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return read_input_lines(__file__, 3)[0]


def part_1(data: InputType) -> int:
    visits = Houses()
    for direction in data:
        visits.visit(direction)
    return len(visits)


def part_2(data: InputType) -> int:
    santa_visits = Houses()
    robo_visits = Houses()

    for (position, direction) in enumerate(data):
        location = position % 2 and robo_visits or santa_visits
        location.visit(direction)

    return len(santa_visits & robo_visits)


def run_15_3(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_15_3(parsed_input))
