#!/usr/bin/env python3

def check_even_odd(number):
    """
    Function to check if a number is even or odd.

    Parameters:
        number (int): The number to be checked.

    Returns:
        str: "Even" if the number is even, "Odd" if the number is odd.
    """
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def find_largest_number(a, b, c):
    """
    Function to find the largest number among three numbers.

    Parameters:
        a (int): First number.
        b (int): Second number.
        c (int): Third number.

    Returns:
        int: The largest number among a, b, and c.
    """
    return max(a, b, c)


def check_grade(score):
    """
    Function to assign grades based on the score.

    Parameters:
        score (int): The score to be evaluated.

    Returns:
        str: The grade assigned based on the score.
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def main():
    """
    Main function to demonstrate the functions interactively.
    """
    num = int(input("Enter a number to check if it's even or odd: "))
    print(f"{num} is {check_even_odd(num)}")

    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))
    print(f"The largest number among {num1}, {num2}, and {num3} is {find_largest_number(num1, num2, num3)}")

    score = int(input("Enter the score to check the grade: "))
    print(f"The grade for the score {score} is {check_grade(score)}")


if __name__ == "__main__":
    main()
