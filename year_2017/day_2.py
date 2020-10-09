# -*- coding: utf-8 -*-
"""Advent of Code Year 2017, Day 2

.. _Link:
    https://adventofcode.com/2017/day/2

"""
from typing import List, Tuple

from helpers.input import read_from_file

DAY = 2


def get_input_data() -> List[List[int]]:
    data = [i.strip().split("\t") for i in read_from_file(__file__, DAY)]
    table = [[int(j) for j in i] for i in data]

    return table


def row_difference(row: List[int]) -> int:
    """
    Returns the difference between maximum and minimum of a list
    :param row:
    :return:

    >>> row_difference([5, 1, 9, 5])
    8

    >>> row_difference([7, 5, 3])
    4

    >>> row_difference([2, 4, 6, 8])
    6

    """
    return max(row) - min(row)


def checksum_1(table: List[List[int]]) -> int:
    """
    Computes the checksum of a table by summing the `row_difference` of all
    rows.

    :param table:
    :return:

    >>> checksum_1([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]])
    18

    """
    return sum(row_difference(row) for row in table)


def part_1():
    data = get_input_data()
    return checksum_1(data)


def even_division(row: List[int]) -> int:
    """
    Finds the division of two such numbers in the row where one
    evenly divides the other

    :param row:
    :return:

    >>> even_division([5, 9, 2, 8])
    4
    >>> even_division([9, 4, 7, 3])
    3
    >>> even_division([3, 8, 6, 5])
    2

    """
    row.sort()
    for idx in range(len(row)):
        divisor = row[idx]
        for number in row[idx + 1 :]:
            if not number % divisor:
                result, _ = divmod(number, divisor)
                return result
    raise ValueError


def checksum_2(table: List[List[int]]) -> int:
    """
    Finds the improved checksum

    :param table:
    :return:

    >>> checksum_2([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])
    9

    """
    return sum(even_division(i) for i in table)


def part_2():
    data = get_input_data()
    return checksum_2(data)


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 2 for year 2017

    >>> result = run()
    >>> result == {'part_1': 32020, 'part_2': 236}
    True

    """
    return dict(part_1=part_1(), part_2=part_2())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(run())
