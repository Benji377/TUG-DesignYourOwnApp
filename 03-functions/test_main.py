from main import greet_user, calculate_sum, is_prime


def test_greet_user():
    assert greet_user("Alice") == "Hello, Alice!"
    assert greet_user("Bob") == "Hello, Bob!"


def test_calculate_sum():
    assert calculate_sum(3, 5) == 8
    assert calculate_sum(0, 0) == 0
    assert calculate_sum(-1, 1) == 0


def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(4) == False
    assert is_prime(1) == False
