from year_2021.day_21_01 import get_input_data, run_21_1


def test_day_21_1_works():
    parsed_input = get_input_data()
    assert run_21_1(parsed_input) == (1139, 1103)
