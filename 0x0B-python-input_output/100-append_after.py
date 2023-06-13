#!/usr/bin/python3
"""module to insert line of text to a file"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    """
    s = ""
    with open(filename) as f:
        for line in f:
            s = s + line
            if search_string in line:
                s = s + new_string
    with open(filename, "w+") as f2:
        f2.write(s)
