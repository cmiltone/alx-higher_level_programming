#!/usr/bin/python3
"""
module fetches from
https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    from urllib import request, parse
    from sys import argv
    url = argv[1]
    email = argv[2]
    data = parse.urlencode({'email': email}).encode()
    req = request.Request(url, data=data)
    with request.urlopen(req) as response:
        content = response.read()
        print("{}".format(content.decode("utf-8")))
