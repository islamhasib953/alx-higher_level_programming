#!/usr/bin/python3
"""100-my_int"""


class MyInt(int):
    """class MyInt that inherits from int"""

    def __eq__(self, value):
        """Returns the opposite of the == operator"""
        return super().__ne__(value)

    def __ne__(self, value):
        """Returns the opposite of the != operator"""
        return super().__eq__(value)
