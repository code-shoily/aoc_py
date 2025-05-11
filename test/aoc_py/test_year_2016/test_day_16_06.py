from aoc_py.year_2016.day_16_06 import get_input_data, run_16_6


def test_day_16_6_works():
    parsed_input = get_input_data()
    assert run_16_6(parsed_input) == ("qzedlxso", "ucmifjae")
