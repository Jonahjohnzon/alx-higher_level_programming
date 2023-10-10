#!/bin/python3
""" load from JSON"""
import json


def load_from_json_file(filename):
    """JSON file"""
    with open(filename) as fil:
        return json.load(fil)
