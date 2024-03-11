"""Advent of Code Year 2023, Day 4 - Scratchcards
Problem Link: https://adventofcode.com/2023/day/4
Difficulty: S
Tags: set
"""

from dataclasses import dataclass
from typing import Self

from helpers.input import read_input_lines

DAY = 4

InputType = list["Card"]
OutputType = tuple[int, int]


@dataclass
class Card:
    card_id: int
    winning_set: set[int]
    my_set: set[int]

    def winning_card_ids(self, highest_card_id: int) -> list[int]:
        card_id_range = range(1, 1 + len(self.winning_set & self.my_set))
        return [self.card_id + i for i in card_id_range][: highest_card_id + 1]

    @property
    def point(self):
        power = len(self.winning_set & self.my_set) - 1
        return 2**power if power >= 0 else 0

    @classmethod
    def from_line(cls, line: str) -> Self:
        lhs, rhs = line.removeprefix("Card ").split(": ")
        winning, mine = ({int(i) for i in side.split()} for side in rhs.split(" | "))
        return cls(int(lhs), winning, mine)


def get_input_data() -> InputType:
    return list(map(Card.from_line, read_input_lines(__file__, DAY)))


def part_1(data: InputType) -> int:
    return sum(map(lambda i: i.point, data))


def part_2(data: InputType) -> int:
    last_card_id = max(i.card_id for i in data)
    tally = {i: 1 for i in range(1, last_card_id + 1)}

    for card in data:
        for winning_card_id in card.winning_card_ids(last_card_id):
            tally[winning_card_id] += tally[card.card_id]

    return sum(map(lambda i: tally[i.card_id], data))


def run_23_4(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_23_4(parsed_input))
