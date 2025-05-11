"""Advent of Code Year 2016, Day 6 - Signals and Noise
Problem Link: https://adventofcode.com/2016/day/6
Difficulty: XS
Tags: counter
"""

from collections import Counter
from enum import IntEnum

from aoc_py.helpers.input import read_input_lines

DAY = 6

InputType = list[list[str]]
OutputType = tuple[str, str]


def get_input_data() -> InputType:
    def transpose(matrix: InputType) -> InputType:
        return [list(i) for i in zip(*matrix)]

    return transpose([list(i) for i in read_input_lines(__file__, DAY)])


class FrequencyType(IntEnum):
    MOST_FREQUENT = 0
    LEAST_FREQUENT = -1


def decode_message(signal: InputType, frequency_type: FrequencyType) -> str:
    chars = []
    for column in signal:
        (char, _) = Counter(column).most_common()[frequency_type.value]
        chars.append(char)

    return "".join(chars)


def part_1(data: InputType) -> str:
    return decode_message(data, FrequencyType.MOST_FREQUENT)


def part_2(data: InputType) -> str:
    return decode_message(data, FrequencyType.LEAST_FREQUENT)


def run_16_6(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_16_6(parsed_input))
