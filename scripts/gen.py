import os
import sys
from os import O_CREAT, O_EXCL, O_WRONLY

import requests

CURRENT_YEAR = 2023
FLAGS = O_CREAT | O_EXCL | O_WRONLY
INPUT_URL = "https://adventofcode.com/{}/day/{}/input"
TEMPLATE = '''\
"""Advent of Code Year {0}, Day {1} - <?TITLE?>
Problem Link: https://adventofcode.com/{0}/day/{1}
Difficulty: 
Tags:
"""

from helpers.input import read_input_lines

DAY = {1}


def get_input_data() -> list[str]:
    return read_input_lines(__file__, DAY)


def part_1() -> int:
    data = get_input_data()
    return 0


def part_2() -> int:
    data = get_input_data()
    return 0


def run() -> dict[str, int]:
    """
    Solution runner
    :return: The solutions of both parts of day {1} for year {0}

    >>> run()
    {{'part_1': 0, 'part_2': 0}}

    """
    return {{
        "part_1": part_1(),
        "part_2": part_2()
    }}


if __name__ == '__main__':
    import doctest

    doctest.testmod()

    print(run())

'''


def fetch_input_data(year, day):
    return requests.get(
        INPUT_URL.format(year, day), cookies={"session": os.environ.get("COOKIE", None)}
    ).text


def add_input_stub(year, day):
    file_handler = os.open(f"year_{year}/files/{day}.dat", FLAGS)
    input_data = fetch_input_data(year, day)
    with os.fdopen(file_handler, "w") as f:
        f.write(input_data)


def add_solution_module(year, day):
    file_handler = os.open(f"year_{year}/day_{day}.py", FLAGS)
    with os.fdopen(file_handler, "w") as f:
        f.write(TEMPLATE.format(year, day))


if __name__ == "__main__":
    _, year_, day_ = sys.argv
    assert 2015 <= int(year_) <= CURRENT_YEAR
    assert 1 <= int(day_) <= 25
    add_input_stub(year_, day_)
    add_solution_module(year_, day_)
