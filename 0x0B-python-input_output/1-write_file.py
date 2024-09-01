#!/usr/bin/python3

"""1-write_file"""


def write_file(filename="", text=""):
    """wirite file function"""
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
