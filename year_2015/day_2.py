from collections import namedtuple
from operator import mul, add
from typing import Iterator

from helpers.input import read_from_file

DAY = 2


class Paper(namedtuple("_", "height,width,length")):
    def smallest_area(self) -> int:
        return mul(*sorted(self)[:2])

    def smallest_perimeter(self) -> int:
        return add(*sorted(self)[:2]) * 2

    def volume(self) -> int:
        return self.height * self.width * self.length

    def perimeter(self) -> int:
        height, width, length = self
        return 2 * (height * width + width * length + length * height)

    def wrapper_size(self) -> int:
        return self.perimeter() + self.smallest_area()

    def ribbon_size(self) -> int:
        return self.smallest_perimeter() + self.volume()


def _as_paper(data):
    return Paper(*map(int, data.split("x")))


def get_input_data() -> Iterator[Paper]:
    return map(_as_paper, read_from_file(__file__, DAY))


def part_1():
    return sum(i.wrapper_size() for i in get_input_data())


def part_2():
    return sum(i.ribbon_size() for i in get_input_data())


def run():
    return dict(part_1=part_1(), part_2=part_2())
