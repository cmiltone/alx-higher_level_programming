#!/usr/bin/python3
"""
module  sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == "__main__":
    import requests
    from sys import argv
    url = 'http://0.0.0.0:5000/search_user'
    letter = ""
    if len(argv) > 1:
        letter = argv[1]
    data = {'q': letter}
    req = requests.post(url, data=data)
    try:
        json = req.json()
        if json == {}:
            print("No result")
        else:
            print("[{}] {}".format(json.get('id'), json.get('name')))
    except ValueError:
        print("Not a valid JSON")
