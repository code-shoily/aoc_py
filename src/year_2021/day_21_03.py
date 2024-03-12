"""Advent of Code Year 2021, Day 3 - Binary Diagnostic
Problem Link: https://adventofcode.com/2021/day/3
Difficulty: S
Tags: matrix todo-refactor
"""

from collections import Counter
from typing import TypeVar

from helpers.input import read_input_lines

DAY = 3

T = TypeVar("T")
Mat = list[list[T]]
InputType = tuple[Mat, Mat]
OutputType = tuple[int, int]


def transpose(digit_list: Mat[str]) -> Mat[str]:
    return [list(i) for i in zip(*digit_list)]


def get_input_data() -> InputType:
    data = [list(i) for i in read_input_lines(__file__, DAY)]
    transposed = transpose(data)
    return data, transposed


def to_binary(lst: list[str]) -> int:
    return int("".join(lst), 2)


def part_1(data: InputType) -> int:
    gamma, epsilon = [], []
    _, transposed = data

    for column in transposed:
        (most, _), (least, _) = Counter(column).most_common()
        gamma.append(most)
        epsilon.append(least)

    gamma_rate = to_binary(gamma)
    epsilon_rate = to_binary(epsilon)

    return gamma_rate * epsilon_rate


def get_gas_rating(
    container: Mat, transposed: Mat[str], keep_most: bool, tie_breaker: str
) -> int:
    idx = 0

    while True:
        (most, most_n), (least, least_n) = Counter(transposed[idx]).most_common()
        keep = []

        for i in container:
            keep_if = tie_breaker if most_n == least_n else most if keep_most else least
            if i[idx] == keep_if:
                keep.append(i)

        if len(keep) == 1:
            return int("".join(keep[0]), 2)

        container = keep
        transposed = transpose(keep)
        idx += 1


def part_2(data: InputType) -> int:
    diagnostics, transposed = data
    o2_generator = get_gas_rating(diagnostics, transposed, True, "1")
    co2_scrubber = get_gas_rating(diagnostics, transposed, False, "0")

    return o2_generator * co2_scrubber


def run_21_3(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_21_3(parsed_input))
