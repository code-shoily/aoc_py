"""Advent of Code Year 2022, Day 2 - Rock, Paper, Scissors
Problem Link: https://adventofcode.com/2022/day/2
Difficulty: XS
Tags: mapping
"""

from helpers.input import read_input_lines

DAY = 2

InputType = list[tuple[int, int]]
OutputType = tuple[int, int]

ROCK, PAPER, SCISSORS = 1, 2, 3
LOSE, DRAW, WIN = 0, 3, 6


def get_score(elf: int, me: int) -> int:
    match (elf, me):
        case (elf, me) if (elf, me) in {
            (PAPER, ROCK),
            (SCISSORS, PAPER),
            (ROCK, SCISSORS),
        }:
            return LOSE + me
        case (x, y) if x == y:
            return DRAW + me
        case _:
            return WIN + me


def strategic_score(elf: int, outcome: int) -> int:
    losing_move = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}
    winning_move = {ROCK: PAPER, PAPER: SCISSORS, SCISSORS: ROCK}
    my_move = {ROCK: losing_move[elf], PAPER: elf, SCISSORS: winning_move[elf]}

    return get_score(elf, my_move[outcome])


def get_input_data() -> InputType:
    def as_rps(elf: str, me: str) -> tuple[int, int]:
        str_to_rps = {
            "A": ROCK,
            "B": PAPER,
            "C": SCISSORS,
            "X": ROCK,
            "Y": PAPER,
            "Z": SCISSORS,
        }
        return str_to_rps[elf], str_to_rps[me]

    return [as_rps(*i.split(" ")) for i in read_input_lines(__file__, DAY)]


def part_1(data: InputType) -> int:
    return sum([get_score(elf, me) for elf, me in data])


def part_2(data: InputType) -> int:
    return sum([strategic_score(elf, decision) for elf, decision in data])


def run_22_2(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_22_2(parsed_input))
