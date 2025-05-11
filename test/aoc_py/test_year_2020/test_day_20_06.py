from aoc_py.year_2020.day_20_06 import get_input_data, run_20_6


def test_day_20_6_works():
    parsed_input = get_input_data()
    assert run_20_6(parsed_input) == (6885, 3550)
