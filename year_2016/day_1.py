"""Advent of Code Year 2016, Day 1 - No Time for a Taxicab

Problem Link: https://adventofcode.com/2016/day/1
"""
from collections import namedtuple
from dataclasses import dataclass
from enum import Enum, auto

from helpers.input import read_input_lines

Point = namedtuple("Point", "x, y")


class LR(Enum):
    LEFT = auto()
    RIGHT = auto()

    @classmethod
    def get_direction(cls, abbr: str):
        return {"L": cls.LEFT, "R": cls.RIGHT}[abbr]


class Directions(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()
    WEST = auto()

    @classmethod
    def next_direction(cls, current, lr: LR):
        return {
            cls.NORTH: {LR.LEFT: cls.WEST, LR.RIGHT: cls.EAST},
            cls.SOUTH: {LR.LEFT: cls.EAST, LR.RIGHT: cls.WEST},
            cls.EAST: {LR.LEFT: cls.NORTH, LR.RIGHT: cls.SOUTH},
            cls.WEST: {LR.LEFT: cls.SOUTH, LR.RIGHT: cls.NORTH},
        }[current][lr]

    @classmethod
    def next_direction_function(cls, direction, command):
        next_direction = cls.next_direction(direction, command.face)
        block = command.blocks
        return {
            cls.NORTH: lambda x, y: Point(x=x, y=y + block),
            cls.SOUTH: lambda x, y: Point(x=x, y=y - block),
            cls.EAST: lambda x, y: Point(x=x - block, y=y),
            cls.WEST: lambda x, y: Point(x=x + block, y=y),
        }[next_direction]


@dataclass
class Command:
    face: LR
    blocks: int


@dataclass
class CityGrid:
    face: Directions
    position: Point

    def __init__(self):
        self.position = Point(x=0, y=0)
        self.face = Directions.NORTH

    def move(self, command: Command):
        next_direction = Directions.next_direction(self.face, command.face)
        func = Directions.next_direction_function(self.face, command)
        self.position = func(*self.position)
        self.face = next_direction

    def __len__(self):
        x, y = self.position
        return abs(x) + abs(y)


def parse_command(command: str):
    face, *blocks = command.strip()
    return Command(face=LR.get_direction(face), blocks=int("".join(blocks)))


def get_input_data():
    return map(parse_command, read_input_lines(__file__, 1)[0].split(","))


def part_1():
    city_grid = CityGrid()
    for command in get_input_data():
        city_grid.move(command)

    return len(city_grid)


def points_between(start: Point, end: Point) -> list[Point]:
    """Returns all points between two points

    :param start: Starting point
    :param end: Ending point (Inclusive)
    :return: List of all points between `start` and `end`

    >>> [tuple(i) for i in points_between((0, 0), (0, -3))]
    [(0, 0), (0, -1), (0, -2), (0, -3)]

    >>> [tuple(i) for i in points_between((-1, -4), (-4, -4))]
    [(-1, -4), (-2, -4), (-3, -4), (-4, -4)]

    >>> [tuple(i) for i in points_between((3, 5), (1, 5))]
    [(3, 5), (2, 5), (1, 5)]

    """
    output = []
    xs, ys = start
    xe, ye = end
    is_reversed = False

    if xs > xe:
        xs, xe = xe, xs
        is_reversed = True
    if ys > ye:
        ys, ye = ye, ys
        is_reversed = True

    if xs == xe:
        for i in range(ys, ye + 1):
            output.append(Point(xs, i))
    else:
        for i in range(xs, xe + 1):
            output.append(Point(i, ys))

    return list(reversed(output)) if is_reversed else output


def part_2():
    city_grid = CityGrid()
    current_path = city_grid.position
    visits = set()

    for command in get_input_data():
        city_grid.move(command)
        points = points_between(current_path, city_grid.position)
        point_set = set(points) ^ {city_grid.position}
        current_path = city_grid.position

        for point in points:
            if point in visits:
                return abs(point.x) + abs(point.y)
        else:
            visits |= point_set


def run() -> dict[str, int]:
    """
    Solution runner
    :return: The solutions of both parts of day 3 for year 2016

    >>> run()
    {'part_1': 253, 'part_2': 126}

    """
    return {
        "part_1": part_1(),
        "part_2": part_2()
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print(run())
