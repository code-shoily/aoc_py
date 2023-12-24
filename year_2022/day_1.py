"""Advent of Code Year 2022, Day 1
Problem Link: https://adventofcode.com/2022/day/1
Difficulty: XS
Tags: section-parse sort
"""
from helpers.input import read_input_lines

DAY = 1


def get_input_data() -> list[int]:
    calories = []
    current_calories = 0
    for elf_calorie in [i.strip() for i in read_input_lines(__file__, DAY)]:
        if not elf_calorie:
            calories.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(elf_calorie)

    return calories


def part_1() -> int:
    data = get_input_data()
    return sorted(data, reverse=True)[0]


def part_2() -> int:
    data = get_input_data()
    return sum(sorted(data, reverse=True)[:3])


def run() -> dict[str, int]:
    """
    Solution runner
    :return: The solutions of both parts of day 1 for year 2022

    >>> run()
    {'part_1': ,70720 'part_2': 207_148}

    """
    return {
        "part_1": part_1(),
        "part_2": part_2()
    }


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    print(run())

