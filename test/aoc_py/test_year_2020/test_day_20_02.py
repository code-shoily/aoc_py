from aoc_py.year_2020.day_20_02 import get_input_data, run_20_2


def test_day_20_2_works():
    parsed_input = get_input_data()
    assert run_20_2(parsed_input) == (607, 321)
