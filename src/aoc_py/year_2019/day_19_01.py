"""Advent of Code Year 2019, Day 1 - The Tyranny of the Rocket Equation

Problem Link: https://adventofcode.com/2019/day/1
Difficulty: XS
Tags: arithmetic formulae
"""

import operator
from functools import reduce

from aoc_py.helpers.input import read_input_lines


def get_fuel(mass):
    """
    Get fuel of a module given the mass
    :param mass:
    :return:

    >>> data = [12, 14, 1969, 100756]
    >>> [get_fuel(i) for i in data]
    [2, 2, 654, 33583]

    """
    return (mass // 3) - 2


def get_additional_fuel(mass):
    """
    Calculate additional fuel for mass

    :param mass:
    :return:

    >>> get_additional_fuel(1969)
    966

    """
    fuel = get_fuel(mass)
    total = [fuel]

    while True:
        fuel = get_fuel(fuel)
        if fuel <= 0:
            break
        total.append(fuel)

    return sum(total)


InputType = list[int]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return [int(i.strip()) for i in read_input_lines(__file__, 1)]


def part_1(data: InputType) -> int:
    return reduce(operator.add, map(get_fuel, data))


def part_2(data: InputType):
    return sum(get_additional_fuel(i) for i in data)


def run_19_1(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_19_1(parsed_input))
