"""Advent of Code Year 2015, Day 5 - Doesn't He Have Intern-Elves For This?
Problem Link: https://adventofcode.com/2015/day/5
Difficulty: XS
Tags: string
"""

from helpers.input import read_input_lines

DAY = 5

InputType = list[str]
OutputType = tuple[int, int]


def has_three_vowels(line: str) -> bool:
    vowel_count = 0
    for char in line:
        if char in "aeiou":
            vowel_count += 1
        if vowel_count == 3:
            return True
    return False


def has_repeating_char(line: str) -> bool:
    return any(a == b for a, b in zip(line, line[1:]))


def has_no_bad_pair(line: str) -> bool:
    bad_pairs = [tuple(pair) for pair in ["ab", "cd", "pq", "xy"]]
    return not any((a, b) in bad_pairs for a, b in zip(line, line[1:]))


def is_nice_v1(line: str) -> bool:
    return has_three_vowels(line) and has_repeating_char(line) and has_no_bad_pair(line)


def has_sandwich(line: str) -> bool:
    return any(line[i] == line[i + 2] for i in range(0, len(line) - 2))


def has_repeating_pairs(line: str) -> bool:
    pairs = [i + j for i, j in zip(line, line[1:])]
    found_pairs = set()
    last_found = None

    for pair in pairs:
        if pair == last_found:
            last_found = None
        elif pair in found_pairs:
            return True
        else:
            found_pairs.add(pair)
            last_found = pair

    return False


def is_nice_v2(line: str) -> bool:
    return has_sandwich(line) and has_repeating_pairs(line)


def get_input_data() -> InputType:
    return read_input_lines(__file__, DAY)


def part_1(data: InputType) -> int:
    return sum([1 for line in data if is_nice_v1(line)])


def part_2(data: InputType) -> int:
    return sum([1 for line in data if is_nice_v2(line)])


def run_15_5(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_15_5(parsed_input))
