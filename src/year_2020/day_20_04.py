"""Advent of Code Year 2020, Day 4 - Passport Processing
Problem Link: https://adventofcode.com/2020/day/4
Difficulty: xs
Tags: section-parse validation
"""
import itertools
from dataclasses import dataclass
from functools import reduce

from helpers.input import read_input_lines

DAY = 4


@dataclass(frozen=True)
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: str

    def is_valid(self):
        return reduce(
            lambda acc, fun: acc and getattr(self, fun)(),
            filter(lambda i: i.startswith("is_valid_"), dir(self)),
            True,
        )

    def is_valid_byr(self) -> bool:
        return self.is_within("byr", 1920, 2002)

    def is_valid_iyr(self) -> bool:
        return self.is_within("iyr", 2010, 2020)

    def is_valid_eyr(self) -> bool:
        return self.is_within("eyr", 2020, 2030)

    def is_valid_hgt(self) -> bool:
        if (height := self.hgt.strip("cm")) and height != self.hgt:
            return 150 <= int(height) <= 193
        elif (height := self.hgt.strip("in")) and height != self.hgt:
            return 59 <= int(height) <= 76
        return False

    def is_valid_hcl(self) -> bool:
        if not self.hcl.startswith("#") or len(self.hcl) != 7:
            return False

        try:
            int(self.hcl.strip("#"), 16)
        except ValueError:
            return False

        return True

    def is_valid_ecl(self) -> bool:
        return self.ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    def is_valid_pid(self) -> bool:
        return len(self.pid) == 9 and self.pid.isdigit()

    def is_within(self, attr, i, f):
        return i <= int(getattr(self, attr)) <= f


def make_passport(lines: list[str]) -> Passport | None:
    merged_tokens = " ".join(lines).split(" ")
    tokens = {"cid": ""} | dict([i.split(":") for i in merged_tokens])
    try:
        passport = Passport(**tokens)
        return passport
    except TypeError:
        return None


InputType = list[Passport]
OutputType = tuple[int, int]


def get_input_data() -> InputType:
    lines = read_input_lines(__file__, DAY)
    passports = [make_passport(p) for s, p in itertools.groupby(lines, bool) if s]
    return list(filter(None, passports))


def part_1(data: InputType) -> int:
    return len(data)


def part_2(data: InputType) -> int:
    return len(list(filter(lambda p: p.is_valid(), data)))


def run_20_4(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_20_4(parsed_input))
