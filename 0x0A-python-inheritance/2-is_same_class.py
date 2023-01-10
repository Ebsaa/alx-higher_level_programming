#!/usr/bin/python3
"""Checks if object is an instance of a class"""


def is_same_class(obj, a_class):
    """If object is an instance of the
    class Return True, else return false
    """
    return (type(obj) == a_class)
