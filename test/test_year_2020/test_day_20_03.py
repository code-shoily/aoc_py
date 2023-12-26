from year_2020.day_20_03 import get_input_data, run_20_3


def test_day_20_3_works():
    parsed_input = get_input_data()
    assert run_20_3(parsed_input) == (272, 3_898_725_600)
