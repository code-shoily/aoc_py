"""Advent of Code Year 2023, Day 4 - Scratchcards
Problem Link: https://adventofcode.com/2023/day/4
Difficulty: S
Tags: set
"""

from dataclasses import dataclass

from helpers.input import read_input_lines

DAY = 4

InputType = list["Card"]
OutputType = tuple[int, int]


@dataclass
class Card:
    id: int
    winning_set: set[int]
    my_set: set[int]

    def __post_init__(self):
        self.count = len(self.winning_set & self.my_set)

    def winning_ids(self, limit: int) -> list[int]:
        return [self.id + i for i in range(1, 1 + self.count)][: limit + 1]

    @property
    def point(self):
        power = self.count - 1
        return 2**power if power >= 0 else 0

    @classmethod
    def from_line(cls, line: str) -> "Card":
        lhs, rhs = line.removeprefix("Card ").split(": ")
        winning, mine = ({int(i) for i in side.split()} for side in rhs.split(" | "))
        return cls(int(lhs), winning, mine)


def get_input_data() -> InputType:
    return list(map(Card.from_line, read_input_lines(__file__, DAY)))


def part_1(data: InputType) -> int:
    return sum(map(lambda i: i.point, data))


def part_2(data: InputType) -> int:
    last_id = max(i.id for i in data)
    tally = {i: 1 for i in range(1, last_id + 1)}

    for card in data:
        for winning_id in card.winning_ids(last_id + 1):
            tally[winning_id] += tally[card.id]

    return sum(map(lambda i: tally[i.id], data))


def run_23_4(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_23_4(parsed_input))
