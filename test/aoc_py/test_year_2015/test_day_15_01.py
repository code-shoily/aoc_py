from aoc_py.year_2015.day_15_01 import get_input_data, run_15_1


def test_day_1_works():
    parsed_input = get_input_data()
    assert run_15_1(parsed_input) == (232, 1783)
