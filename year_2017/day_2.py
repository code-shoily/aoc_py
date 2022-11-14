"""Advent of Code Year 2017, Day 2 - Corruption Checksum

Problem Link: https://adventofcode.com/2017/day/2
"""
from helpers.input import read_input_lines


def get_input_data() -> list[list[int]]:
    data = [i.strip().split("\t") for i in read_input_lines(__file__, 2)]
    table = [[int(j) for j in i] for i in data]

    return table


def row_difference(row: list[int]) -> int:
    """Returns the difference between maximum and minimum of a list

    >>> row_difference([5, 1, 9, 5])
    8

    >>> row_difference([7, 5, 3])
    4

    >>> row_difference([2, 4, 6, 8])
    6

    """
    return max(row) - min(row)


def checksum_1(table: list[list[int]]) -> int:
    """Computes the checksum of a table by summing the `row_difference` of all rows.

    >>> checksum_1([[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]])
    18

    """
    return sum(row_difference(row) for row in table)


def even_division(row: list[int]) -> int:
    """Finds the division of two such numbers in the row where one evenly divides the other

    >>> even_division([2, 5, 8, 9])
    4
    >>> even_division([3, 4, 7, 9])
    3
    >>> even_division([3, 5, 6, 8])
    2

    """
    for (idx, _) in enumerate(row):
        divisor = row[idx]
        for number in row[idx + 1 :]:
            if not number % divisor:
                result, _ = divmod(number, divisor)
                return result


def checksum_2(table: list[list[int]]) -> int:
    """Finds the improved checksum

    >>> checksum_2([[5, 9, 2, 8], [9, 4, 7, 3], [3, 8, 6, 5]])
    9

    """
    return sum(even_division(sorted(i)) for i in table)


def part_1():
    return checksum_1(get_input_data())


def part_2():
    return checksum_2(get_input_data())


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 2 for year 2017

    >>> run()
    {'part_1': 32020, 'part_2': 236}

    """
    return {"part_1": part_1(), "part_2": part_2()}


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
