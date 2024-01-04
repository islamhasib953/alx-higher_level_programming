#!/usr/bin/python3
""" Print Square using # """


def print_square(size):
    """
    Print Square using #
    Args:
        size (int): size of a square
    """
    if size == 0:
        return
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    print("\n".join("#" * size for x in range(size)))


if __name__ == "__main__":
    import doctest

    doctest.testfile("tests/4-print_square.txt")
