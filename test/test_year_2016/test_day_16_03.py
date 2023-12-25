from year_2016.day_16_03 import get_input_data, run_16_3


def test_day_16_3_works():
    parsed_input = get_input_data()
    assert run_16_3(parsed_input) == (993, 1849)
