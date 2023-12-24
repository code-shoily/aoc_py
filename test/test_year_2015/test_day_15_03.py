from year_2015.day_15_03 import get_input_data, run_15_3


def test_day_1_works():
    parsed_input = get_input_data()
    assert run_15_3(parsed_input) == (2081, 2341)