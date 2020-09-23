# -*- coding: utf-8 -*-
"""Advent of Code Year 2018, Day 1

.. _Link:
    https://adventofcode.com/2018/day/1

"""
from itertools import cycle
from operator import add
from functools import reduce

from helpers.input import read_from_file

DAY = 1


def get_input_data():
    return [int(i.strip()) for i in read_from_file(__file__, DAY)]


def part_1():
    return reduce(add, get_input_data())


def part_2():
    visits = set([])
    total = 0
    for i in cycle(get_input_data()):
        total += i
        if total in visits:
            break
        visits.add(total)

    return total


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 1 for year 2018

    >>> result = run()
    >>> result == {'part_1': 590, 'part_2': 83445}
    True

    """
    return dict(
        part_1=part_1(),
        part_2=part_2()
    )


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    print(run())

