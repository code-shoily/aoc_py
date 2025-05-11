"""Advent of Code Year 2017, Day 5 - A Maze of Twisty Trampolines, All Alike
Problem Link: https://adventofcode.com/2017/day/5
Difficulty: XS
Tags: op-code slow
"""

from array import array
from dataclasses import dataclass, field

from aoc_py.helpers.input import read_input_lines

DAY = 5


@dataclass
class Tape:
    instructions: array[int]
    size: int = field(init=False)
    jumps: int = 0
    ptr: int = 0

    def __post_init__(self):
        self.size = len(self.instructions)

    @property
    def offset(self) -> int:
        return self.instructions[self.ptr]

    def incr(self):
        self.instructions[self.ptr] += 1

    def decr(self):
        self.instructions[self.ptr] -= 1

    def run(self, *, for_v2: bool):
        while self.ptr < self.size:
            next_ptr = self.ptr + self.offset

            if for_v2 and self.offset >= 3:
                self.decr()
            else:
                self.incr()

            self.ptr = next_ptr
            self.jumps += 1


InputType = array[int]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return array("i", map(int, read_input_lines(__file__, DAY)))


def part_1(data: InputType) -> int:
    tape = Tape(data[:])
    tape.run(for_v2=False)
    return tape.jumps


def part_2(data: InputType) -> int:
    tape = Tape(data[:])
    tape.run(for_v2=True)
    return tape.jumps


def run_17_5(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_17_5(parsed_input))
