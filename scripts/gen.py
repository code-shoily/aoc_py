import os
import sys
from os import O_CREAT, O_EXCL, O_WRONLY
from typing import Callable

import requests

CURRENT_YEAR = 2023
FLAGS = O_CREAT | O_EXCL | O_WRONLY
INPUT_URL = "https://adventofcode.com/{}/day/{}/input"
SRC_TPL = '''\
"""Advent of Code Year {0}, Day {1} - <?TITLE?>
Problem Link: https://adventofcode.com/{0}/day/{1}
Difficulty: 
Tags:
"""

from helpers.input import read_input_lines

DAY = {1}

InputType = list[str]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    return read_input_lines(__file__, DAY)


def part_1(data: InputType) -> int:
    return 0


def part_2(data: InputType) -> int:
    return 0


def run_{2}_{1}(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == '__main__':
    parsed_input = get_input_data()
    print(run_{2}_{1}(parsed_input))

'''

TEST_TPL = """
from year_{0}.day_{2}_{3} import get_input_data, run_{2}_{1}


def test_day_{2}_{1}_works():
    parsed_input = get_input_data()
    assert run_{2}_{1}(parsed_input) == (0, 0)

"""


def fetch_input_data(year, day):
    return requests.get(
        INPUT_URL.format(year, day), cookies={"session": os.environ.get("COOKIE", None)}
    ).text


def do_gen(file_name: str, template: str | None, year: str, day: str) -> str:
    file_handler = os.open(file_name, FLAGS)
    input_data = fetch_input_data(year, day)
    with (os.fdopen(file_handler, "w") as f):
        (
            f.write(template.format(year, day, year[2:], day.rjust(2, "0")))
            if template
            else f.write(input_data)
        )
    return file_name


def day_part(year: str, day: str) -> str:
    return "_".join([year[2:], day.rjust(2, "0")])


def gen_input(year: str, day: str) -> str:
    return do_gen(f"src/year_{year}/files/{day_part(year, day)}.txt", None, year, day)


def gen_src(year: str, day: str) -> str:
    return do_gen(f"src/year_{year}/day_{day_part(year, day)}.py", SRC_TPL, year, day)


def gen_test(year: str, day: str) -> str:
    return do_gen(
        f"test/test_year_{year}/test_day_{day_part(year, day)}.py", TEST_TPL, year, day
    )


def log_result(func: Callable[[str, str], str], prefix: str, year: str, day: str):
    try:
        file_name = func(year, day)
        print(f"[{prefix} - SUCCESS] File written: {file_name}")
    except FileExistsError:
        print(f"[{prefix} - EXISTS] File already exists")


if __name__ == "__main__":
    _, year_, day_ = sys.argv
    assert 2015 <= int(year_) <= CURRENT_YEAR
    assert 1 <= int(day_) <= 25

    log_result(gen_input, "INPUT", year_, day_)
    log_result(gen_src, "SOLUTION", year_, day_)
    log_result(gen_test, "TEST", year_, day_)
