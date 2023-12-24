"""Advent of Code Year 2022, Day 1
Problem Link: https://adventofcode.com/2022/day/1
Difficulty: XS
Tags: section-parse sort
"""
from helpers.input import read_input_lines

DAY = 1


type InputType = list[int]
type OutputType = tuple[int, int]

def get_input_data() -> InputType:
    calories = []
    current_calories = 0
    for elf_calorie in [i.strip() for i in read_input_lines(__file__, DAY)]:
        if not elf_calorie:
            calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(elf_calorie)

    return calories


def part_1(data: InputType) -> int:
    return sorted(data, reverse=True)[0]


def part_2(data: InputType) -> int:
    return sum(sorted(data, reverse=True)[:3])


def run_22_1(data: InputType) -> OutputType:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_22_1(parsed_input))
