from year_2020.day_20_04 import get_input_data, run_20_4


def test_day_20_4_works():
    parsed_input = get_input_data()
    assert run_20_4(parsed_input) == (233, 111)
