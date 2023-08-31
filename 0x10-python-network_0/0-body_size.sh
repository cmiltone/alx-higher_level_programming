#!/bin/bash
# script prints size of body of response in bytes
curl -s "$1" | wc -c
