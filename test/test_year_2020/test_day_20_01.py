from year_2020.day_20_01 import get_input_data, run_20_1


def test_day_20_1_works():
    parsed_input = get_input_data()
    assert run_20_1(parsed_input) == (1_014_624, 80_072_256)
