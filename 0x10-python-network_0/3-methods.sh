#!/bin/bash
# sends delete request and prints body of response
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
