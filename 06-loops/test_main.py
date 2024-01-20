from main import calculate_factorial_with_while_loop


def test_calculate_factorial_with_while_loop():
    assert calculate_factorial_with_while_loop(0) == 1
    assert calculate_factorial_with_while_loop(1) == 1
    assert calculate_factorial_with_while_loop(5) == 120
