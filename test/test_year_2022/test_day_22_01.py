from year_2022.day_22_01 import get_input_data, run_22_1


def test_day_22_1_works():
    parsed_input = get_input_data()
    assert run_22_1(parsed_input) == (70720, 207148)
