#!/usr/bin/python3
"""
module sends a request to the URL and
displays the body of the response
also handles errors by displaying the
error code
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = argv[1]
    res = requests.get(url)
    code = res.status_code
    if code >= 400:
        print("Error code: {}".format(code))
    else:
        print(res.text)
