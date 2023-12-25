
from year_2021.day_21_02 import get_input_data, run_21_2


def test_day_21_2_works():
    parsed_input = get_input_data()
    assert run_21_2(parsed_input) == (1_660_158, 1_604_592_846)
