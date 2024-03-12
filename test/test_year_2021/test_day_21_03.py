from year_2021.day_21_03 import get_input_data, run_21_3


def test_day_21_3_works():
    parsed_input = get_input_data()
    assert run_21_3(parsed_input) == (1_540_244, 4_203_981)
