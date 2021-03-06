# -*- coding: utf-8 -*-
"""Advent of Code Year 2019, Day 2

.. _Link:
    https://adventofcode.com/2019/day/2

"""
import array

from helpers.input import read_from_file
from helpers.int_code import IntCode

DAY = 2


def get_input_data():
    return array.array("I", map(int, read_from_file(__file__, DAY)[0].split(",")))


def part_1():
    program = get_input_data()
    program[1] = 12
    program[2] = 2

    int_code = IntCode(program)
    int_code.run()

    return int_code.result


def part_2():
    desired_output = 19690720
    program = get_input_data()
    int_code = IntCode(program)

    for i in range(0, 100):
        for j in range(0, 100):
            fixed_program = program[:]
            fixed_program[1] = i
            fixed_program[2] = j

            int_code.reset(fixed_program)
            int_code.run()

            if int_code.result == desired_output:
                return i * 100 + j

    raise ValueError


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 2 for year 2019

    >>> assert run() == {'part_1': 3562624, 'part_2': 8298}

    """
    return dict(part_1=part_1(), part_2=part_2())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(run())
