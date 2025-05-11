"""Advent of Code Year 2022, Day 3 - Rucksack Reorganization
Problem Link: https://adventofcode.com/2022/day/3
Difficulty: XS
Tags: set ascii
"""

from dataclasses import dataclass
from typing import Self

from aoc_py.helpers.input import read_input_lines

DAY = 3


@dataclass
class Rucksack:
    rucksack: str
    item_a: str
    item_b: str

    @classmethod
    def from_line(cls, line: str) -> Self:
        mid_point = len(line) // 2
        item_a, item_b = line[:mid_point], line[mid_point:]
        return cls(line, item_a, item_b)

    @property
    def priority(self) -> int:
        common, *_ = {*self.item_a} & {*self.item_b}
        return get_priority(common)


InputType = list[Rucksack]
OutputType = tuple[int, int]


def get_priority(letter: str) -> int:
    if letter.islower():
        return 1 + ord(letter) - ord("a")
    return (ord(letter) - ord("A") + 1) + 26


def in_groups(rucksacks: list[Rucksack]) -> list[list[Rucksack]]:
    groups = []
    left, right = 0, 3

    while right < len(rucksacks) + 3:
        groups.append(rucksacks[left:right])
        left += 3
        right += 3

    return groups


def badge(group: list[Rucksack]):
    [a, b, c] = map(lambda i: i.rucksack, group)
    common, *_ = {*a} & {*b} & {*c}
    return get_priority(common)


def get_input_data() -> InputType:
    return [Rucksack.from_line(i) for i in read_input_lines(__file__, DAY)]


def part_1(data: InputType) -> int:
    return sum([i.priority for i in data])


def part_2(data: InputType) -> int:
    return sum([badge(i) for i in in_groups(data)])


def run_22_3(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_22_3(parsed_input))
