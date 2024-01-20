from main import manipulate_list, process_tuple, manipulate_set, process_dictionary


def test_manipulate_list():
    assert manipulate_list([1, 2, 3, 4, 5]) == [1, 2, 4, 5, 6]


def test_process_tuple():
    assert process_tuple((1, 2, 3, 4, 5)) == (1, 9, 3, 4, 5)


def test_manipulate_set():
    assert manipulate_set({1, 2, 3, 4, 5}) == {1, 3, 4, 5, 7}


def test_process_dictionary():
    assert process_dictionary({"name": "Alice", "age": 30, "size": "medium"}) == {"name": "Alice", "age": 30,
                                                                                  "color": "blue"}
