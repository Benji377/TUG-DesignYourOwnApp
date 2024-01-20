#!/usr/bin/env python3

def manipulate_list(input_list):
    """
    Function to manipulate a list.

    Parameters:
        input_list (list): The input list to be manipulated.

    Returns:
        list: The modified list after performing the operations.
    """
    # Add an element to the end of the list
    input_list.append(6)
    # Remove the first occurrence of 3 in the list
    input_list.remove(3)
    # Return the modified list
    return input_list


def process_tuple(input_tuple):
    """
    Process a tuple by converting it to a list, changing the second element to 9,
    and converting the list back to a tuple.

    Parameters:
        input_tuple (tuple): The input tuple to be processed.

    Returns:
        tuple: The modified tuple with the second element changed to 9.
    """
    # Function to process a tuple
    # Convert the tuple to a list
    tuple_list = list(input_tuple)
    # Change the second element to 9
    tuple_list[1] = 9
    # Convert the list back to a tuple
    modified_tuple = tuple(tuple_list)
    return modified_tuple


def manipulate_set(input_set):
    """
    Function to manipulate a set.

    Parameters:
        input_set (set): The set to be manipulated.

    Returns:
        set: The manipulated set.
    """
    # Add an element to the set
    input_set.add(7)
    # Remove an element from the set
    input_set.remove(2)
    return input_set


def process_dictionary(input_dict):
    """
    Function to process a dictionary.

    Parameters:
        input_dict (dict): The dictionary to be processed.

    Returns:
        dict: The processed dictionary.
    """
    # Add a new key-value pair to the dictionary
    input_dict["color"] = "blue"
    # Remove an existing key-value pair from the dictionary
    del input_dict["size"]
    return input_dict


def main():
    """
    Main function to demonstrate collection-related functions.
    """
    print("Manipulating list:")
    print(manipulate_list([1, 2, 3, 4, 5]))

    print("\nProcessing tuple:")
    print(process_tuple((1, 2, 3, 4, 5)))

    print("\nManipulating set:")
    print(manipulate_set({1, 2, 3, 4, 5}))

    print("\nProcessing dictionary:")
    print(process_dictionary({"name": "Alice", "age": 30, "size": "medium"}))


if __name__ == "__main__":
    main()
