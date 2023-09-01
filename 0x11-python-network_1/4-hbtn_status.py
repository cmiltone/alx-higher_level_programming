#!/usr/bin/python3
"""
module fetches from
https://alx-intranet.hbtn.io/status
using requests
"""


if __name__ == "__main__":
    import requests
    url = 'https://alx-intranet.hbtn.io/status/'
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res)))
    print("\t- content: {}".format(res))
