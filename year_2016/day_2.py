# -*- coding: utf-8 -*-
"""Advent of Code Year 2016, Day 2

.. _Link:
    https://adventofcode.com/2016/day/2

"""
from dataclasses import dataclass
from typing import List, Tuple, Dict

from helpers.input import read_input_lines

DAY = 2
DIAL_PAD_1 = "1 2 3\n4 5 6\n7 8 9"
DIAL_PAD_2 = "_ _ 1 _ _\n_ 2 3 4 _\n5 6 7 8 9\n_ A B C _\n_ _ D _ _"


def get_input_data():
    return [i.strip() for i in read_input_lines(__file__, DAY)]


@dataclass
class SecuritySystem:
    pad: Dict[Tuple[int, int], str]
    reverse_pad: Dict[str, Tuple[int, int]]
    keys: List[str]
    position: Tuple[int, int]

    def __init__(self):
        self.pad = {}
        self.keys = []
        self.reverse_pad = {}

    def setup(self, pad: str, starting_position: str):
        """
        Sets up the security system with pad and starting position.

        :param pad:
        :param starting_position:
        :return:

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

    def run_sequences(self, sequences: List[str]) -> str:
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


def part_1():
    system = SecuritySystem()
    system.setup(DIAL_PAD_1, "5")

    return system.run_sequences(get_input_data())


def part_2():
    system = SecuritySystem()
    system.setup(DIAL_PAD_2, "5")

    return system.run_sequences(get_input_data())


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 2 for year 2016

    >>> assert run() == {'part_1': '76792', 'part_2': 'A7AC3'}

    """
    return dict(part_1=part_1(), part_2=part_2())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(run())
