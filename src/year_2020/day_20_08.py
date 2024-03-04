"""Advent of Code Year 2020, Day 8 - <?TITLE?>
Problem Link: https://adventofcode.com/2020/day/8
Difficulty:
Tags: op-code
"""

from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Optional

from helpers.input import read_input_lines

DAY = 8


class OpCode(Enum):
    ACC = auto()
    JMP = auto()
    NOP = auto()


@dataclass
class Instruction:
    op_code: OpCode
    value: int

    def __str__(self):
        return f"{self.op_code.name}=>{self.value}"

    def should_flip(self):
        return self.op_code == OpCode.JMP or self.op_code == OpCode.NOP

    def flip(self):
        if self.should_flip():
            self.op_code = OpCode.NOP if self.op_code == OpCode.JMP else OpCode.JMP


def parse_op(instruction_vector: tuple[str, str]) -> Instruction:
    match instruction_vector[0]:
        case "acc":
            op_code = OpCode.ACC
        case "jmp":
            op_code = OpCode.JMP
        case "nop":
            op_code = OpCode.NOP
        case _:
            raise ValueError(f"Invalid command vector: {instruction_vector}")

    return Instruction(op_code, int(instruction_vector[1]))


InputType = list[Instruction]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    instructions = []
    for line in read_input_lines(__file__, DAY):
        ixn, val = line.split(" ")
        instructions.append(parse_op((ixn, val)))

    return instructions


@dataclass
class Device:
    ixns: InputType
    size: int = field(init=False)
    acc: int = 0
    ptr: int = 0
    is_ok: bool = False
    ixn_set: set[int] = field(default_factory=set)
    is_running: bool = True

    def __post_init__(self):
        self.size = len(self.ixns)

    def run(self, *, ok_only: bool) -> Optional[int]:
        while self.is_running:
            self._on_cmd()
            if self.ptr in self.ixn_set or self.ptr >= self.size:
                self.is_running = False
                if self.ptr == self.size:
                    self.is_ok = True

            self.ixn_set.add(self.ptr)

        return self._verified_result() if ok_only else self.acc

    def _verified_result(self) -> Optional[int]:
        return self.acc if self.is_ok else None

    def _on_cmd(self):
        match self.ixns[self.ptr]:
            case Instruction(OpCode.ACC, value):
                self.acc += value
                self.ptr += 1
            case Instruction(OpCode.JMP, value):
                self.ptr += value
            case _:
                self.ptr += 1


def part_1(data: InputType) -> int:
    return Device(data).run(ok_only=False)


def part_2(data: InputType) -> int:
    for idx, _ in filter(lambda i: i[1].should_flip(), enumerate(data)):
        data[idx].flip()
        if result := Device(data).run(ok_only=True):
            return result

        data[idx].flip()


def run_20_8(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_20_8(parsed_input))
