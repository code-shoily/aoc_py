from year_2020.day_20_08 import get_input_data, run_20_8


def test_day_20_8_works():
    parsed_input = get_input_data()
    assert run_20_8(parsed_input) == (2080, 2477)
