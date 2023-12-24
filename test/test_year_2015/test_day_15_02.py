from year_2015.day_15_02 import get_input_data, run_15_2


def test_day_1_works():
    parsed_input = get_input_data()
    assert run_15_2(parsed_input) == (1_606_483, 3_842_356)