from year_2023.day_23_04 import get_input_data, run_23_4


def test_day_23_4_works():
    parsed_input = get_input_data()
    assert run_23_4(parsed_input) == (24_542, 8_736_438)
