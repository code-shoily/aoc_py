import os
from typing import List


def read_from_file(location: str, day: int) -> List[str]:
    dir_path = os.path.dirname(os.path.realpath(location))
    with open(f"{dir_path}/files/{day}.dat") as inf:
        lines = inf.readlines()

    return lines
