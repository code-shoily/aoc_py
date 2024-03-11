"""Advent of Code Year 2023, Day 2 - Cube Conundrum
Problem Link: https://adventofcode.com/2023/day/2
Difficulty: S
Tags: comparison
"""

from dataclasses import dataclass
from functools import reduce
from typing import Self

from helpers.input import read_input_lines

DAY = 2

InputType = list["Game"]
OutputType = tuple[int, int]


@dataclass
class Bag:
    red: int = 0
    green: int = 0
    blue: int = 0

    def contains_less_than(self, red: int, green: int, blue: int) -> bool:
        return self.red <= red and self.green <= green and self.blue <= blue

    @property
    def product(self):
        return self.red * self.green * self.blue

    def __or__(self, other: Self) -> Self:
        return Bag(
            max(self.red, other.red),
            max(self.green, other.green),
            max(self.blue, other.blue),
        )


@dataclass
class Game:
    game_id: int
    bags: list[Bag]

    def is_possible_game(self, red: int, green: int, blue: int) -> bool:
        return all(i.contains_less_than(red, green, blue) for i in self.bags)

    @property
    def power(self):
        return reduce(lambda a, b: a | b, self.bags).product

    @classmethod
    def from_line(cls, game_id: int, cubes: str) -> Self:
        return cls(game_id, [cls.parse_colours(cube) for cube in cubes.split("; ")])

    @staticmethod
    def parse_colours(cube: str) -> Bag:
        return Bag(
            **{
                col: int(freq)
                for (freq, col) in map(lambda i: i.split(" "), cube.split(", "))
            }
        )


def parse_line(line: str) -> tuple[int, str]:
    lhs, rhs = line.removeprefix("Game ").split(": ")
    return int(lhs), rhs


def get_input_data() -> InputType:
    result = []
    for line in read_input_lines(__file__, DAY):
        game_id, raw_cubes = parse_line(line)
        result.append(Game.from_line(game_id, raw_cubes))

    return result


def part_1(data: InputType) -> int:
    return sum(
        map(
            lambda i: i.game_id,
            filter(lambda i: i.is_possible_game(red=12, green=13, blue=14), data),
        )
    )


def part_2(data: InputType) -> int:
    return sum(i.power for i in data)


def run_23_2(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_23_2(parsed_input))
