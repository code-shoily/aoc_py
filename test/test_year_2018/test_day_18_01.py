
from year_2018.day_18_01 import get_input_data, run_18_1


def test_day_18_1_works():
    parsed_input = get_input_data()
    assert run_18_1(parsed_input) == (590, 83445)
