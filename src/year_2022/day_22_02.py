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


def round_score_1(elf: int, me: int) -> int:
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


def round_score_2(opponent: int, decision: int) -> int:
    if decision == ROCK:  # lose
        if opponent == ROCK:
            return round_score_1(ROCK, SCISSORS)
        if opponent == PAPER:
            return round_score_1(PAPER, ROCK)
        if opponent == SCISSORS:
            return round_score_1(SCISSORS, PAPER)
    if decision == PAPER:  # draw
        if opponent == ROCK:
            return round_score_1(ROCK, ROCK)
        if opponent == PAPER:
            return round_score_1(PAPER, PAPER)
        if opponent == SCISSORS:
            return round_score_1(SCISSORS, SCISSORS)
    if decision == SCISSORS:  # win
        if opponent == ROCK:
            return round_score_1(ROCK, PAPER)
        if opponent == PAPER:
            return round_score_1(PAPER, SCISSORS)
        if opponent == SCISSORS:
            return round_score_1(SCISSORS, ROCK)


def get_input_data() -> InputType:
    def as_rps(elf: str, me: str) -> tuple[int, int]:
        mapping = {
            "A": ROCK,
            "B": PAPER,
            "C": SCISSORS,
            "X": ROCK,
            "Y": PAPER,
            "Z": SCISSORS,
        }
        return mapping[elf], mapping[me]

    return [as_rps(*i.split(" ")) for i in read_input_lines(__file__, DAY)]


def part_1(data: InputType) -> int:
    return sum([round_score_1(elf, me) for elf, me in data])


def part_2(data: InputType) -> int:
    return sum([round_score_2(elf, decision) for elf, decision in data])


def run_22_2(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_22_2(parsed_input))
