#!/bin/bash
# sends post request with data
curl -X POST -s -d '{"email": "test@gmail.com", "subject": "I will always be here for PLD"}' "$1"
