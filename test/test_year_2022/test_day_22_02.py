from year_2022.day_22_02 import get_input_data, run_22_2


def test_day_22_2_works():
    parsed_input = get_input_data()
    assert run_22_2(parsed_input) == (12_645, 11_756)
