"""Advent of Code Year 2020, Day 2 - <?TITLE?>
Problem Link: https://adventofcode.com/2020/day/2
Difficulty: 
Tags:
"""
from collections import Counter
from dataclasses import dataclass

from helpers.input import read_input_lines

DAY = 2


@dataclass(frozen=True)
class PasswordPolicy:
    range_from: int
    range_to: int
    char: str
    body: str

    def is_valid_1(self) -> bool:
        frequencies = Counter(self.body)
        return self.range_from <= frequencies[self.char] <= self.range_to

    def is_valid_2(self) -> bool:
        (a, z) = self.get_range()
        return (a == self.char) ^ (z == self.char)

    def __getitem__(self, item):
        return self.body[item - 1]

    def get_range(self):
        return self[self.range_from], self[self.range_to]


InputType = list[PasswordPolicy]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    policies: list[PasswordPolicy] = []

    for line in read_input_lines(__file__, DAY):
        [from_to, char, body] = line.split(" ")
        range_from, range_to = list(map(int, from_to.split("-")))
        policies.append(PasswordPolicy(range_from, range_to, char.strip(":"), body))

    return policies


def part_1(data: InputType) -> int:
    return len([i for i in data if i.is_valid_1()])


def part_2(data: InputType) -> int:
    return len([i for i in data if i.is_valid_2()])


def run_20_2(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_20_2(parsed_input))
