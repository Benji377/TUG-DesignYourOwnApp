from main import check_even_odd, find_largest_number, check_grade


def test_check_even_odd():
    assert check_even_odd(4) == "Even"
    assert check_even_odd(7) == "Odd"


def test_find_largest_number():
    assert find_largest_number(3, 7, 5) == 7
    assert find_largest_number(10, 2, 9) == 10


def test_check_grade():
    assert check_grade(95) == "A"
    assert check_grade(85) == "B"
    assert check_grade(75) == "C"
    assert check_grade(65) == "D"
    assert check_grade(55) == "F"
