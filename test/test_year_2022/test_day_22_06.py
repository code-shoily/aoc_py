from year_2022.day_22_06 import get_input_data, run_22_6


def test_day_22_6_works():
    parsed_input = get_input_data()
    assert run_22_6(parsed_input) == (1651, 3837)
