"""Advent of Code Year 2016, Day 3 - Squares With Three Sides

Problem Link: https://adventofcode.com/2016/day/3
"""
from helpers.input import read_input_lines


def get_input_data():
    return read_input_lines(__file__, 3)


def split_by_spaces(line: str) -> list[int]:
    """
    Splits by multiple number of spaces

    :param line: The line to tokenize
    :return: list of tokens that were joined by spaces

    >>> split_by_spaces("1 2     34  5    ")
    [1, 2, 5, 34]

    """
    return sorted([int(i) for i in line.split(" ") if i])


def is_triangle(sides: list[int]) -> bool:
    """
    Checks if sides in the list can ever form triangle.

    >>> is_triangle([5, 10, 25])
    False

    >>> is_triangle([2, 2, 3])
    True

    """
    a, b, c = sides
    return (a + b) > c


def part_1():
    list_of_sides = map(split_by_spaces, get_input_data())
    return sum(map(is_triangle, list_of_sides))


def chunkify(lst: list[any], by=3) -> list[list[any]]:
    """
    Chunks `lst` as list of `by` elements

    :param lst: The list to chunkify
    :param by: Size of each chunk (default to 3)
    :return: Chunked List

    >>> chunkify([1, 2, 3, 4, 5, 6, 7, 8, 9])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    """
    return [lst[i : i + 3] for i in range(0, len(lst), by)]


def get_vertical_sides(dataset: list[str]) -> list[list[int]]:
    """
    Rearranges the matrix so that three vertical numbers form sides of a triangle.

    :param matrix: Input data, list of list where first list has three items
    :return: Rearranged list of sides sorted by value

    >>> get_vertical_sides(['1  2  3', '4  5  6', '7  8  9'])
    [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    """
    parsed_data = list(
        map(int, filter(None, " ".join([i.strip() for i in dataset]).split(" ")))
    )

    sides = parsed_data[0::3] + parsed_data[1::3] + parsed_data[2::3]

    return [sorted(i) for i in chunkify(sides)]


def part_2():
    return sum([is_triangle(i) for i in get_vertical_sides(get_input_data())])


def run():
    """
    Solution runner
    :return: The solutions of both parts of day 3 for year 2016

    >>> result = run()
    >>> result == {'part_1': 993, 'part_2': 1849}
    True

    """
    return {
        "part_1": part_1(),
        "part_2": part_2(),
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    print(run())
