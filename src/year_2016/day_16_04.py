"""Advent of Code Year 2016, Day 4 - Security through Obscurity
Problem Link: https://adventofcode.com/2016/day/4
Difficulty: XS
Tags: checksum ascii
"""

from collections import Counter
from dataclasses import dataclass
from typing import Self

from helpers.input import read_input_lines

DAY = 4


@dataclass
class Room:
    name: str
    sector_id: int
    checksum: str

    @classmethod
    def from_str(cls, data: str) -> Self:
        tokens = data.split("-")
        name = tokens[:-1]
        [sector_id, checksum] = tokens[-1].strip("]").split("[")
        return cls(name="".join(name), sector_id=int(sector_id), checksum=checksum)

    @property
    def is_valid(self) -> bool:
        top_5 = sorted(
            Counter(self.name).most_common(), key=lambda a: (-1 * a[1], a[0])
        )[:5]
        return self.checksum == "".join([i[0] for i in top_5])

    @property
    def decrypt(self):
        return "".join(self._rotated_value(i) for i in self.name)

    def _rotated_value(self, char: str):
        return chr(ord("a") + ((ord(char) - ord("a")) + self.sector_id) % 26)


InputType = list[Room]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return list(map(Room.from_str, read_input_lines(__file__, DAY)))


def get_valid_rooms(rooms: InputType) -> InputType:
    return [room for room in rooms if room.is_valid]


def part_1(data: InputType) -> int:
    return sum([i.sector_id for i in get_valid_rooms(data)])


def part_2(data: InputType) -> int:
    for room in get_valid_rooms(data):
        if room.decrypt.startswith("northpoleobject"):
            return room.sector_id

    raise ValueError("Unreachable code")


def run_16_4(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_16_4(parsed_input))
