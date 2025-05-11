import pytest
from aoc_py.year_2017.day_17_05 import get_input_data, run_17_5


@pytest.mark.slow
def test_day_17_5_works():
    parsed_input = get_input_data()
    assert run_17_5(parsed_input) == (372_671, 25_608_480)
