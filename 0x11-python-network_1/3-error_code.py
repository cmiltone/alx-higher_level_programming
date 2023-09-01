#!/usr/bin/python3
"""
module fetches from
https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    from urllib import request, error
    from sys import argv
    url = argv[1]
    try:
        with request.urlopen(url) as response:
            body = response.read()
            print("{}".format(body.decode("utf-8")))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
