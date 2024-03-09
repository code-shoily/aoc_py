"""Advent of Code Year 2017, Day 9 - Stream Processing
Problem Link: https://adventofcode.com/2017/day/9
Difficulty: S
Tags:
"""

from dataclasses import dataclass

from helpers.input import read_input_lines

DAY = 9

InputType = list["StreamResult"]
OutputType = tuple[int, int]


@dataclass
class StreamResult:
    score = 0
    garbage = 0


@dataclass
class Flags:
    is_cancel = False
    is_garbage = False
    level = 0


def process(stream: str) -> StreamResult:
    input_flags = Flags()
    stream_result = StreamResult()

    for char in stream:
        match (char, input_flags):
            case (_, Flags(is_cancel=True)):
                input_flags.is_cancel = False
            case ("!", _):
                input_flags.is_cancel = True
            case (char, Flags(is_garbage=True)) if char == ">":
                input_flags.is_garbage = False
            case (_, Flags(is_garbage=True)):
                StreamResult.garbage += 1
            case ("<", _):
                input_flags.is_garbage = True
            case ("{", _):
                input_flags.level += 1
                StreamResult.score += input_flags.level
            case ("}", _):
                input_flags.level -= 1

    return stream_result


def get_input_data() -> InputType:
    return [process(stream) for stream in read_input_lines(__file__, DAY)]


def part_1(data: InputType) -> int:
    return sum(i.score for i in data)


def part_2(data: InputType) -> int:
    return sum(i.garbage for i in data)


def run_17_9(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_17_9(parsed_input))
