"""Advent of Code Year 2022, Day 4 - Camp Cleanup
Problem Link: https://adventofcode.com/2022/day/4
Difficulty: XS
Tags: range
"""

from dataclasses import dataclass
from typing import Self

from helpers.input import read_input_lines

DAY = 4
InputType = list["Pair"]
OutputType = tuple[int, int]


@dataclass(frozen=True)
class Range:
    """Range forming assigned section to elves, range is inclusive"""

    start: int
    end: int

    @classmethod
    def from_line(cls, line: str) -> Self:
        section_from, section_to = map(int, line.split("-"))
        return cls(section_from, section_to)

    def contains(self, other: Self) -> bool:
        return self.start <= other.start and self.end >= other.end

    def overlaps_with(self, other: Self) -> bool:
        return (
            self.start <= other.start <= self.end
            or other.start <= self.start <= other.end
        )


@dataclass(frozen=True)
class Pair:
    left: Range
    right: Range

    @classmethod
    def from_line(cls, line: str) -> Self:
        left, right = map(Range.from_line, line.split(","))
        return cls(left, right)

    @property
    def is_containing(self) -> bool:
        return self.left.contains(self.right) or self.right.contains(self.left)

    @property
    def is_overlapping(self) -> bool:
        return self.left.overlaps_with(self.right)


def get_input_data() -> InputType:
    return list(map(Pair.from_line, read_input_lines(__file__, DAY)))


def part_1(data: InputType) -> int:
    return len([i for i in data if i.is_containing])


def part_2(data: InputType) -> int:
    return len([i for i in data if i.is_overlapping])


def run_22_4(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_22_4(parsed_input))
