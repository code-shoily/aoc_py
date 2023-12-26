"""Advent of Code Year 2020, Day 3 - Toboggan Trajectory
Problem Link: https://adventofcode.com/2020/day/3
Difficulty: xs
Tags: grid
"""
from functools import reduce

from helpers.input import read_input_lines

DAY = 3
TREE = "#"
SLOPES = [(1, 1), (5, 1), (7, 1), (1, 2)]
InputType = list[list[str]]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return [list(i) for i in read_input_lines(__file__, DAY)]


def count_trees(grid: InputType, right: int, down: int) -> int:
    trees = 0
    h, v, size = 0, 0, len(grid[0])

    while v < len(grid):
        trees += 1 if grid[v][h] == TREE else 0
        h = (h + right) % size
        v = v + down

    return trees


def part_1(data: InputType) -> int:
    return count_trees(data, 3, 1)


def part_2(data: InputType) -> int:
    return reduce(lambda acc, x: acc * count_trees(data, x[0], x[1]), SLOPES, 1)


def run_20_3(data: InputType) -> tuple[int, int]:
    for_3_1 = part_1(data)
    for_others = part_2(data) * for_3_1
    return for_3_1, for_others


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_20_3(parsed_input))
