#!/usr/bin/env python3

def get_data_types():
    """
    Function to demonstrate different data types in Python.

    Returns:
        tuple: A tuple containing different data types, including integer, float, string, boolean, list, dictionary, tuple, and set.
    """
    integer_value = 42
    float_value = 3.14
    string_value = "Hello, Python!"
    boolean_value = True
    list_value = [1, 2, 3, 4, 5]
    dictionary_value = {"name": "Alice", "age": 30}
    tuple_value = (1, 2, 3)
    set_value = {1, 2, 3, 4, 5}

    return integer_value, float_value, string_value, boolean_value, list_value, dictionary_value, tuple_value, set_value


def main():
    """
    Main function to demonstrate different data types.
    """
    int_val, float_val, str_val, bool_val, list_val, dict_val, tuple_val, set_val = get_data_types()

    print("Integer:", int_val)
    print("Float:", float_val)
    print("String:", str_val)
    print("Boolean:", bool_val)
    print("List:", list_val)
    print("Dictionary:", dict_val)
    print("Tuple:", tuple_val)
    print("Set:", set_val)


if __name__ == "__main__":
    main()
