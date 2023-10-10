#!/usr/bin/python3
""" save to JSON"""
import json


def save_to_json_file(my_obj, filename):
    """write JSON file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
