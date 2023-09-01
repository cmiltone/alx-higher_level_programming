#!/usr/bin/python3
"""
module fetches from
https://alx-intranet.hbtn.io/status
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    req = requests.post(url, data=data)
    print("{}".format(req.text))
