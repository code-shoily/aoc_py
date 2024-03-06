from year_2016.day_16_07 import get_input_data, run_16_7


def test_day_16_7_works():
    parsed_input = get_input_data()
    assert run_16_7(parsed_input) == (105, 258)
