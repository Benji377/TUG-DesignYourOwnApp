#!/usr/bin/env python3

def print_numbers_with_for_loop(n):
    """
    Function to print numbers from 1 to n using a for loop.

    Parameters:
        n (int): The upper limit of the range.

    Returns:
        None
    """
    for i in range(1, n + 1):
        print(i)


def calculate_factorial_with_while_loop(n):
    """
    Calculate the factorial of a number using a while loop.

    Parameters:
        n (int): The number for which factorial needs to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1
    return factorial


def generate_multiplication_table(n):
    """
    Generates a multiplication table for a given number.

    Parameters:
        n (int): The number for which the multiplication table is generated.

    Returns:
        None
    """
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")


def main():
    """
    Main function to demonstrate loop-related functions.
    """
    print("Printing numbers from 1 to 5:")
    print_numbers_with_for_loop(5)

    num = 5
    print(f"Factorial of {num} is {calculate_factorial_with_while_loop(num)}")

    print(f"\nMultiplication table for {num}:")
    generate_multiplication_table(num)


if __name__ == "__main__":
    main()
