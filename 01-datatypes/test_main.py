from main import get_data_types


def test_get_data_types():
    int_val, float_val, str_val, bool_val, list_val, dict_val, tuple_val, set_val = get_data_types()

    assert isinstance(int_val, int)
    assert isinstance(float_val, float)
    assert isinstance(str_val, str)
    assert isinstance(bool_val, bool)
    assert isinstance(list_val, list)
    assert isinstance(dict_val, dict)
    assert isinstance(tuple_val, tuple)
    assert isinstance(set_val, set)
