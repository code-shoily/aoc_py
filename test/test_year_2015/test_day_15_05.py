from year_2015.day_15_05 import get_input_data, run_15_5


def test_day_15_5_works():
    parsed_input = get_input_data()
    assert run_15_5(parsed_input) == (255, 55)
