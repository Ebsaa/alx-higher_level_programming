#!/usr/bin/python3
"""Function that defines a class Student"""


class Student:
    """represent a student."""

    def __init__(self, first_name, last_name, age):
        """rnitializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """gets a dictionary representation of the Student.
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """replaces all attributes of the Student
        """
        for k, v in json.items():
            setattr(self, k, v)
