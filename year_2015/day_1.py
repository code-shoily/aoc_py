from helpers.input import read_from_file

DAY = 1


def get_input_data():
    return read_from_file(__file__, DAY)[0]


def get_floor(instructions):
    floor = 0
    for instruction in instructions:
        if instruction == "(":
            floor += 1
        else:
            floor -= 1

    return floor


def part_1():
    return get_floor(get_input_data())


def get_basement_position(instructions):
    floor = 0
    for (position, instruction) in enumerate(instructions):
        if floor == -1:
            return position
        elif instruction == "(":
            floor += 1
        else:
            floor -= 1


def part_2():
    return get_basement_position(get_input_data())


def run():
    return dict(part_1=part_1(), part_2=part_2())
