"""Advent of Code Year 2019, Day 2 - 1202 Program Alarm

Problem Link: https://adventofcode.com/2019/day/2
Difficulty: XS
Tags: op-code emulation int-code
"""
import array
from copy import copy

from helpers.input import read_input_lines
from helpers.int_code import IntCode

InputType = array.array[int]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return array.array("I", map(int, read_input_lines(__file__, 2)[0].split(",")))


def part_1(program: InputType) -> int:
    program[1] = 12
    program[2] = 2

    int_code = IntCode(program)
    int_code.run()

    return int_code.result


def part_2(program: InputType) -> int:
    desired_output = 19_690_720
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


def run_19_2(program: InputType) -> OutputType:
    return part_1(copy(program)), part_2(copy(program))


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_19_2(parsed_input))
