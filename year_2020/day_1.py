# -*- coding: utf-8 -*-
"""Advent of Code Year 2020, Day 1

.. _Link:
    https://adventofcode.com/2020/day/1

"""

from helpers.input import read_input_lines

DAY = 1


def get_input_data():
    return [int(i.strip()) for i in read_input_lines(__file__, DAY)]


def part_1():
    data = get_input_data()
    data_set = set(data)

    for i in data:
        rem = 2020 - i
        if rem in data_set:
            return i * rem


def part_2():
    data = get_input_data()
    data_set = set(data)

    for i in data:
        for j in data[1:]:
            rem = 2020 - (i + j)
            if rem in data_set:
                return i * j * rem


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 1 for year 2020

    >>> result = run()
    >>> result == {'part_1': 1_014_624, 'part_2': 80_072_256}
    True

    """
    return dict(part_1=part_1(), part_2=part_2())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(run())
