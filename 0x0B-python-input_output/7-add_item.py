#!/usr/bin/python3
"""FUNCTION"""
import sys


if __name__ == "__main__":
    save = __import__('5-save_to_json_file').save_to_json_file
    load = __import__('6-load_from_json_file').load_from_json_file
    try:
        item = load("add_item.json")
    except FileNotFoundError:
        item = []
    item.extend(sys.argv[1:])
    save(item, "add_item.json")
