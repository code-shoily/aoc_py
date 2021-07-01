"""Advent of Code Year 2015, Day 1 - The Tyranny of the Rocket Equation

Problem Link: https://adventofcode.com/2019/day/1
"""
import operator
from functools import reduce

from helpers.input import read_input_lines


def get_input_data():
    return [int(i.strip()) for i in read_input_lines(__file__, 1)]


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


def part_1():
    return reduce(operator.add, map(get_fuel, get_input_data()))


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


def part_2():
    return sum(get_additional_fuel(i) for i in get_input_data())


def run() -> dict[str, int]:
    """
    Solution runner
    :return: The solutions of both parts of day 1 for year 2019

    >>> run()
    {'part_1': 3421505, 'part_2': 5129386}

    """
    return {
        "part_1": part_1(),
        "part_2": part_2()
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
