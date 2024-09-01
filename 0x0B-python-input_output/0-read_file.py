#!/usr/bin/python3
"""0-read_file"""


def read_file(filename=""):
    """function that reads a text file"""
    with open(filename, mode="r", encoding="utf-8") as f:
        print(f.read(), end="")
