#!/usr/bin/python3
"""Function that defines a text file-reading function"""


def read_file(filename=""):
    """prints the contents of a UTF8 text file"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
