
from year_2023.day_23_01 import get_input_data, run_23_1


def test_day_23_1_works():
    parsed_input = get_input_data()
    assert run_23_1(parsed_input) == (53194, 54249)
