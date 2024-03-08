from year_2022.day_22_04 import get_input_data, run_22_4


def test_day_22_4_works():
    parsed_input = get_input_data()
    assert run_22_4(parsed_input) == (518, 909)
