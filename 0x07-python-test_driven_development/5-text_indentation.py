#!/usr/bin/python3
"""
This is a simple module to print text


"""


def text_indentation(text):
    """
    prints text with new lines after . ? :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    print("{}".format(text))
