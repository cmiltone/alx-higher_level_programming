#!/usr/bin/python3
"""module to add all arguments to list and save to file"""
import sys


def add_item():
    """adds all arguments to list and save to file"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    data = []
    try:
        data = load_from_file(filename)
    except (FileNotFoundError):
        pass
    args = sys.argv[1:]
    if len(data) > 0:
        data = data + args
    else:
        data = args
    save_to_json_file(data, filename)


if __name__ == "__main__":
    add_item()
