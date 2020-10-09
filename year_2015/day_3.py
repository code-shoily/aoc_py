from dataclasses import dataclass
from typing import Set, Tuple, Optional

from helpers.input import read_from_file

DAY = 3
CLOSURES = {
    "^": lambda x, y: (x, y + 1),
    "v": lambda x, y: (x, y - 1),
    "<": lambda x, y: (x - 1, y),
    ">": lambda x, y: (x + 1, y),
}


@dataclass
class Houses:
    STARTING_POSITION = (0, 0)
    visited: Set[Tuple[int, int]]
    current: Optional[Tuple[int, int]]

    def __init__(self, visited=None):
        self.current = self.STARTING_POSITION
        self.visited = visited or {self.STARTING_POSITION}

    def visit(self, direction):
        self.current = CLOSURES[direction](*self.current)
        self.visited.add(self.current)

    def __len__(self):
        return len(self.visited)

    def __and__(self, other):
        return Houses(self.visited.union(other.visited))


def get_input_data():
    return read_from_file(__file__, DAY)[0]


def part_1() -> int:
    visits = Houses()
    for direction in get_input_data():
        visits.visit(direction)
    return len(visits)


def part_2() -> int:
    santa_visits = Houses()
    robo_visits = Houses()

    for (position, direction) in enumerate(get_input_data()):
        location = position % 2 and robo_visits or santa_visits
        location.visit(direction)

    return len(santa_visits & robo_visits)


def run():
    return dict(part_1=part_1(), part_2=part_2())
