"""Advent of Code Year 2016, Day 2 - Bathroom Security

Problem Link: https://adventofcode.com/2016/day/2
Difficulty: XS
Tags: cartesian navigation
"""
from dataclasses import dataclass, field

from helpers.input import read_input_lines

DIAL_PAD_1 = "1 2 3\n4 5 6\n7 8 9"
DIAL_PAD_2 = "_ _ 1 _ _\n_ 2 3 4 _\n5 6 7 8 9\n_ A B C _\n_ _ D _ _"


@dataclass
class SecuritySystem:
    pad: dict[tuple[int, int], str] = field(default_factory=dict)
    reverse_pad: dict[str, tuple[int, int]] = field(default_factory=dict)
    keys: list[str] = field(default_factory=list)
    position: tuple[int, int] = field(default_factory=tuple)

    def setup(self, pad: str, starting_position: str):
        """
        Sets up the security system with pad and starting position.

        >>> result = {
        ...     (0, 0): '1', (0, 1): '2', (0, 2): '3',
        ...     (1, 0): '4', (1, 1): '5', (1, 2): '6',
        ...     (2, 0): '7', (2, 1): '8', (2, 2): '9'
        ... }
        >>> pad = '1 2 3\\n4 5 6\\n7 8 9'
        >>> system = SecuritySystem()
        >>> system.setup(pad, '5')
        >>> assert system.pad == result
        >>> assert system.reverse_pad == {v: k for (k, v) in system.pad.items()}
        >>> assert system.position == (1, 1)

        """
        self.__set_pad(pad)
        self.position = self.reverse_pad[starting_position]

    def run_sequences(self, sequences: list[str]) -> str:
        for sequence in sequences:
            self.__append_code(sequence)

        return "".join(self.keys)

    def __move(self, instruction):
        new_position = {
            "U": lambda x, y: (x - 1, y),
            "D": lambda x, y: (x + 1, y),
            "L": lambda x, y: (x, y - 1),
            "R": lambda x, y: (x, y + 1),
        }[instruction](*self.position)

        if new_position in self.pad:
            self.position = new_position

    def __append_code(self, sequence: str):
        for instruction in sequence:
            self.__move(instruction)

        self.keys.append(self.pad[self.position])

    def __set_pad(self, pad: str):
        row_ = 0
        col_ = 0

        rows = pad.split("\n")
        for row in rows:
            for col in row.split(" "):
                if col != "_":
                    self.pad[(row_, col_)] = col
                    self.reverse_pad[col] = (row_, col_)
                col_ += 1
            col_ = 0
            row_ += 1


type InputType = list[str]
type OutputType = tuple[str, str]


def get_input_data() -> InputType:
    return [i.strip() for i in read_input_lines(__file__, 2)]


def part_1(data: InputType) -> str:
    system = SecuritySystem()
    system.setup(DIAL_PAD_1, "5")

    return system.run_sequences(data)


def part_2(data: InputType) -> str:
    system = SecuritySystem()
    system.setup(DIAL_PAD_2, "5")

    return system.run_sequences(data)


def run_16_2(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_16_2(parsed_input))
