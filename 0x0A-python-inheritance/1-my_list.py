#!/usr/bin/python3
"""1-my_list"""


class MyList(list):
    """MyList class that inherits from list and adds a print_sorted method."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        print(sorted(self))
