import pytest
from year_2020.day_20_08 import Instruction, OpCode, get_input_data, run_20_8


@pytest.mark.parametrize(
    "op_code, flip", [(OpCode.NOP, True), (OpCode.JMP, True), (OpCode.ACC, False)]
)
def test_should_flippable_suggest_correct_flips(op_code, flip):
    assert Instruction(op_code, 10).should_flip() == flip


@pytest.mark.parametrize(
    "given_op_code, expected_op_code",
    [
        (OpCode.NOP, OpCode.JMP),
        (OpCode.JMP, OpCode.NOP),
        (OpCode.ACC, OpCode.ACC),
    ],
)
def test_flip_flips_instructions_correctly(given_op_code, expected_op_code):
    instruction = Instruction(given_op_code, 10)
    instruction.flip()
    assert instruction.op_code == expected_op_code


def test_day_20_8_works():
    parsed_input = get_input_data()
    assert run_20_8(parsed_input) == (2080, 2477)
