"""Module to read input file"""

import os


def extract_year_from_dir(location: str) -> int:
    (_, parent) = os.path.split(location)
    (_, year) = parent.split("_")

    return int(year) % 2000


def read_input_lines(location: str, day: int) -> list[str]:
    """Read input files. The location of input files is `year_xxxx/files`"""
    dir_path = os.path.dirname(os.path.realpath(location))
    year = extract_year_from_dir(dir_path)
    day_part = str(day).rjust(2, "0")

    # XXX: f"{dir_path}/files/{year}_{str(day).rjust(2, "0")}.txt") confuses black.
    with open(f"{dir_path}/files/{year}_{day_part}.txt") as inf:
        lines = inf.readlines()

    return [i.strip() for i in lines]
