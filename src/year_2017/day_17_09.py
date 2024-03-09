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


@dataclass(frozen=True)
class StreamResult:
    score: int
    garbage: int


def process(stream: str) -> StreamResult:
    cancel_mode, garbage_mode = False, False
    level, score, garbage = 0, 0, 0

    for char in stream:
        match (char, cancel_mode, garbage_mode):
            case (_, True, _):
                cancel_mode = False
            case ("!", _, _):
                cancel_mode = True
            case (">", _, True):
                garbage_mode = False
            case (_, _, True):
                garbage += 1
            case ("<", _, _):
                garbage_mode = True
            case ("{", _, _):
                level += 1
                score += level
            case ("}", _, _):
                level -= 1

    return StreamResult(score, garbage)


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
