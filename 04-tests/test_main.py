from main import add_numbers, multiply_numbers, check_palindrome


def test_add_numbers():
    assert add_numbers(3, 5) == 8
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0


def test_multiply_numbers():
    assert multiply_numbers(3, 5) == 15
    assert multiply_numbers(0, 5) == 0
    assert multiply_numbers(-1, 5) == -5


def test_check_palindrome():
    assert check_palindrome("racecar") == True
    assert check_palindrome("hello") == False
    assert check_palindrome("A man a plan a canal Panama") == True
