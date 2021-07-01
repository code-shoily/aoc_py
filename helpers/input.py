"""Module to read input file"""
import os


def read_input_lines(location: str, day: int) -> list[str]:
    """Read input files. In our current setup, the location of input files is `year_xxxx/files`"""
    dir_path = os.path.dirname(os.path.realpath(location))
    with open(f"{dir_path}/files/{day}.dat") as inf:
        lines = inf.readlines()

    return lines
