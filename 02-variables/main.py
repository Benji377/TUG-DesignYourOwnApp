#!/usr/bin/env python3

def demonstrate_variables_usage():
    """
    Demonstrates the usage of variables in Python.

    Variables are containers for storing data values.
    You can assign values to variables using the assignment operator (=).
    Variables can store different types of data and can be used in operations.
    This function showcases the creation, updating, and usage of variables.
    """
    name = "Alice"
    age = 30
    is_adult = True

    age = 31

    greeting = "Hello, " + name + "!"

    print(greeting)
    print("Age:", age)

    if is_adult:
        print(name, "is an adult.")
    else:
        print(name, "is not an adult.")


def main():
    """
    This is the main function of the program.
    It calls the function to demonstrate variable usage.
    """
    demonstrate_variables_usage()


if __name__ == "__main__":
    main()

