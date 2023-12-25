
from year_2017.day_17_01 import get_input_data, run_17_1


def test_day_17_1_works():
    parsed_input = get_input_data()
    assert run_17_1(parsed_input) == (1089, 1156)
