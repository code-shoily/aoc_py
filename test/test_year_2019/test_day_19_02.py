
from year_2019.day_19_02 import get_input_data, run_19_2


def test_day_19_2_works():
    parsed_input = get_input_data()
    assert run_19_2(parsed_input) == (3_562_624, 8298)
