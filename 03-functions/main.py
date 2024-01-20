#!/usr/bin/env python3

def greet_user(name):
    """
    Function to greet the user.

    Parameters:
        name (str): The name of the user.

    Returns:
        str: A greeting message with the user's name.
    """
    return "Hello, " + name + "!"


def calculate_sum(a, b):
    """
    Function to calculate the sum of two numbers.

    Parameters:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b


def is_prime(number):
    """
    Check if a number is prime.

    Parameters:
        number (int): The number to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def main():
    """
    This function is the entry point of the program.
    It prompts the user for their name, greets them, calculates the sum of two numbers,
    and checks if a number is prime.
    """
    user_name = input("Enter your name: ")
    greeting_message = greet_user(user_name)
    print(greeting_message)

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = calculate_sum(num1, num2)
    print("Sum:", result)

    prime_number = int(input("Check if number is prime: "))
    prime_number_res = is_prime(prime_number)
    # Using the ternary conditional operator to construct the message
    prime_status = "is" if prime_number_res else "is not"
    print(f"Number {prime_number} {prime_status} a prime number")


if __name__ == "__main__":
    main()
