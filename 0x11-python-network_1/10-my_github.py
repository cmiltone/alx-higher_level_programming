#!/usr/bin/python3
"""
module takes your GitHub credentials
(username and password) and
uses the GitHub API to display your id
"""


if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv
    uname = argv[1]
    password = argv[2]
    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(uname, password)
    req = requests.get(url, auth=auth)
    try:
        json = req.json()
        print("{}".format(json.get('id')))
    except ValueError:
        pass
