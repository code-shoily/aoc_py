from year_2023.day_23_02 import get_input_data, run_23_2


def test_day_23_2_works():
    parsed_input = get_input_data()
    assert run_23_2(parsed_input) == (2085, 79_315)
