import os, sys
from os import O_CREAT, O_EXCL, O_WRONLY

FLAGS = O_CREAT | O_EXCL | O_WRONLY
TEMPLATE = '''\
# -*- coding: utf-8 -*-
"""Advent of Code Year {0}, Day {1}

.. _Link:
    https://adventofcode.com/{0}/day/{1}

"""

from helpers.input import read_from_file

DAY = {1}


def get_input_data():
    return read_from_file(__file__, DAY)


def part_1():
    data = get_input_data()
    return 0


def part_2():
    data = get_input_data()
    return 0


def run():
    """
    Solution runner
    :return: The solutions of both parts of day {1} for year {0}

    >>> result = run()
    >>> result == {{'part_1': 0, 'part_2': 0}}
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

'''

def validate_year(year: str):
    assert 2015 <= int(year) <= 2019


def validate_day(day):
    assert 1 <= int(day) <= 25


def add_input_stub(year, day):
    file_handler = os.open(f'year_{year}/files/{day}.dat', FLAGS)
    with os.fdopen(file_handler, 'w') as f:
        f.write("")


def add_solution_module(year, day):
    file_handler = os.open(f'year_{year}/day_{day}.py', FLAGS)
    with os.fdopen(file_handler, 'w') as f:
        f.write(TEMPLATE.format(year, day))


if __name__ == '__main__':
    _, year_, day_ = sys.argv
    validate_year(year_)
    validate_day(day_)
    # add_input_stub(year_, day_)
    add_solution_module(year_, day_)