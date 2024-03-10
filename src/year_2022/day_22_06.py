"""Advent of Code Year 2022, Day 6 - <?TITLE?>
Problem Link: https://adventofcode.com/2022/day/6
Difficulty:
Tags:
"""

from helpers.input import read_input_lines

DAY = 6

InputType = str
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return read_input_lines(__file__, DAY)[0]


def som_marker(signals: str, *, frame_size: int):
    pointer = 0

    while pointer < len(signals):
        frame = {*signals[pointer : pointer + frame_size]}
        if len(frame) == frame_size:
            return pointer + frame_size
        pointer += 1


def part_1(data: InputType) -> int:
    return som_marker(data, frame_size=4)


def part_2(data: InputType) -> int:
    return som_marker(data, frame_size=14)


def run_22_6(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_22_6(parsed_input))
