
from year_2016.day_16_02 import get_input_data, run_16_2


def test_day_16_2_works():
    parsed_input = get_input_data()
    assert run_16_2(parsed_input) == ('76792', 'A7AC3')
