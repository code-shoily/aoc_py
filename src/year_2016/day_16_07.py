"""Advent of Code Year 2016, Day 7 - <?TITLE?>
Problem Link: https://adventofcode.com/2016/day/7
Difficulty:
Tags:
"""

from dataclasses import dataclass

from helpers.input import read_input_lines

DAY = 7


@dataclass(frozen=True)
class IPv7:
    seq: list[str]
    hn_seq: list[str]

    def supports_tls(self) -> bool:
        return any([self.has_abba(i) for i in self.seq]) and not any(
            [self.has_abba(i) for i in self.hn_seq]
        )

    def supports_ssl(self) -> bool:
        abas = []
        for s in self.seq:
            abas.extend(self.get_abas(s))

        for aba in abas:
            for hn in self.hn_seq:
                if self.has_bab(hn, aba):
                    return True

        return False

    @staticmethod
    def has_abba(data: str) -> bool:
        left, right, limit = 0, 4, len(data)

        while right <= limit:
            match [*data][left:right]:
                case [a, b, c, d] if a == d and b == c and a != b:
                    return True
            left += 1
            right += 1

        return False

    @staticmethod
    def get_abas(data: str) -> list[str]:
        abas = []
        left, right, limit = 0, 3, len(data)

        while right <= limit:
            match [*data][left:right]:
                case [a, b, c] if a == c and a != b:
                    abas.append(f"{a}{b}{c}")

            left += 1
            right += 1

        return abas

    @staticmethod
    def has_bab(data: str, aba: str) -> bool:
        [a, b, _] = list(aba)
        return f"{b}{a}{b}" in data


InputType = list[IPv7]
OutputType = tuple[int, int]


def parse_ipv7(packet: str) -> IPv7:
    packets = packet.replace("[", "]").split("]")
    return IPv7(packets[::2], packets[1::2])


def get_input_data() -> InputType:
    return [parse_ipv7(i) for i in read_input_lines(__file__, DAY)]


def part_1(data: InputType) -> int:
    return len([i for i in data if i.supports_tls()])


def part_2(data: InputType) -> int:
    return len([i for i in data if i.supports_ssl()])


def run_16_7(data: InputType) -> tuple[int, int]:
    return part_1(data), part_2(data)


if __name__ == "__main__":
    parsed_input = get_input_data()
    print(run_16_7(parsed_input))
