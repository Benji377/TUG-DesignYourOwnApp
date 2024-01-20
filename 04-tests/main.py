#!/usr/bin/env python3

def add_numbers(a, b):
    """
    Function to add two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def multiply_numbers(a, b):
    """
    Multiply two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The product of the two numbers.
    """
    return a * b


def check_palindrome(word):
    """
    Check if a word is a palindrome.

    Parameters:
        word (str): The word to be checked.

    Returns:
        bool: True if the word is a palindrome, False otherwise.
    """
    cleaned_word = word.lower().replace(" ", "")  # Remove spaces and convert to lowercase
    return cleaned_word == cleaned_word[::-1]


def main():
    """
    Main function to demonstrate the functions.
    """
    num1 = 5
    num2 = 3
    print(f"Adding {num1} and {num2}: {add_numbers(num1, num2)}")

    num3 = 4
    num4 = 6
    print(f"Multiplying {num3} and {num4}: {multiply_numbers(num3, num4)}")

    word = "A man a plan a canal Panama"
    print(f"Checking if '{word}' is a palindrome: {check_palindrome(word)}")


if __name__ == "__main__":
    main()
