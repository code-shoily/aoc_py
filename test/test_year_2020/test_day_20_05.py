from year_2020.day_20_05 import get_input_data, run_20_5


def test_day_20_5_works():
    parsed_input = get_input_data()
    assert run_20_5(parsed_input) == (930, 515)
