from year_2015.day_15_01 import get_input_data, run


def test_day_1_works():
    parsed_input = get_input_data()
    assert run(parsed_input) == (232, 1783)