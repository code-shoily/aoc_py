
from year_2019.day_19_01 import get_input_data, run_19_1


def test_day_19_1_works():
    parsed_input = get_input_data()
    assert run_19_1(parsed_input) == (3_421_505, 5_129_386)
