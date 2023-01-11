#!/usr/bin/python3
"""Function that defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """creates a python object from a given JSON file"""
    with open(filename) as f:
        return json.load(f)
