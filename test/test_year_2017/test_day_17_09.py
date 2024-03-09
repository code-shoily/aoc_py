from year_2017.day_17_09 import get_input_data, run_17_9


def test_day_17_9_works():
    parsed_input = get_input_data()
    assert run_17_9(parsed_input) == (7616, 3838)
