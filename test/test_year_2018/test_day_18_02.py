from year_2018.day_18_02 import get_input_data, run_18_2


def test_day_18_2_works():
    parsed_input = get_input_data()
    assert run_18_2(parsed_input) == (7221, "mkcdflathzwsvjxrevymbdpoq")
