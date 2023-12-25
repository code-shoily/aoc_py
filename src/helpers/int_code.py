import array
import operator
from dataclasses import dataclass
from enum import Enum
from typing import List


class OpCodes(Enum):
    ADD = 1
    MUL = 2
    END = 99


@dataclass
class IntCode:
    program: array.ArrayType
    current_pointer: int

    def __init__(self, program: array.ArrayType):
        self.program = program
        self.current_pointer = 0

    @property
    def result(self):
        if self.is_running():
            return None
        return self.program[0]

    def run(self):
        """
        Runs a program

        :return:

        >>> program = array.array('I', [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        >>> int_code = IntCode(program)
        >>> int_code.run()
        >>> int_code.result
        3500

        """
        while self.is_running():
            self.evaluate(self.program[self.current_pointer])

    def reset(self, program: array.ArrayType):
        self.current_pointer = 0
        self.program = program

    def evaluate(self, op_code):
        """
        Evaluates a single opcode.

        :param op_code:
        :return:

        >>> program = array.array('I', [1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50])
        >>> int_code = IntCode(program)
        >>> int_code.evaluate(1)
        >>> int_code.current_pointer
        4
        >>> int_code.program[3]
        70

        """
        if OpCodes(op_code) == OpCodes.ADD:
            self.__apply_binary(operator.add)
        elif OpCodes(op_code) == OpCodes.MUL:
            self.__apply_binary(operator.mul)

    def is_running(self) -> bool:
        try:
            state = OpCodes.END != OpCodes(self.program[self.current_pointer])
        except ValueError:
            state = False

        return state

    def __apply_binary(self, fn):
        pointer = self.current_pointer
        a = self.program[self.program[pointer + 1]]
        b = self.program[self.program[pointer + 2]]

        self.program[self.program[pointer + 3]] = fn(a, b)
        self.current_pointer = pointer + 4


if __name__ == "__main__":
    import doctest

    doctest.testmod()
