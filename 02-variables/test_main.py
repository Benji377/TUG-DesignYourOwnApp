from main import demonstrate_variables_usage


# Since this function only prints output, there are no specific tests needed.
def test_demonstrate_variables_usage(capsys):
    demonstrate_variables_usage()
    captured = capsys.readouterr()
    assert "Hello, Alice!\n" in captured.out
