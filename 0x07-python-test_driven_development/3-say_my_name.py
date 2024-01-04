#!/usr/bin/python3
""" Say My Name"""


def say_my_name(first_name, last_name=""):
    """
    Write function that print the name
    Args:
    first_name: first name input
    last_name: last name input, default ""
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/3-say_my_name.txt")
