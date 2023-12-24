"""Advent of Code Year 2015, Day 2 - I Was Told There Would Be No Math

Problem Link: https://adventofcode.com/2015/day/2
Difficulty: XS
Tags: geometry
"""
from dataclasses import astuple, dataclass

from helpers.input import read_input_lines


@dataclass
class Paper:
    height: int
    width: int
    length: int

    def smallest_area(self) -> int:
        [a, b, *_] = sorted(astuple(self))
        return a * b

    def smallest_perimeter(self) -> int:
        [a, b, *_] = sorted(astuple(self))
        return (a + b) * 2

    def volume(self) -> int:
        return self.height * self.width * self.length

    def perimeter(self) -> int:
        height, width, length = astuple(self)
        return 2 * (height * width + width * length + length * height)

    def wrapper_size(self) -> int:
        return self.perimeter() + self.smallest_area()

    def ribbon_size(self) -> int:
        return self.smallest_perimeter() + self.volume()


def get_input_data() -> list[Paper]:
    return [Paper(*map(int, i.split("x"))) for i in read_input_lines(__file__, 2)]


def part_1() -> int:
    return sum(i.wrapper_size() for i in get_input_data())


def part_2() -> int:
    return sum(i.ribbon_size() for i in get_input_data())


def run() -> dict[str, int]:
    """
    Solution runner
    :return: The solutions of both parts of day 2 for year 2015

    >>> run()
    {'part_1': 1606483, 'part_2': 3842356}

    """
    return {"part_1": part_1(), "part_2": part_2()}


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
