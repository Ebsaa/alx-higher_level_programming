#!/usr/bin/python3
"""checks if object is an instance of a class that
inherited from the specified class or not
"""


def inherits_from(obj, a_class):
    """If object is an instance of a class that inherited
    (directly or indirectly) from
    the specified class returns True, else return False
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
