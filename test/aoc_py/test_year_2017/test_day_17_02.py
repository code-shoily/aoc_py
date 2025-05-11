from aoc_py.year_2017.day_17_02 import get_input_data, run_17_2


def test_day_17_2_works():
    parsed_input = get_input_data()
    assert run_17_2(parsed_input) == (32020, 236)
