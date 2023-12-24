import os
import sys
from os import O_CREAT, O_EXCL, O_WRONLY
from typing import Callable

import requests

CURRENT_YEAR = 2023
FLAGS = O_CREAT | O_EXCL | O_WRONLY
INPUT_URL = "https://adventofcode.com/{}/day/{}/input"
SOLUTION_TEMPLATE = '''\
"""Advent of Code Year {0}, Day {1} - <?TITLE?>
Problem Link: https://adventofcode.com/{0}/day/{1}
Difficulty: 
Tags:
"""

from helpers.input import read_input_lines

DAY = {1}

type InputType = list[str]
type OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return read_input_lines(__file__, DAY)


def part_1(data: InputType) -> int:
    return 0


def part_2(data: InputType) -> int:
    return 0


def run(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == '__main__':
    parsed_input = get_input_data()
    print(run(parsed_input))

'''

TEST_TEMPLATE = '''
from year_{0}.day_{1} import get_input_data, run


def test_day_{1}_works():
    parsed_input = get_input_data()
    assert run(parsed_input) == (0, 0)
'''


def fetch_input_data(year, day):
    return requests.get(
        INPUT_URL.format(year, day), cookies={"session": os.environ.get("COOKIE", None)}
    ).text


def add_file(file_name: str, template: str | None, year: int, day: int) -> str:
    file_handler = os.open(file_name, FLAGS)
    input_data = fetch_input_data(year, day)
    with os.fdopen(file_handler, "w") as f:
        f.write(template.format(year, day)) if template else f.write(input_data)
    return file_name


def format_year_folder(year: int) -> str:
    return f"year_{year % 2000}"


def format_day_file(day: int, ext: str = "py") -> str:
    return f"day_{str(day).rjust(2, "0")}.{ext}"


def add_input_stub(year, day) -> str:
    return add_file(
        f"src/{format_year_folder(year)}/files/{format_day_file(day, "txt")}",
        None,
        year,
        day)


def add_solution_module(year, day) -> str:
    return add_file(
        f"src/{format_year_folder(year)}/{format_day_file(day)}",
        SOLUTION_TEMPLATE,
        year,
        day)


def add_test_module(year, day) -> str:
    return add_file(
        f"test/test_{format_year_folder(year)}/test_{format_day_file(day)}",
        TEST_TEMPLATE,
        year,
        day)


def log_result(func: Callable[[int, int], str], prefix: str, year: int, day: int):
    try:
        file_name = func(year, day)
        print(f"[{prefix} - SUCCESS] File written: {file_name}")
    except FileExistsError:
        print(f"[{prefix} - EXISTS] File already exists")


if __name__ == "__main__":
    _, year_, day_ = sys.argv
    assert 2015 <= int(year_) <= CURRENT_YEAR
    assert 1 <= int(day_) <= 25

    log_result(add_input_stub, "INPUT", year_, day_)
    log_result(add_solution_module, "SOLUTION", year_, day_)
    log_result(add_test_module, "TEST", year_, day_)
