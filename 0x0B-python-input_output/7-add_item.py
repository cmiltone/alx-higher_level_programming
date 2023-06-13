#!/usr/bin/python3
"""module to add all arguments to list and save to file"""
import sys


def add_item():
    """adds all arguments to list and save to file"""
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_file = __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    args = sys.argv[1:]
    save_to_json_file(args, filename)

    data = load_from_file(filename)
    print(data)


if __name__ == "__main__":
    add_item()
