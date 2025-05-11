from aoc_py.year_2016.day_16_04 import get_input_data, run_16_4


def test_day_16_4_works():
    parsed_input = get_input_data()
    assert run_16_4(parsed_input) == (158_835, 993)
