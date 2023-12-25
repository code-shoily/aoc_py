
from year_2017.day_17_04 import get_input_data, run_17_4


def test_day_17_4_works():
    parsed_input = get_input_data()
    assert run_17_4(parsed_input) == (455, 186)
