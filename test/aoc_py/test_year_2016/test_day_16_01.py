from aoc_py.year_2016.day_16_01 import get_input_data, run_16_1


def test_day_1_works():
    parsed_input = get_input_data()
    assert run_16_1(parsed_input) == (253, 126)
