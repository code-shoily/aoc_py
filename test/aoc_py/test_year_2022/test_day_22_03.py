from aoc_py.year_2022.day_22_03 import get_input_data, run_22_3


def test_day_22_3_works():
    parsed_input = get_input_data()
    assert run_22_3(parsed_input) == (8233, 2821)
